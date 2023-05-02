import requests
from requests import HTTPError
from top_container import TopContainer

class TopContainerFetcher:
    def __init__(self, config: dict, session_id):
        self.base_url = config['base_url']
        self.repository_id = config['repository_id']
        self.session_id = session_id

    def get_top_container(self, top_container_id):
        header = {"X-ArchivesSpace-Session": self.session_id}
        response = requests.get(f"{self.base_url}/repositories/{self.repository_id}/top_containers/{top_container_id}", headers=header)
        response.raise_for_status()
        top_container_json = response.json()
        # import ipdb; ipdb.set_trace()
        top_container = TopContainer(top_container_json)
        return top_container
