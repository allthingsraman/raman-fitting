

import logging


from .. import __package_name__
logger = logging.getLogger(__package_name__)

from . import config


def get_directory_paths_for_run_mode(run_mode: str = ''):

        dest_dirs = {}
        DATASET_DIR = None
        RESULTS_DIR = None

        if run_mode in ('DEBUG', 'testing'):
            # self.debug = True
            RESULTS_DIR = config.TESTS_RESULTS_DIR
            DATASET_DIR = config.TESTS_DATASET_DIR

        elif run_mode == 'make_examples':
            RESULTS_DIR = config.PACKAGE_HOME.joinpath('example_results')
            DATASET_DIR = config.TESTS_DATASET_DIR
            # self._kwargs.update({'default_selection' : 'all'})

        elif run_mode in ('normal', 'make_index'):
            RESULTS_DIR = config.RESULTS_DIR
            DATASET_DIR = config.DATASET_DIR
            # INDEX_FILE = config.INDEX_FILE
        else:
            logger.warning(f'Run mode {run_mode} not recognized. Exiting...')

        if DATASET_DIR:
            if not DATASET_DIR.is_dir():
                logger.warning(f'The datafiles directory does not exist, index will be empty.\n"{DATASET_DIR}"\nExiting...')
                sys.exit()
            # raise FileNotFoundError(f'This directory does not exist:\n{DATASET_DIR}')
        else:
            logger.warning(f'No datafiles directory was set for{run_mode}. Exiting...')
        if not RESULTS_DIR.is_dir():
            RESULTS_DIR.mkdir(exist_ok=True,parents=True)
            logger.info(f'{self._cqnm} the results directory did not exist and was created at:\n"{RESULTS_DIR}"')

    # def get_index_file_path(self, dest_dir = Path()):
        ''' returns index file path '''
        if RESULTS_DIR.exists():
            INDEX_FILE = config.INDEX_FILE
            logger.info(f'get_directory_paths_for_run_mode the index file will be saved as:\n"{INDEX_FILE}"')
            # return INDEX_FILE
        else:
            logger.warning(f'get_directory_paths_for_run_mode the index file destination dir does not exists. Please choose an existing Results dir.\n"{dest_dir}"')
            INDEX_FILE = None

        dest_dirs = {'RESULTS_DIR': RESULTS_DIR, 'DATASET_DIR': DATASET_DIR, 'INDEX_FILE': INDEX_FILE}
        return dest_dirs