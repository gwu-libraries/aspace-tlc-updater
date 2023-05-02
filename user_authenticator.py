import requests
from requests import HTTPError

class UserAuthenticator:

  def __init__(self, config: dict):
    self.base_url = config['base_url']
    self.user = config['username']
    self.password = config['password']


  def authenticate(self):
    response = requests.post(f"{self.base_url}/users/{self.user}/login",
                      params={'password': self.password})
    response.raise_for_status()
    session_id = response.json()["session"]
    return session_id