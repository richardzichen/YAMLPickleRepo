import PickleLibrary
from Utilities import *

from Algorithms import MCSA
from Algorithms import FCH
from Algorithms import SSAP

msgLogger(0, f'KnDist_Assignments:')
msgLogger(1, f'Opening testing shelve:')

# loading settings
settings = loadSettings('settings.yaml')

# opening PickleShelve
path = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
shelfName = 'TestPickleShelve'
msgLogger(2, f'Opened test shelve [{path}/{shelfName}].')
pkShelve = PickleLibrary.PickleShelve(path, shelfName)

# unloading variables we need to generate taxi data
numSimulations = settings['numSimulations']
resources = settings['resources']

results = dict()
testDataDict = dict()

# getting latest test dictionary
msgLogger(1, f'Retrieving testing data:')

pkShelve.pickleDict['results'] = results
pkShelve.pickleDict['testDataDict'] = testDataDict

testKey = testDataDict[KEYS][-1]
results['testKey'] = testKey
msgLogger(2, f'Using test data keyed with [{testKey}].')

# getting the corresponding test dictionary
testDict = testDataDict[TEST_DATA][testKey]

# unpacking test dictionary metrics
taskDict = testDict['data']
numTestSets = testDict['numTestSets']
numTests = testDict['numTests']
numDPs = testDict['numDPs']
taskDists = testDict['distributions']

results[RESOURCES] = resources

# creating fch object with specified task distributions
msgLogger(1, f'Creating algorithm objects:')
MCSAObj = MCSA.MCSA(resources, taskDists, numDPs, numSimulations)
FCHObj = FCH.FCH(resources, taskDists, numDPs)
VecSSAPObj = SSAP.VectorSSAP(resources, taskDists, numDPs)

# creating the algorithm dictionary and storing it in the results dictionary
algDict = dict()
algDict['mcsa'] = MCSAObj
algDict['fch'] = FCHObj
algDict['vec_ssap'] = VecSSAPObj
results[ALGORITHMS] = algDict

# creating the assignment dictionary and storing it in the results dictionary
assignmentDict = dict()

results[ASSIGNMENTS] = assignmentDict

msgLogger(2, f'Storing data in [{path}/{shelfName}]')
