import urllib.request
from Dataset import Dataset

class Dataset(object):
    """ This implementation send the reasons and messages to the PagerDuty system. """
    def search(self, message):
        """ Open an incident on the PD """
        raise NotImplementedError("TODO: PD integration under development")

    def query_external_api(self, email):
        req = urllib.request.Request(
            "https://api.pwnedpasswords.com/pwnedpassword/"+email, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        f = urllib.request.urlopen(req)
        print(f.read().decode('utf-8'))
        return (f.read().decode('utf-8'))