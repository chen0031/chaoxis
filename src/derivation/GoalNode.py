#!/usr/bin/env python

# **************************************** #

#############
#  IMPORTS  #
#############
# standard python packages
import os, sys

import DerivTree

# **************************************** #

DEBUG = True

class GoalNode( ) :

  #############
  #  ATTRIBS  #
  #############
  treeType    = "goal"
  name        = None  # name of relation identifier
  isNeg       = False # is goal negative? assume positive
  record      = []
  descendants = []
  bindings    = None

  #################
  #  CONSTRUCTOR  #
  #################
  def __init__( self, n, i, r ) :
    self.name     = n
    self.isNeg    = i
    self.record   = r

  ################
  #  PRINT TREE  #
  ################
  def printTree( self ) :
    print "********************************"
    print "           GOAL NODE"
    print "********************************"
    print "name   :" + str( self.name )
    print "isNeg  :" + str( self.isNeg )
    print "record :" + str( self.record )
    print "[ DESCENDANTS ]"
    for d in self.descendants :
      d.printDerivTree()

  ################
  #  PRINT NODE  #
  ################
  def printNode( self ) :
    return "GOAL NODE: \nname = " + str( self.name ) + " ; \nisNeg = " + str( self.isNeg ) + ";\nbindings = " + str(self.bindings)

  ##############
  #  GET NAME  #
  ##############
  def getName( self ) :
    return self.name

  ##############
  #  GET SIGN  #
  ##############
  def getSign( self ) :
    return self.isNeg

  ################
  #  GET RECORD  #
  ################
  def getRecord( self ) :
    return self.record

  #######################
  #  CLEAR DESCENDANTS  #
  #######################
  def clearDescendants( self ) :
    self.descendants = []

  #####################
  #  SET DESCENDANTS  #
  #####################
  def setDescendants( self, provRuleName, allRulesSubs, bindings, results, cursor ) :
    self.bindings = bindings

    if DEBUG :
      print ">>> ... setting descendants ... <<<"
      print "   allRulesSubs  = " + str( allRulesSubs )
      print "   bindings = " + str( bindings )
      print "   results  = " + str( results )

    #sys.exit( "BREAKPOINT: allRulesSubs = " + str( allRulesSubs )  )

    for subDict in allRulesSubs :
      if DEBUG :
        print "GOALNODE : " + provRuleName + " processing rule expression from " + str(subDict)
      newRuleNode = DerivTree.DerivTree( provRuleName, "rule", False, self.record, results, cursor, allRulesSubs, bindings )
      self.descendants.append( newRuleNode )

    if DEBUG :
      print "GOALNODE : " + provRuleName + " has " + str(len(self.descendants)) + " descendants."
      print ">>> ... done setting descendants ... <<<"


  #####################
  #  GET DESCENDANTS  #
  #####################
  def getDescendants( self ) :
    return self.descendants


#########
#  EOF  #
#########