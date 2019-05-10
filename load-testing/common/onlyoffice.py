import json
import time
from collections.abc import Iterable
from typing import Optional, Union

import websocket
from locust.events import request_success, request_failure


class CloseHandlerException(Exception):
    pass


class OnlyofficeException(Exception):
    pass


class HeaderAssertionError(AssertionError):
    def __init__(self, actual, expected, recv, *args, **kwargs):  # real signature unknown
        super().__init__(f"recv header {actual} doesn't match expected header {expected}. recv: {recv}")
        self.actual = actual
        self.expected = expected
        self.recv = recv


class MessageTypeAssertionError(AssertionError):
    def __init__(self, actual, expected, payload, *args, **kwargs):  # real signature unknown
        super().__init__(
            f"payload message type {actual} doesn't match expected message type {expected}. payload: {payload}")
        self.actual = actual
        self.expected = expected
        self.payload = payload


class OnlyofficeState:
    def __init__(self):
        self.auth = {}
        self.heartbeats = []
        self.document_open_data = None
        self.messages = []


class OnlyofficeHandler:
    def __init__(self):
        self.config = {}
        self.state = OnlyofficeState()
        self.ws = None  # type: websocket.WebSocket
        self.url = None  # type: str

    def run(self, config, url):
        try:
            self.config = config
            self.state = OnlyofficeState()
            self.url = url
            self.ws = websocket.create_connection(url)
            while not self.state.document_open_data:
                self.recv_and_handle()
            self.scenario()
        except CloseHandlerException:
            pass
        finally:
            self.ws.close()
            self.ws = None
            self.url = None

    def scenario(self):
        self.send_message({'type': 'getMessages'}, 'message')

    def _handle_recv(self, recv, expected_header=None, expected_message_type=None):
        header = recv[:1]
        content = recv[1:]
        payload = json.loads(content) if content else None

        handled = []
        if expected_header and \
           expected_header != header and \
           header not in expected_header if isinstance(expected_header, Iterable) else False:
            raise HeaderAssertionError(header, expected_header, recv)

        if header == 'o':
            self._handle_open(content)
        elif header == 'h':
            self._handle_heartbeat(content)
        elif header == 'a':
            for payload_item in payload:
                handled.append(self._handle_message(payload_item, expected_message_type))
        elif header == 'm':
            handled.append(self._handle_message(payload, expected_message_type))
        elif header == 'c':
            self._handle_close(payload)
        else:
            raise NotImplementedError(f"Message header {header} is not implemented.")

        return (header, *handled)

    def _handle_message(self, payload, expected_message_type=None):
        message = json.loads(payload)
        message_type = message['type']

        if expected_message_type and \
           expected_message_type != message_type and \
           message_type not in expected_message_type if isinstance(expected_message_type, Iterable) else False:
            raise MessageTypeAssertionError(message_type, expected_message_type, payload)

        if hasattr(self, message_type):
            ret = getattr(self, message_type)(message)
            return message_type, message, ret
        else:
            raise NotImplementedError(f"Message type {message_type} is not implemented.")

    def _handle_heartbeat(self, message):
        self.state.heartbeats.append(message)

    def _handle_open(self, message):
        self.opened = True

    def _handle_close(self, message):
        self.__init__()
        raise CloseHandlerException()

    def recv_and_handle(self, wait_response: Optional[Union[bool, str, Iterable]] = False):
        start_time = time.time()
        recv = None
        request_type = "WebSocket"
        name = "OnlyOffice"
        name_additions = "?"
        try:
            recv = self.ws.recv()
            handled = self._handle_recv(
                recv,
                expected_header=('a', 'm') if not isinstance(wait_response, bool) else None,
                expected_message_type=wait_response if not isinstance(wait_response, bool) else None)

            if handled:
                name_additions = handled[0]
            if len(handled) <= 1:
                request_success.fire(
                    request_type=request_type,
                    name=f"{name} ({name_additions})",
                    response_time=int((time.time() - start_time) * 1000),
                    response_length=len(recv)
                )
            else:
                i = 1
                while i < len(handled):
                    message_type, _, _ = handled[i]
                    name_additions += f" ({message_type})"

                    request_success.fire(
                        request_type=request_type,
                        name=f"{name} ({name_additions})",
                        response_time=int((time.time() - start_time) * 1000),
                        response_length=len(recv)
                    )
                    i += 1
            return handled
        except HeaderAssertionError as e:
            if e.actual == 'h':
                request_success.fire(
                    request_type=request_type,
                    name=f"{name} ({name_additions})",
                    response_time=int((time.time() - start_time) * 1000),
                    response_length=len(recv) if recv else None
                )
                return self.recv_and_handle(wait_response)
            else:
                request_failure.fire(
                    request_type=request_type,
                    name=f"{name} ({name_additions})",
                    response_time=int((time.time() - start_time) * 1000),
                    exception=e
                )
                raise

    def send_message(self, message,
                     wait_response: Optional[Union[bool, str, Iterable]] = None):
        self.ws.send(json.dumps([json.dumps(message)]))
        if wait_response:
            return self.recv_and_handle(wait_response)

    def authChanges(self, data):
        pass

    def auth(self, message):
        if message.get('result') != 1:
            raise OnlyofficeException(f"Invalid auth response: {message}")
        print(message)
        self.state.auth = message

    def license(self, message):
        document = self.config.get('document')
        editor_config = self.config.get('editorConfig')
        user = editor_config.get('user')

        self.send_message({"type": "auth",
                           "docid": document.get('key'),
                           "documentCallbackUrl": editor_config.get('callbackUrl'),
                           "token": "fghhfgsjdgfjs",
                           "user": {"id": user.get('id'), "username": user.get('name'),
                                    "firstname": None, "lastname": None, "indexUser": -1},
                           "editorType": 0,
                           "lastOtherSaveTime": -1,
                           "block": [],
                           "sessionId": None,
                           "sessionTimeConnect": None,
                           "sessionTimeIdle": 0,
                           "documentFormatSave": 65,
                           "view": False,
                           "isCloseCoAuthoring": False,
                           "openCmd": {"c": "open",
                                       "id": document.get('key'),
                                       "userid": user.get('id'),
                                       "format": document.get('fileType'),
                                       "url": document.get('url'),
                                       "title": document.get('title'),
                                       "nobase64": True},
                           "lang": None,
                           "mode": None,
                           "permissions": {}})

    def documentOpen(self, message):
        if 'data' not in message or 'status' not in message['data'] or message['data']['status'] != 'ok':
            raise OnlyofficeException(f"Invalid documentOpen response: {message}")
        self.state.document_open_data = message['data']

    def message(self, message):
        pass

    def saveLock(self, message):
        return message.get('saveLock')

    def unSaveLock(self, message):
        pass
