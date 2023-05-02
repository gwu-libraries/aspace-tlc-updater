import requests
from requests import HTTPError
from top_container_fetcher import TopContainerFetcher
from top_container import TopContainer

class TopContainerUpdater:
    def __init__(self, config, session_id):
        self.base_url = config['base_url']
        self.repository_id = config['repository_id']
        self.session_id = session_id
        self.top_container_fetcher = TopContainerFetcher(config, session_id)

    def update_top_container(self, top_container_id: int, new_barcode):
      top_container = self.top_container_fetcher.get_top_container(top_container_id)
      top_container_update_json = top_container.serialize(new_barcode=new_barcode)

      header = {"X-ArchivesSpace-Session": self.session_id}
      response = requests.post(f"{self.base_url}/repositories/{self.repository_id}/top_containers/{top_container_id}",
                    headers = header,
                    json=top_container_update_json)
      response.raise_for_status()
      # do the post request here
      # import ipdb; ipdb.set_trace()
      # return top_container