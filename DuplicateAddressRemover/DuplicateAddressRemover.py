import requests
import traceback
from configparser import ConfigParser

class DuplicateAddressRemover(object):

    def __init__(self,config):

        self._cookie = config['DATA']['Cookie']
        self._url = config['DATA']['Url']
        self._formkey = config['DATA']['FormKey']
        try:
            self._addIds = config['DATA']['AddressIds'].split(',')
        except:
            print("Incorrect Address ID config") # Wanted to raise specifically

    def requestRemovals(self):

        print("Removing Addresses")

        ids = self._addIds.copy()
        headers = { 'Cookie':self._cookie ,  'Host': "tr.buynespresso.com", 'Referer': "https://tr.buynespresso.com/tr_en/customer/address/index/" }


        for id in ids:
            curUrl =   self._url.format(id, self._formkey)

            try:
                r = requests.get(url=curUrl, headers=headers)
                assert r.status_code == 200
            except AssertionError:
                raise Exception("Request response not OK!")


if __name__ == "__main__":

    try:

        # Initialize objects
        config = ConfigParser()
        config.read("config.cfg") # Config file contains session and address id information which is essential for requests

        addremover  = DuplicateAddressRemover(config)
        addremover.requestRemovals()
        print("Fin, program terminated")
    except:
        traceback.print_exc()