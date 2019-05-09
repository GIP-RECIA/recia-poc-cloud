import json
import random
import string

import pkg_resources
from locust import task, HttpLocust

from common.nextcloud import NextcloudBrowserTaskSet
from common.onlyoffice import OnlyofficeHandler
from common.webdav import Webdav


class OnlyofficeTaskSet(NextcloudBrowserTaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.browser.options.download = False

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    @task
    def load_file(self):
        webdav = Webdav(self.client, self.browser.requesttoken)

        letters = string.ascii_lowercase
        filename = ''.join(random.choice(letters) for i in range(12)) + '.docx'

        data = pkg_resources.resource_string(__name__, 'data/word.docx')

        r = webdav.put(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice/{filename}', data, catch_response=True)
        r.success()
        if r.status_code == 404:
            webdav.mkcol(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice')
            webdav.put(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice/{filename}', data)

        propfind = next(webdav.propfind(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice/{filename}'))

        r = self.browser.navigate(f"/apps/onlyoffice/{propfind.fileid}", params={"filePath": f"/Onlyoffice/{filename}"})
        script = r.dom.select_one('.app-onlyoffice script')
        host = script.attrs['src'].replace('/web-apps/apps/api/documents/api.js', '')

        r = self.client.get(f"/apps/onlyoffice/ajax/config/{propfind.fileid}",
                            params={"filePath": f"/Onlyoffice/{filename}"},
                            headers={'requesttoken': self.browser.requesttoken})

        config = json.loads(r.text)

        self.browser.navigate(
            f'{host}/web-apps/apps/documenteditor/main/index.html?lang=fr&customer=ONLYOFFICE&frameEditorId=iframeEditor')
        r = self.client.get(f"{host}/doc/{config['document']['key']}/c/info?t=1557393092054")
        info = json.loads(r.text)

        # Some info on the OnlyOffice WebSocket protocol were grabbed from 
        # https://github.com/ONLYOFFICE/testing-documentserver-capacity/blob/master/capacity.js
        server_id = random.randint(1, 1000)
        session_id = ''.join(random.choice(letters) for i in range(8))

        ws_host = host
        ws_host = ws_host.replace('https://', 'wss://')
        ws_host = ws_host.replace('http://', 'ws://')

        class Scenario(OnlyofficeHandler):
            def scenario(self):
                super().scenario()
                super().send_message({'type': 'isSaveLock'}, wait_response='saveLock')
                super().send_message(self.hello_world_message, wait_response='unSaveLock')

            @property
            def hello_world_message(self):
                return {'type': 'saveChanges',
                        'changes': json.dumps([
                            '78;AgAAADEA//8BAALeZvCfEAAALQEAAAUAAAAAAAAAAAAAAAIAAAAAAAAA9v///xwAAAA1AC4AMgAuADgALgAyADQALgBAAEAAUgBlAHYA',
                            '34;BgAAADEANgA4AAEAHAABAAAAAAAAAAEAAABIAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAAAQAAAAEAAABlAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAAAgAAAAEAAABsAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAAAwAAAAEAAABsAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAABAAAAAEAAABvAAAAAwAAAA==',
                            '78;AgAAADEA//8BAALeZvCfEAAAiwAAAAEAAAABAAAAAAAAAAIAAAAAAAAA9v///xwAAAA1AC4AMgAuADgALgAyADQALgBAAEAAUgBlAHYA',
                            '34;BgAAADEANgA4AAEAHAABAAAABQAAAAIAAAAAAAAAAwAAAA==',
                            '78;AgAAADEA//8BAALeZvCfEAAALQEAAAUAAAACAAAAAAAAAAIAAAAAAAAA9v///xwAAAA1AC4AMgAuADgALgAyADQALgBAAEAAUgBlAHYA',
                            '34;BgAAADEANgA4AAEAHAABAAAABgAAAAEAAABXAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAABwAAAAEAAABvAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAACAAAAAEAAAByAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAACQAAAAEAAABsAAAAAwAAAA==',
                            '34;BgAAADEANgA4AAEAHAABAAAACgAAAAEAAABkAAAAAwAAAA==']),
                        'startSaveChanges': True,
                        'endSaveChanges': True,
                        'isCoAuthoring': False,
                        'isExcel': False,
                        'deleteIndex': None,
                        'excelAdditionalInfo': json.dumps(
                            {"Rk": "F1700ivg2",
                             "V1d": "F1700ivg",
                             "yvd": "14;BgAAADEANgA4AAsAAAA="}
                        ),
                        'unlock': False,
                        'releaseLocks': False}

        Scenario().run(config, f"{ws_host}/doc/{propfind.fileid}/c/{server_id}/{session_id}/websocket")

        webdav.delete(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice/{filename}')
        webdav.delete(f'/remote.php/dav/files/{self.browser.user}/Onlyoffice')


class OnlyofficeLocust(HttpLocust):
    task_set = OnlyofficeTaskSet
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 5000
    max_wait = 10000


if __name__ == '__main__':
    OnlyofficeLocust().run()
