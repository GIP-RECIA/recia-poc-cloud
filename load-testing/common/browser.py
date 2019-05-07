from typing import Optional

from bs4 import BeautifulSoup, Tag
from gevent.pool import Group
from locust.clients import Response, HttpSession
from locust.exception import StopLocust


class Browser:
    def __init__(self, client: HttpSession):
        self.client = client
        self.history = []  # type: list[GoResponse]
        self.resources = Resources(client)

    def dom(self, r: Response):
        dom = BeautifulSoup(r.content, 'html.parser', from_encoding=r.encoding)
        return dom

    def navigate(self, url, **kwargs):
        download = kwargs.pop('download', True)
        response = self.client.get(url, **kwargs)
        if response.status_code != 200:
            raise StopLocust()

        dom = self.dom(response)
        resources = self.resources.get(dom, download)
        go_response = GoResponse(resources, response, dom)
        self.history.append(go_response)

        return go_response

    @property
    def last(self):
        return self.history[-1]

    def follow(self, link_text: str, tag: Optional[Tag] = None):
        if not tag:
            tag = self.last.dom
        for a in tag.select("a[href]"):
            if a.text == link_text:
                return self.navigate(a.attrs['href'])
        raise StopLocust("Link not found (" + link + ")")


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
            group = Group()
            for url, response in resources.images.items():
                if not response:
                    group.spawn(self.download_item, resources.images, url)
            for url, response in self.scripts.items():
                if not response:
                    group.spawn(self.download_item, resources.scripts, url)
            for url, response in self.links.items():
                if not response:
                    group.spawn(self.download_item, resources.links, url)
            group.join()

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
