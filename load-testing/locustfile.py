from locust import HttpLocust

from nextcloud import NextcloudTaskSet
from onlyoffice import OnlyofficeTaskSet


class DefaultLocust(HttpLocust):
    task_set = {OnlyofficeTaskSet: 10, NextcloudTaskSet: 1}
    host = 'https://nextcloud.pce-cloud-2.asogfi.fr'

    min_wait = 5000
    max_wait = 10000


if __name__ == '__main__':
    DefaultLocust().run()
