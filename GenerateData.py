import PickleLibrary
from Utilities import *
import numpy as np

# opening shelve and getting correct dists
# opening the testing shelve
msgLogger(0, f'KnDists_GenerateData:')
msgLogger(1, f'Opening testing shelve:')

# loading settings
settings = loadSettings('settings.yaml')

# opening PickleShelve
path = '/home/ase_intern/PycharmProjects/pickleTest/pickleProject'
shelfName = 'TestPickleShelve'
msgLogger(2, f'Opened test shelve [{path}/{shelfName}].')
pkShelve = PickleLibrary.PickleShelve(path, shelfName)

# unloading variables we need to generate taxi data
taskVecSize = settings['taskVecSize']
numTestSets = settings['numTestSets']
numTests = settings['numTests']
numDPs = settings['numDPs']

distributions = settings['distributions']

msgLogger(2, f'Retrieved settings from [{settings}].')

# Creating dictionary to store testing information
testDict = dict()

# storing basic testing information
testDict['taskVecSize'] = taskVecSize
testDict['numTestSets'] = numTestSets
testDict['numTests'] = numTests
testDict['numDPs'] = numDPs
testDict['distributions'] = distributions
testDict['data'] = dict()

msgLogger(1, f'Creating test data sets:')

# extracting the distribution dictionary and the distributions generated based on the
# complete data
testDict['dists'] = distributions

for dataSet in range(numTestSets):
    msgLogger(2, f'Dataset: {dataSet}.')
    for test in range(numTests):
        msgLogger(3, f'Test {test}.')
        # creating test task list and storing in shelve
        tasks = np.zeros((numDPs, taskVecSize), dtype=float)

        # populating test data with distribution values
        for i in range(taskVecSize):
            taskValues = distributions[i].rvs(size=numDPs)
            tasks[:, i] = taskValues

        # making sure we have no negative values in the task vectors
        negIndxs = np.argwhere(tasks < 0)
        tasks[negIndxs[:, 0], negIndxs[:, 1]] = 0

        # adding the test data to the dictionary
        testDict['data'][(dataSet, test)] = tasks

# adding testDict to pickleDict
pkShelve.pickleDict.testDataDict['testDataDict'] = testDict

