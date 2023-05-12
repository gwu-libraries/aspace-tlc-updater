import requests
from requests import HTTPError
from top_container_tools.top_container import TopContainer
from exceptions.duplicate_barcode_exception import DuplicateBarcodeException
from exceptions.missing_tlc_exception import MissingTLCException

class TopContainerFetcher:
    def __init__(self, config: dict, session_id):
        self.base_url = config['base_url']
        self.repository_id = config['repository_id']
        self.session_id = session_id

    def get_top_container(self, top_container_id):
        header = {"X-ArchivesSpace-Session": self.session_id}
        response = requests.get(f"{self.base_url}/repositories/{self.repository_id}/top_containers/{top_container_id}", headers=header, timeout=None)
        response_json = response.json()
        if 'error' in response_json:
            if response_json['error'] == 'TopContainer not found':
                raise MissingTLCException
        top_container_json = response.json()
        top_container = TopContainer(top_container_json)
        return top_container