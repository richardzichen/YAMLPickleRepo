import PickleLibrary
from Utilities import *
import numpy as np


def processData(assignmentDict, algsList, setCount, numTrials):
	reviewDict = dict()

def evaluateSet(assignmentDict, algsList, setCount, numTrials):
	reviewDict = processData(assignmentDict, algsList, setCount, numTrials)

# opening PickleShelve
path = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
shelfName = 'TestPickleShelve'
msgLogger(2, f'Opened test shelve [{path}/{shelfName}].')
pkShelve = PickleLibrary.PickleShelve(path, shelfName)

# getting most recent results
results = pkShelve.pickleDict['results']
resultKey = results[KEYS][-1]

assignmentDict = results[ASSIGNMENTS]

# getting corresponding test data key and test dictionary
testDataDict = pkShelve.pickleDict['testDataDict']
testKey = results['testKey']
testDict = testDataDict[TEST_DATA][testKey]