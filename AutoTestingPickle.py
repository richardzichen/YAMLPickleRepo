import PickleLibrary
import math
import subprocess
from scipy import stats as sps
from Utilities import *
import yaml
from yaml.loader import SafeLoader

# creating a list of programs to run in sequence
program_list = ['KnDists_GenerateData.py', 'KnDists_AssignResources.py', 'KnDists_ReviewAssignments.py']

# for loop for whatever setting we are changing here
mean = 100
sd = 40

a = mean - ((math.sqrt(12) / 2) * sd)
b = a + (2 * (mean - a))

distList = [[sps.norm(mean, sd), sps.norm(mean, sd), sps.norm(mean, sd), sps.norm(mean, sd), sps.norm(mean, sd)],
            [sps.uniform(a, b), sps.uniform(a, b), sps.uniform(a, b), sps.uniform(a, b), sps.uniform(a, b)]]

# opening PickleShelve
path = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
shelfName = 'TestPickleShelve'
msgLogger(2, f'Opened test shelve [{path}/{shelfName}].')
pkShelve = PickleLibrary.PickleShelve(path, shelfName)

fileName = 'settings.yaml'
filePath = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
for distSet in distList:
    # Open YAML file and load settings
    settingsFile = open(f'{filePath}/{fileName}', 'r')
    settingsDict = yaml.load(settingsFile, Loader=SafeLoader)
    settingsFile.close()

    # Get previous settings
    prevSettingsKey = settingsDict['KEYS'][-1]
    prevSettings = settingsDict['SETTINGS'][prevSettingsKey]

    # Copy the latest settings dictionary and alter a parameter for testing
    newSettings = prevSettings.copy()
    newSettings['distributions'] = distSet

    settingsFile = open(f'{filePath}/{fileName}', 'w')
    yaml.safe_dump(newSettings, settingsFile)
    settingsFile.close()

    # Call each of the programs in sequence to complete a full test
    for program in program_list:
        subprocess.call(['python', program])

print('Finished all test cases.')
