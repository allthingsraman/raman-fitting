import pathlib

# from .logging_config import get_console_handler
import logging
from .. import __package_name__

logger = logging.getLogger('pyramdeconv')

# import pandas as pd
# pd.options.display.max_rows = 10
# pd.options.display.max_columns = 10

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL_DIR = PACKAGE_ROOT / "deconvolution_models"

TESTS_ROOT_DIR = PACKAGE_ROOT.parent.parent / "tests"
TESTS_DATASET_DIR = TESTS_ROOT_DIR / "test_data"
TESTS_RESULTS_DIR = TESTS_ROOT_DIR / "test_results"

# Home dir from pathlib.Path for storing the results
PACKAGE_HOME = pathlib.Path.home() / ".pyramdeconv" # pyramdeconv is the new version package name

DATASET_DIR = PACKAGE_HOME / "datafiles"
RESULTS_DIR =  PACKAGE_HOME/ "results"
# Storage file of the index
INDEX_FILE = RESULTS_DIR / f"{__package_name__}_index.csv"
# Optional local configuration file
LOCAL_CONFIG_FILE = PACKAGE_HOME / "local_config.py"


# ADAPT to your own configurations
if LOCAL_CONFIG_FILE.is_file():
    try:
        from .local_config import DATASET_DIR, RESULTS_DIR, INDEX_FILE  # PACKAGE_ROOT, MODEL_DIR are not locally configurated
        print(f' Importing settings from local config...','\n',f'RESULTS_DIR : {RESULTS_DIR}','\n',f'From file: {__name__}')

    except Exception as e:
        print(f'Failed importing settings from local config...{RESULTS_DIR} because {e}')

# import configparser
# config = configparser.ConfigParser()
# config['DEFAULT'] = {'A': 1}
