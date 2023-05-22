This repository contains code for batch updating Top Level Containers in [ArchiveSpace](https://archivesspace.org/) with new barcodes.

**Instructions for use:**
- Clone the repository to your local machine. 
- In the main directory of the repository on your machine, create or paste in a CSV file containing a column titled `barcode` and a column titled `top_container`. See [update_csv.csv.example](update_csv.csv.example) for an example. The file may contain additional columns, but only requires these two specifically named columns to function. 
- Requires Python packages listed in [requirements.txt](requirements.txt) file (alive-progress, pandas, requests).
- Copy the [config/config.py.example](config/config.py.example) file and complete with the base url for your ArchivesSpace instance API endpoint, username, password, repository ID, and the name of the CSV containing top level container and barcode IDs.
- In a terminal window, navigate to the main directory of the repository, and run `python main.py`.
- If successful, terminal window will show a progress bar keeping track of the updates, and more information can be seen by following the output of [logs/output.log](logs/output.log). 