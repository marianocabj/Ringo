import sys
import requests
import json
# from ServiceDiscoverer import ServiceDiscoverer

URL = "http://localhost:8000/doorbell/api/"
PICTURE_URL = URL + "pictures/"
RECT_URL = URL + "rects/"


class FaceSender:
    def __init__(self):
        self.session = requests.Session()

    # def get_service_info(self, name):
        # sd = ServiceDiscoverer(name, "_http._tcp")
        # sd.discover(error_handler=self.on_error)

        # url = 'http://%s:%s%s' % (sd.service_info['address'],
        #                           sd.service_info['port'],
        #                           sd.service_info['txt']['doorbell_api'])

        # self.picture_endpoint = url + 'pictures/'
        # self.rect_endpoint = url + 'rects/'

    def set_auth(self, user, password):
        self.session.auth = (user, password)

    def post_picture(self, image, fmt):
        files = {'picture': ('jondoe.%s' % fmt, image, 'image/%s' % fmt)}
        response = self.session.post(PICTURE_URL, files=files)

        response.raise_for_status()

        j = response.json()
        return j['url']

    def post_rect(self, rects):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(RECT_URL,
                                     data=json.dumps(rects),
                                     headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            with open("debug.html", "w") as f:
                f.write(e.response.text)

    def close(self):
        self.session.close()

    @staticmethod
    def on_error(args):
        print("Error: %s" % args)
        sys.exit(1)
