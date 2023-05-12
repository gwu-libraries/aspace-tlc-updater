import requests
from requests import HTTPError
import logging
from user_tools.user import User
from exceptions.failed_authentication_exception import FailedAuthException

class UserAuthenticator:

  def __init__(self, config: dict):
    self.base_url = config['base_url']
    self.user = config['username']
    self.password = config['password']

  def authenticate(self):
    try:
      response = requests.post(f"{self.base_url}/users/{self.user}/login",
                        params={'password': self.password},
                        timeout = None)
      user = User(response.json())
    except:
      print("Authentication failed - check config.py settings.")
      raise FailedAuthException
    else:
      logging.info(f"Authenticated as user {user.email} with session {user.session}")
      return user