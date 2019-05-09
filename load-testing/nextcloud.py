import json
import os
import random
import string

from gevent.pool import Pool
from locust import task, HttpLocust, TaskSet
from locust.clients import HttpSession
from locust.exception import LocustError

from common.auth import get_random_user, get_user_password
from common.browser import Browser
from common.webdav import Webdav, WebdavError


class NextcloudUserBehaviour(TaskSet):
    # Add this for better code completion in IDE
    locust = None  # type: NextcloudUser

    def __init__(self, parent):
        super().__init__(parent)
        self.client.headers["Accept-Language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6"
        self.browser = Browser(self.client)

    # Add this for better code completion in IDE
    @property
    def client(self) -> HttpSession:
        return super().client

    @property
    def requesttoken(self):
        for history_item in reversed(self.browser.history):
            requesttokenTag = history_item.dom.select_one('head[data-requesttoken]')
            return requesttokenTag.attrs['data-requesttoken']
        return None

    @property
    def user(self):
        for history_item in reversed(self.browser.history):
            requesttokenTag = history_item.dom.select_one('head[data-user]')
            return requesttokenTag.attrs['data-user']
        return None

    @task(2)
    def navigate_apps_file(self):
        self.browser.navigate("/apps/files")

        webdav = Webdav(self.client, self.requesttoken)

        pool = Pool(4)

        for response in webdav.propfind(f'/remote.php/dav/files/{self.user}/', deep=False):
            if response.hasPreview:
                pool.spawn(self.client.get,
                           f'/core/preview?fileId={response.fileid}&c={response.etag}&x=250&y=250&forceIcon=0')

        pool.join()

    @task(2)
    def navigate_apps_activity(self):
        self.browser.navigate("/apps/activity")

        r = self.client.get("/ocs/v2.php/apps/activity/api/v2/activity/all?format=json&previews=true&since=0",
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API activity/all")

    @task(2)
    def navigate_apps_gallery(self):
        self.browser.navigate("/apps/gallery")

        r = self.client.get("/apps/gallery/config",
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API gallery/config")
        config = json.loads(r.text)

        r = self.client.get("/apps/gallery/files/list",
                            params={"location": "",
                                    "features": ';'.join(config.get('features')),
                                    "etag": "",
                                    "mediatypes": ';'.join(config.get('mediatypes'))},
                            headers={"OCS-APIREQUEST": "true", "requesttoken": self.requesttoken})
        if r.status_code != 200:
            raise LocustError("Invalid response for API gallery/config")
        galleries = json.loads(r.text)

        pool = Pool(4)
        for f in galleries['files']:
            pool.spawn(self.client.get, f"/apps/gallery/preview/{f['nodeid']}?width=200&height=200")
        pool.join()

    @task(1)
    def browse_webdav(self):
        pool = Pool(4)

        webdav = Webdav(self.client, self.requesttoken)

        for response in webdav.propfind(f'/remote.php/dav/files/{self.user}/', deep=True):
            if response.hasPreview:
                pool.spawn(self.client.get,
                           f'/core/preview?fileId={response.fileid}&c={response.etag}&x=250&y=250&forceIcon=0')

        pool.join()

    @task(10)
    def upload_webdav(self):
        webdav = Webdav(self.client, self.requesttoken)

        letters = string.ascii_lowercase
        filename = ''.join(random.choice(letters) for i in range(12))

        data = os.urandom(1024 * 512)
        r = webdav.put(f'/remote.php/dav/files/{self.user}/Locust/' + filename, data, catch_response=True)
        r.success()
        if r.status_code == 404:
            webdav.mkcol(f'/remote.php/dav/files/{self.user}/Locust')
            webdav.put(f'/remote.php/dav/files/{self.user}/Locust/' + filename, data)

        webdav.delete(f'/remote.php/dav/files/{self.user}/Locust/' + filename)
        webdav.delete(f'/remote.php/dav/files/{self.user}/Locust')

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.browser.navigate('/login')
        self.wait()
        self.browser.follow("Connexion directe")
        login_form = self.browser.form('form')
        values = login_form.values()

        values['user'] = get_random_user()
        values['password'] = get_user_password(values['user'])
        login_form.submit(values)

    def logout(self):
        self.browser.navigate('/logout')


class NextcloudUser(HttpLocust):
    task_set = NextcloudUserBehaviour
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 5000
    max_wait = 10000


if __name__ == '__main__':
    NextcloudUser().run()
