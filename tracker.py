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

def addProblem(name, pattern, difficulty):
    problems = loadProblems()
    newProblem = {
        "name": name,
        "pattern": pattern,
        "difficulty": difficulty,
        "dateSolved": str(date.today())
    }
    problems.append(newProblem)
    saveProblems(problems)
    print(f"Added: {name}")

def patternCounts():
    problems = loadProblems()
    patterns = [p["pattern"] for p in problems]
    return Counter(patterns)

def leastPracticedPattern(allKnownPatterns):
    counts = patternCounts()
    for pattern in allKnownPatterns:
        if pattern not in counts:
            counts[pattern] = 0
    return counts.most_common()[::-1]