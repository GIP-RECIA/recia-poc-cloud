from locust import task, HttpLocust, TaskSet, log
from locust.clients import HttpSession
from common.browser import Browser


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

    @task
    def task1(self):
        pass

    @task
    def task2(self):
        pass

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.browser.navigate('/login')
        self.wait()
        self.browser.follow("Direct log in")

    def logout(self):
        self.browser.follow()


class NextcloudUser(HttpLocust):
    task_set = NextcloudUserBehaviour
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 500
    max_wait = 1000


if __name__ == '__main__':
    NextcloudUser().run()
