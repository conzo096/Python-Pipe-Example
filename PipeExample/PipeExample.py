import subprocess as sp
from subprocess import Popen 
import os
import sys
import getopt
 
# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"p:")
 
exampleArg=''
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-p':
        exampleArg = a
    else:
        print("Usage: %s -p exampleArg" % sys.argv[0])
 
# Display input and output file name passed as the args
print ("exampleArg: %s" % (exampleArg) )
exe = "../Debug/ApplicationToPipeFrom.exe"
runningApp = Popen(exe,stdout = sp.PIPE, universal_newlines = True)
capturedArguments = runningApp.communicate()[0]
print("Command line from app 1: " + capturedArguments)

print("App 2:")
exe = "../Debug/ApplicationToPipeToo.exe"
runningApp = Popen([exe, capturedArguments, "-p " + exampleArg])