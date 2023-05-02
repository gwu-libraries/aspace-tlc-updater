import requests
from requests import HTTPError
from user_authenticator import UserAuthenticator
from top_container_fetcher import TopContainerFetcher
from top_container_updater import TopContainerUpdater
from config import config

user_authenticator = UserAuthenticator(config)

session_id = user_authenticator.authenticate()

top_container_updater = TopContainerUpdater(config, session_id)

x = top_container_updater.update_top_container(top_container_id=510, new_barcode="TEST-10:24")

# import ipdb; ipdb.set_trace()
