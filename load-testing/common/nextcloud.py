from typing import Optional

from locust import TaskSet, TaskSequence
from locust.clients import HttpSession

from common.auth import get_random_user, get_user_password
from common.browser import Browser


class NextcloudBase:
    def login(self):
        self.browser.navigate('/login')
        self.wait()
        self.browser.follow("Connexion directe")
        login_form = self.browser.form('form')
        values = login_form.values()

        values['user'] = get_random_user()
        values['password'] = get_user_password(values['user'])

        login_form.submit(values)

        self.browser.navigate('/')

    def logout(self):
        self.browser.navigate('/logout')


class NextcloudBrowser(Browser):
    def __init__(self, client: HttpSession):
        super().__init__(client)
        self.requesttoken = None  # type: Optional[str]
        self.user = None  # type: Optional[str]

    def navigate(self, url, **kwargs):
        history_item = super().navigate(url, **kwargs)
        requesttokenTag = history_item.dom.select_one('head[data-requesttoken]')
        if requesttokenTag:
            self.requesttoken = requesttokenTag.attrs['data-requesttoken']

        userTag = history_item.dom.select_one('head[data-user]')
        if userTag:
            self.user = userTag.attrs['data-user']

        return history_item


class NextcloudBrowserExtension:
    # Add this for better code completion in IDE
    client = None  # type: HttpSession

    def __init__(self, parent):
        self.client.headers["Accept-Language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6"
        if hasattr(parent, 'browser'):
            self.browser = parent.browser
        else:
            self.browser = NextcloudBrowser(self.client)


class NextcloudBrowserTaskSet(TaskSet, NextcloudBase, NextcloudBrowserExtension):
    def __init__(self, parent):
        super().__init__(parent)
        NextcloudBrowserExtension.__init__(self, parent)


class NextcloudBrowserTaskSequence(TaskSequence, NextcloudBase, NextcloudBrowserExtension):
    def __init__(self, parent):
        super().__init__(parent)
        NextcloudBrowserExtension.__init__(self, parent)
