import json
import os
import random
import string

from gevent.pool import Pool
from locust import task, HttpLocust
from locust.exception import LocustError

from common.nextcloud import NextcloudBrowserTaskSet
from common.webdav import Webdav


class NextcloudTaskSet(NextcloudBrowserTaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    @task(2)
    def navigate_apps_file(self):
        self.browser.navigate("/apps/files")

        webdav = Webdav(self.client, self.browser.requesttoken)

        pool = Pool(4)

        for response in webdav.propfind(
                f'/remote.php/dav/files/{self.browser.user}/',
                name='/remote.php/dav/files/{user}',
                deep=False):
            if response.hasPreview:
                pool.spawn(self.client.get, f'/core/preview',
                           name='/core/preview',
                           params={'fileId': response.fileid, 'c': response.etag, 'x': 250, 'y': 250, 'forceIcon': 0}
                           )

        pool.join()

    @task(2)
    def navigate_apps_activity(self):
        self.browser.navigate("/apps/activity")

        r = self.client.get("/ocs/v2.php/apps/activity/api/v2/activity/all?format=json&previews=true&since=0",
                            name="/ocs/v2.php/apps/activity/api/v2/activity/all",
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.browser.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API activity/all")

    @task(2)
    def navigate_apps_gallery(self):
        self.browser.navigate("/apps/gallery")

        r = self.client.get("/apps/gallery/config",
                            name="/apps/gallery/config",
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.browser.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API gallery/config")
        config = json.loads(r.text)

        r = self.client.get("/apps/gallery/files/list",
                            name="/apps/gallery/files/list",
                            params={"location": "",
                                    "features": ';'.join(config.get('features')),
                                    "etag": "",
                                    "mediatypes": ';'.join(config.get('mediatypes'))},
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.browser.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API gallery/config")
        galleries = json.loads(r.text)

        pool = Pool(4)
        for f in galleries['files']:
            pool.spawn(
                self.client.get, f"/apps/gallery/preview/{f['nodeid']}",
                name="/apps/gallery/preview/{nodeid}",
                params={'width': 200, 'height': 200}
            )
        pool.join()

    @task(1)
    def browse_webdav(self):
        pool = Pool(4)

        webdav = Webdav(self.client, self.browser.requesttoken)

        for response in webdav.propfind(f'/remote.php/dav/files/{self.browser.user}/',
                                        name="/remote.php/dav/files/{user}/",
                                        deep=True):
            if response.hasPreview:
                pool.spawn(self.client.get,
                           f'/core/preview',
                           name='/core/preview',
                           params={'fileId': response.fileid, 'c': response.etag, 'x': 250, 'y': 250, 'forceIcon': 0}
                           )

        pool.join()

    @task(10)
    def upload_webdav(self):
        webdav = Webdav(self.client, self.browser.requesttoken)

        letters = string.ascii_lowercase
        filename = ''.join(random.choice(letters) for i in range(12))

        data = os.urandom(1024 * 512)
        r = webdav.put(
            f'/remote.php/dav/files/{self.browser.user}/Locust/{filename}',
            name='/remote.php/dav/files/{user}/Locust/{filename}',
            data=data,
            catch_response=True
        )
        r.success()
        if r.status_code == 404:
            webdav.mkcol(
                f'/remote.php/dav/files/{self.browser.user}/Locust',
                name='/remote.php/dav/files/{user}/Locust',
            )
            webdav.put(
                f'/remote.php/dav/files/{self.browser.user}/Locust/{filename}',
                name='/remote.php/dav/files/{user}/Locust/{filename}',
                data=data)

        webdav.delete(
            f'/remote.php/dav/files/{self.browser.user}/Locust/{filename}',
            name='/remote.php/dav/files/{user}/Locust/{filename}'
        )
        webdav.delete(
            f'/remote.php/dav/files/{self.browser.user}/Locust',
            name='/remote.php/dav/files/{user}/Locust'
        )


class NextcloudLocust(HttpLocust):
    task_set = NextcloudTaskSet
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 1000
    max_wait = 5000


if __name__ == '__main__':
    NextcloudLocust().run()
