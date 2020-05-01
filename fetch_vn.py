import requests
import uuid

def fetch(url):
    r = requests.get(url, allow_redirects=True)
    filename = "/tmp/{}".format(uuid.uuid1())
    open(filename, 'wb').write(r.content)
    return filename