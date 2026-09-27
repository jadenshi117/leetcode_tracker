import json
import os
from datetime import date
from collections import Counter

dataFile =  "problems.json"

def loadProblems():
    if not os.path.exists(dataFile):
        return []
    with open(dataFile, "r") as f:
        return json.load(f)

def saveProblems(problems):
    with open(dataFile, "w") as f:
        json.dump(problems, f, indent = 2)