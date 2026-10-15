from flask import Flask, request, jsonify
from flask_cors import CORS
from tracker import addProblem, deleteProblem, loadProblems, leastPracticedPattern, knownPatterns

app = Flask(__name__)
CORS(app)

#function declarations
#add later


#confirmation the code is running (testing purposes)
@app.route("/")
def home():
    return "LeetCode Tracker API is running"

#
@app.route("/problems", methods = ["GET"])
def getProblems():
    problems = loadProblems()
    return jsonify(problems)

#
@app.route("/problems", methods = ["POST"])
def createProblem():
    data = request.get_json()
    name = data.get("name")
    pattern = data.get("pattern")
    difficulty = data.get("difficulty")
    
    addProblem(name, pattern, difficulty)
    return jsonify({"message": f"Added {name}"}), 201

@app.route("/problems/<int:problemId>", methods = ["DELETE"])
def removeProblem(problemId):
    if deleteProblem(problemId):
        return jsonify({"message": f"Deleted problem {problemId}"})
    return jsonify({"error": "Problem not found"}), 404
    # data = request.get_json()
    # Id = data.get("Id")
    # problems = deleteProblem(Id)
    # return jsonify(problems)

#
@app.route("/stats", methods=["GET"])
def getStats():
    stats = leastPracticedPattern(knownPatterns)
    result = [{"pattern": p, "count": c} for p, c in stats]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)