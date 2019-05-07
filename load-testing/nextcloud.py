import random
import string

from gevent.pool import Pool
from locust import task, HttpLocust, TaskSet, log
from locust.clients import HttpSession
from common.browser import Browser
from common.webdav import Webdav


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

    @task(1)
    def browse_webdav(self):
        pool = Pool(4)

        webdav = Webdav(self.client, self.requesttoken)

        for response in webdav.propfind('/remote.php/dav/files/admin/', deep=True):
            if response.hasPreview:
                pool.spawn(self.client.get, f'/core/preview?fileId={response.fileid}&c={response.etag}&x=250&y=250&forceIcon=0')

        pool.join()

    @task(5)
    def upload_webdav(self):
        webdav = Webdav(self.client, self.requesttoken)

        letters = string.ascii_lowercase
        filename = ''.join(random.choice(letters) for i in range(12))

        data = ''.join(random.choice(letters) for i in range(1024 * 512))
        webdav.put('/remote.php/dav/files/admin/' + filename, data.encode('utf-8'))

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
        values['user'] = 'admin'
        values['password'] = 'admin'
        login_form.submit(values)

    def logout(self):
        self.browser.navigate('/logout')


class NextcloudUser(HttpLocust):
    task_set = NextcloudUserBehaviour
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 500
    max_wait = 1000


if __name__ == '__main__':
    NextcloudUser().run()
