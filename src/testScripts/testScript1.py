# Rosie Aboody
# Joey Velez-Ginorio
# Julian Jara-Ettinger
# Curse of Knowledge Project
# -----------------------------------------------------------------------------


"""
	Overall Description:

	This script shows how to use the Curse of Knowledge source code to
	calculate the probability that a specific example would be taught
	in the blicket detector test.

	- Tips:
		There are quite a few parameters to check out, but a nice experiment is
		keeping everything constant and only changing the example - to see which
		examples are good/bad given a trueHypothesis.

"""


""" Imports """
# Allows us to import parent directory
import sys
sys.path.append("..")

# Import our inference machine, which handles all the inference
from InferenceMachine import InferenceMachine
from GenerateHypothesisSpace import GenerateHypothesisSpace


""" Input Specification """
# Specify the blocks we will be using
blockList = ['A','B','C','D']

# Initialize H, so that it may call multiple hypothesisSpaceGenerators
# e.g. H.unorderedOr() generates hypothesis space for unorederedOr
H = GenerateHypothesisSpace(blockList)
hypothesisSpace = H.unorderedOr()

# Determine amount of mistrust learner has in teacher. [0,1)
# low values = high trust, high values = low trust
lambda_noise = .1

# True Hypothesis
# Or(A,B) -> ['A','B']
trueHypothesis = ['A','B']

# Pick example
# e.g. 'AB' means both A and B are on blicket detector
example1 = 'AB'
example2 = 'A'
example3 = 'ABCD'


"""Calculations"""
# Initialize an instance of our InferenceMachine
infer = InferenceMachine()

# Print probability of teaching example given a hypothesisSpace and the trueHypothesis
print infer.probabilityOfExample(hypothesisSpace, trueHypothesis, example1)




