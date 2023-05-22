import pandas
import logging
import sys
from alive_progress import alive_bar
import user_tools.user as user
from user_tools.user_authenticator import UserAuthenticator
from top_container_tools.top_container_updater import TopContainerUpdater
from exceptions.duplicate_barcode_exception import DuplicateBarcodeException
from exceptions.missing_tlc_exception import MissingTLCException
from exceptions.failed_authentication_exception import FailedAuthException
from config.config import config

logging.basicConfig(
    format='%(levelname)s:%(asctime)s:%(message)s',
    filename="logs/output.log",
    level=logging.INFO
)

matches_csv = pandas.read_csv(config['update_csv'])

user_authenticator = UserAuthenticator(config)

try:
    user = user_authenticator.authenticate()
    session_id = user.session
except FailedAuthException:
    logging.exception("Authentication failed, check config.py values.")
    sys.exit(1)

top_container_updater = TopContainerUpdater(config, session_id)

row_count = matches_csv.shape[0]

missing_tlc_count = 0
duplicate_barcode_count = 0
successful_update_count = 0

with alive_bar(row_count) as bar:
    for index,row in matches_csv.iterrows():
        top_container = str(row["top_container"])
        barcode = str(row["barcode"])
        
        try:
            top_container_updater.update_top_container(
                top_container_id=top_container, 
                new_barcode=barcode
                )
        except MissingTLCException:
            logging.warning("TLC not found for Top Container ID %s", top_container)
            with open("logs/missing_tlc_errors.txt", "a") as file:
                file.write(f"Top Container: {top_container}")
                file.write("\n")
            missing_tlc_count += 1
        except DuplicateBarcodeException:
            logging.warning("Duplicate Barcode error for TLC ID %s and barcode %s", top_container, barcode)
            with open("logs/duplicate_barcode_errors.txt", "a") as file:
                file.write(f"Top Container: {top_container}, Barcode: {barcode}")
                file.write("\n")
            duplicate_barcode_count += 1
        else:
            logging.info("Updated Top Level Container %s with Barcode %s", top_container, barcode)
            successful_update_count += 1
        bar()

print(f"""
Process completed
{successful_update_count} successful updates 
{duplicate_barcode_count} duplicate barcode errors 
{missing_tlc_count} missing TLC errors
""")