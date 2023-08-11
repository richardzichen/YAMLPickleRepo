from yaml.loader import SafeLoader
import yaml
import numpy as np
from scipy import stats as sps

# opening YAML Settings file
def loadSettings(fileName='settings.yaml'):
    # load YAML file into settingsData dict
    filePath = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
    settingsFile = open(f'{filePath}/{fileName}', 'r')
    settingsData = yaml.load(settingsFile, Loader=SafeLoader)
    settingsFile.close()


def addSettings(key, value, fileName='settings.yaml'):
    # load YAML file into settings dict
    filePath = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
    settingsFile = open(f'{filePath}/{fileName}', 'r')
    settings = yaml.load(settingsFile, Loader=SafeLoader)
    settingsFile.close()

    settings[key] = value

    settingsFile = open(f'{filePath}/{fileName}', 'w')
    yaml.safe_dump(settings, settingsFile)
    settingsFile.close()


# function to print text with the specified number of tabs
def msgLogger(numTabs, str):
    print(('\t' * numTabs) + str)


# key variables for shelve dictionaries
TRIP = 'trip'
GEO = 'geo'
DIST = 'dist'

KEYS = 'keys'

DISTS = 'dists'
RAW = 'raw'
TEST_INFO = 'test_info'
COL_NAMES = 'col_names'
TEST_DATA = 'test_data'

SPLIT = 'split'
SPLIT_DATA = 'split_data'
TRAIN = 'train'
TEST = 'test'

RESULTS = 'results'
ALGORITHMS = 'algorithms'
ASSIGNMENT = 'assignment'
ASSIGNMENTS = 'assignments'
A_SCORE = 'a_scores'
O_SCORE = 'o_scores'
RESOURCES = 'resources'
TIME = 'time'

SETTINGS = 'settings'
SETTINGS_KEYS = 'settings_keys'
