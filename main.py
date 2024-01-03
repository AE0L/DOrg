import os
import shutil
from pathlib import Path
from util_logging import setup_custom_logger
from util_config import initialize_config

LOGGER = setup_custom_logger('dorg')
config = initialize_config(LOGGER)
files = os.listdir()

# counters
excluded = 0
unknown = 0
grouped = 0
ungrouped = 0
dirs = 0

# constants
F_SORTED = 'sorted'
F_UNGROUPED = 'sorted/ungrouped'
F_DIRECTORIES = 'directories'
F_UNKNOWN = 'unknown'

LOGGER.info('processing ' + str(len(files)) + ' file/s...')
LOGGER.info('creating "sorted" folder...')

def is_excluded(file = '', ext = ''):
    if file in config['exclusions']['files']: return True
    elif file in config['exclusions']['folders']: return True
    elif ext in config['exclusions']['extensions']: return True
    else: return False

for file in files:
    ext = os.path.splitext(file)[1][1:]

    if is_excluded(file, ext):
        LOGGER.info('skipped ' + file + ' (Excluded)')

        excluded += 1

        continue
    elif os.path.isdir(file):
        LOGGER.info('moving ' + file + '/ into "' + F_DIRECTORIES + '" folder...')

        Path(F_DIRECTORIES).mkdir(parents=True, exist_ok=True)
        shutil.move(file, F_DIRECTORIES + '/' + file)

        dirs += 1
    elif ext == '':
        LOGGER.info('unkown extension: ' + file)
        LOGGER.info('moving file in "' + F_UNKNOWN + '" folder...')

        Path(F_UNKNOWN).mkdir(parents=True, exist_ok=True)
        shutil.move(file, F_UNKNOWN + '/' + file)

        unknown += 1
    else:
        if ext in config['groups']:
            folder = F_SORTED + '/' + config['groups'][ext]

            LOGGER.info('extension found in a group: ' + file)
            LOGGER.info('moving file in "' + folder + '" folder...')

            grouped += 1
        else:
            folder = F_UNGROUPED + '/' + ext

            LOGGER.info('extension not found in a group: ' + file)
            LOGGER.info('moving file in "' + folder + '" folder...')

            ungrouped += 1

        Path(folder).mkdir(parents=True, exist_ok=True)
        shutil.move(file, folder + '/' + file)

LOGGER.info('organizing files completed')
LOGGER.info('Organized files:')
LOGGER.info('    ' + str(grouped) + ' grouped file/s')
LOGGER.info('    ' + str(ungrouped) + ' ungrouped file/s')
LOGGER.info('    ' + str(dirs) + ' directories')
LOGGER.info('    ' + str(unknown) + ' unknown file/s')
LOGGER.info('    ' + str(excluded) + ' excluded file/s')
