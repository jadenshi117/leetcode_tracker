import json
import os
from datetime import date
from collections import Counter

dataFile =  "problems.json"

#checks if file dataFile (in this case file "problems.json") exists,
#if it does then it reads it and returns the contents as a python object
def loadProblems():
    if not os.path.exists(dataFile):
        return []
    with open(dataFile, "r") as f:
        return json.load(f)

#opens a json file to write in the problems, effectively saving them in the file
def saveProblems(problems):
    # w is write, r is read, with is used to open the file,
    # do whatever it needs to do, and then it closes the file, saving you the effort of closing it yourself
    with open(dataFile, "w") as f:
        #json.dump(python data you want to save, writing location, spacing)
        json.dump(problems, f, indent = 2)

#takes in name, pattern, difficulty and date of the problem and
#uses saveProblem() to write it into the json file
def addProblem(name, pattern, difficulty):
    problems = loadProblems()
    newId = max([p["id"] for p in problems], default = 0) + 1
    newProblem = {
        "id": newId,
        "name": name,
        "pattern": pattern,
        "difficulty": difficulty,
        "dateSolved": str(date.today())
    }
    problems.append(newProblem)
    saveProblems(problems)
    print("Added:", name)

def deleteProblem(problemId):
    problems = loadProblems()
    #puts all of the problems without the specific id in a list and rewrites dataFile
    remaining = [p for p in problems if p["id"] != problemId]
    if len(remaining) == len(problems):
        return False
    saveProblems(remaining)
    return True

#uses Counter to find the number of each problem
def patternCounts():
    problems = loadProblems()
    #p["pattern"] looks for everything in problems under the key "pattern"
    patterns = [p["pattern"] for p in problems]
    return Counter(patterns)

#
def leastPracticedPattern(allKnownPatterns):
    counts = patternCounts()
    for pattern in allKnownPatterns:
        if pattern not in counts:
            counts[pattern] = 0
    return counts.most_common()[::-1]

knownPatterns = ["two_pointer", "sliding_window", "hash_map", "stack", "linked_list", "dynamic_programming"]

def main():
    while (True):
        print("\n1. Add problem\n2. Show stats\n3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Problem name: ")
            pattern = input(f"Pattern ({', '.join(knownPatterns)}): ")
            difficulty = input("Difficulty (easy/medium/hard): ")
            addProblem(name, pattern, difficulty)

        elif choice == "2":
            for pattern, count in leastPracticedPattern(knownPatterns):
                print(f"{pattern}: {count} solved")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()