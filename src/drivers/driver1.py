#!/usr/bin/env python

'''
*********************
*  Example driver  **
*********************
'''

# **************************************** #

#############
#  IMPORTS  #
#############
# standard python packages
import os, sys

# ------------------------------------------------------ #
# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../.." )
sys.path.append( packagePath )

from dedc import dedc, dedalusParser
from utils import parseCommandLineInput
from utils.Table import Table
# ------------------------------------------------------ #

# **************************************** #

################
#  PARSE ARGS  #
################
# parse arguments from the command line
def parseArgs( argList ) :
  argDict = {}   # empty dict

  argDict = parseCommandLineInput.parseCommandLineInput( argList )  # get dictionary of arguments.

  return argDict

##########################
#  RUN DATALOG COMPILER  #
##########################
# parse dedalus programs
def runDatalogCompiler( filename ) :
  return dedc.runCompiler( filename )

####################
#  PASS TO SOLVER  #
####################
# pass dedalus programs and arguments to solver
def passToSolver() :
  print " ... In passToSolver ..."
  #

####################
#  OUTPUT RESULTS  #
####################
# output results =]
def outputResults() :
  print " ... In outputResults ..."
  #

############
#  DRIVER  #
############
def driver() :
  # get list of command line args, except prog name
  argList = sys.argv[1:]

  # print help if no args provided
  if( len(argList) < 1 ) :
    thisFilename = os.path.basename(__file__)     # name of this file
    print "No arguments provided. Please run 'python " + sys.argv[0] + " -h' for assistance."
    sys.exit()

  # pass list to parse args, get dict of args
  argDict = parseArgs( argList )
  print argDict

  # parse ded files into tabular intermediate representation
  fullFactTable = Table( "FACT" )
  fullRuleTable = Table( "RULE" )

  
  for key in argDict :
    if "file" in key : # key to a ded file
      dedfilename = argDict[ key ]
      tables = runDatalogCompiler( dedfilename )
      #factTable = tables[ "factTable" ] # fact table derived from this file
      #ruleTable = tables[ "ruleTable" ] # rule table derived from this file
      #fullFactTable.mergeTable( factTable ) # save to collective fact table
      #fullRuleTable.mergeTable( ruleTable ) # save to collective rule table
    else : # this is not the ded file you're looking for. move along.
      continue # do nothing

  # convert into datalog
  # run through pydatalog, collect bindings ~ provenance
  # if buggy => output results
  # else => ...

  print "PASSED" # needed for simpleLog in tests/
                 # TODO: create more robust testing framework

#########################
#  THREAD OF EXECUTION  #
#########################
driver()

#########
#  EOF  #
#########
