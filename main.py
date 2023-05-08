import pandas
from user_authenticator import UserAuthenticator
from top_container_updater import TopContainerUpdater
from exceptions.duplicate_barcode_exception import DuplicateBarcodeException
from exceptions.missing_tlc_exception import MissingTLCException
from config import config

user_authenticator = UserAuthenticator(config)

session_id = user_authenticator.authenticate()

top_container_updater = TopContainerUpdater(config, session_id)

matches_csv = pandas.read_csv(config['update_csv'])

for index,row in matches_csv.iterrows():
    top_container = str(row["top_container"])
    barcode = str(row["barcode"])
    
    try:
        top_container_updater.update_top_container(
            top_container_id=top_container, 
            new_barcode=barcode
            )
        print(f"Updated Top Level Container {top_container} with Barcode {barcode}")
    except MissingTLCException:
        print(f"TLC not found for ID {top_container}")
        with open("exception_logs/not_exist_error.txt", "a") as file:
            file.write("\n")
            file.write(top_container)
    except DuplicateBarcodeException:
        print(f"Duplicate Barcode Error for ID {top_container} and barcode {barcode}")
        with open("exception_logs/unique_barcode_errors.txt", "a") as file:
            file.write("\n")
            file.write(top_container)
