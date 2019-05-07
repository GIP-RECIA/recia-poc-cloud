from typing import Optional, Dict

from bs4 import BeautifulSoup, Tag
from gevent.pool import Pool
from locust.clients import Response, HttpSession
from locust.exception import LocustError


class Browser:
    def __init__(self, client: HttpSession):
        self.client = client
        self.history = []  # type: list[GoResponse]
        self.resources = Resources(client)

    def dom(self, r: Response):
        dom = BeautifulSoup(r.content, 'html.parser', from_encoding=r.encoding)
        return dom

    def navigate(self, url, download=True, history=True, **kwargs):
        response = self.client.get(url, **kwargs)
        return self.handle_response(response, download, history)

    def handle_response(self, response, download=True, history=True):
        if response.status_code != 200:
            raise LocustError()

        dom = self.dom(response)
        resources = self.resources.get(dom, download)
        go_response = GoResponse(resources, response, dom)
        if history:
            self.history.append(go_response)
        return go_response

    def form(self, selector=None, tag: Optional[Tag] = None):
        if not tag:
            tag = self.last.dom

        if selector:
            tag = tag.select_one(selector)

        if not tag or tag.name != 'form':
            raise LocustError("Is not a form")

        return Form(self, tag)

    @property
    def last(self):
        return self.history[-1]

    def follow(self, link_text: str, tag: Optional[Tag] = None):
        if not tag:
            tag = self.last.dom
        for a in tag.select("a[href]"):
            if a.text == link_text:
                return self.navigate(a.attrs['href'])
        raise LocustError("Link not found (" + link_text + ")")


class Resources:
    def __init__(self, client: HttpSession):
        self.images = {}  # type: dict[str, Optional[Response]]
        self.scripts = {}  # type: dict[str, Optional[Response]]
        self.links = {}  # type: dict[str, Optional[Response]]
        self.client = client

    def get(self, dom: Tag, download=True):
        resources = Resources(self.client)

        for img in dom.findAll("img"):
            if "src" in img.attrs:
                resources.images[img.attrs["src"]] = self.images.get(img.attrs["src"])
        for script in dom.findAll("script"):
            if "src" in script.attrs:
                resources.scripts[script.attrs["src"]] = self.scripts.get(script.attrs["src"])
        for link in dom.findAll("link"):
            if "href" in link.attrs:
                resources.links[link.attrs["href"]] = self.links.get(link.attrs["href"])

        if download:
            pool = Pool(4)
            for url, response in resources.images.items():
                if not response:
                    pool.spawn(self.download_item, resources.images, url)
            for url, response in self.scripts.items():
                if not response:
                    pool.spawn(self.download_item, resources.scripts, url)
            for url, response in self.links.items():
                if not response:
                    pool.spawn(self.download_item, resources.links, url)
            pool.join()

        self.update(resources)

        return resources

    def download_item(self, item, download_url):
        item[download_url] = self.client.get(download_url)

    def update(self, resources):
        self.images.update(resources.images)
        self.scripts.update(resources.scripts)
        self.links.update(resources.links)


class GoResponse:
    def __init__(self, resources: Resources, response: Response, dom: BeautifulSoup):
        self.resources = resources
        self.response = response
        self.dom = dom


class Form:
    def __init__(self, browser: Browser, dom: Tag):
        self.browser = browser
        self.dom = dom

    def values(self) -> Dict[str, str]:
        values = {}
        for input in self.dom.findAll('input'):
            if input.attrs.get('name') and input.attrs.get('type') != 'submit':
                values[input.attrs.get('name')] = input.attrs.get('value')
        return values

    def submit(self, values: Dict[str, str], **kwargs) -> GoResponse:
        method = "get"
        action = self.browser.last.response.request.url

        if 'method' in self.dom.attrs:
            method = self.dom.attrs['method'].lower()

        if 'action' in self.dom.attrs:
            action = self.dom.attrs['action']

        if method == 'post':
            return self.browser.handle_response(self.browser.client.post(action, values, **kwargs), download=True)
        elif method == 'get':
            return self.browser.handle_response(self.browser.client.get(action, **kwargs))  # TODO: Encode values in URL
        else:
            raise LocustError("Unsupported form method: " + method)
