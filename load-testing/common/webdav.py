from typing import Iterator

from bs4 import BeautifulSoup, Tag
from locust.clients import HttpSession
from locust.exception import LocustError


class PropfindResponse:
    def __init__(self, item: Tag):
        self.href = item.select_one(r'd\:href').text

        item_prop = item.select_one(r'd\:propstat > d\:prop')
        self.fileid = item_prop.find("oc:fileid").text if item_prop.find("oc:fileid") else False
        self.hasPreview = item_prop.find("nc:has-preview").text == "true" if item_prop.find("nc:has-preview") else False
        self.etag = item_prop.find("d:getetag").text if item_prop.find("d:getetag") else None
        self.contentType = item_prop.find("d:getcontenttype").text if item_prop.find("d:getcontenttype") else None
        self.collection = bool(item_prop.select_one(r"d\:resourcetype > d\:collection"))


class Webdav:
    def __init__(self, client: HttpSession, requesttoken: str):
        self.client = client
        self.requesttoken = requesttoken

    def propfind(self, url, deep=False) -> Iterator[PropfindResponse]:
        query = """<?xml version="1.0"?>
<d:propfind xmlns:d="DAV:" xmlns:oc="http://owncloud.org/ns" xmlns:nc="http://nextcloud.org/ns" xmlns:ocs="http://open-collaboration-services.org/ns">
  <d:prop>
    <d:getlastmodified />
    <d:getetag />
    <d:getcontenttype />
    <d:resourcetype />
    <oc:fileid />
    <oc:permissions />
    <oc:size />
    <d:getcontentlength />
    <nc:has-preview />
    <nc:mount-type />
    <nc:is-encrypted />
    <ocs:share-permissions />
    <oc:tags />
    <oc:favorite />
    <oc:comments-unread />
    <oc:owner-id />
    <oc:owner-display-name />
    <oc:share-types />
  </d:prop>
</d:propfind>"""
        r = self.client.request('PROPFIND', url, data=query, headers={"Content-Type": "application/xml; charset=UTF8",
                                                                      "requesttoken": self.requesttoken})

        if r.status_code == 207:
            response_items = BeautifulSoup(r.text, 'html.parser').findAll('d:response')
            for response_item in response_items:
                response = PropfindResponse(response_item)
                yield response
                if deep and response.collection:
                    yield from self.propfind(response.href)
        else:
            raise LocustError("Invalid status code: " + r.status_code)

    def put(self, url, data: bytes):
        r = self.client.put(url, data,
                        headers={"Content-Type": "application/octet-stream", "requesttoken": self.requesttoken})
        if r.status_code != 201:
            raise LocustError("Can't PUT file")
