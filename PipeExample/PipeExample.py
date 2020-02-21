import subprocess as sp
from subprocess import Popen 
import os

exe = "../Debug/ApplicationToPipeFrom.exe"
runningApp = Popen(exe,stdout = sp.PIPE, universal_newlines = True)
capturedArguments = runningApp.communicate()[0]
print("Command line from app 1: " + capturedArguments)

print("App 2:")
exe = "../Debug/ApplicationToPipeToo.exe"
runningApp = Popen(exe + " " + capturedArguments)