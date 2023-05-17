import requests
from top_container_tools.top_container_fetcher import TopContainerFetcher
from exceptions.duplicate_barcode_exception import DuplicateBarcodeException
from exceptions.missing_tlc_exception import MissingTLCException

class TopContainerUpdater:
    def __init__(self, config, session_id):
        self.base_url = config['base_url']
        self.repository_id = config['repository_id']
        self.session_id = session_id
        self.top_container_fetcher = TopContainerFetcher(config, session_id)

    def update_top_container(self, top_container_id, new_barcode):
        top_container = self.top_container_fetcher.get_top_container(top_container_id)

        top_container_update_json = top_container.serialize(new_barcode=new_barcode)
        header = {"X-ArchivesSpace-Session": self.session_id}
        response = requests.post(f"{self.base_url}/repositories/{self.repository_id}/top_containers/{top_container_id}",
                    headers = header,
                    json = top_container_update_json,
                    timeout = None)
        response_json = response.json()
        if 'error' in response_json:
            # import ipdb; ipdb.set_trace()
            # if response_json['error']['barcode'][0] == 'A barcode must be unique within a repository':
            raise DuplicateBarcodeException