#!/usr/bin/env python

import os, sys

#######################
#  CHECK PARENTHESES  #
#######################
def checkParentheses( line ) :
  numOpen   = 0 # number of open parentheses "("
  numClosed = 0 # number of closed parentheses ")"

  for c in line :
    if c == "(" :
      numOpen += 1
    elif c == ")" :
      numClosed += 1

  if not numOpen == numClosed :
    sys.exit( "ERROR: Incorrect number of parentheses in line: " + line )

  return True

#########
#  EOF  #
######### 
