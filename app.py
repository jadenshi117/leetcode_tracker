from flask import Flask, request, jsonify
from tracker import addProblem, loadProblems, leastPracticedPattern, knownPatterns

app = Flask(__name__)

@app.route("/")
def home():
    return "LeetCode Tracker API is running"

@app.route("/problems", methods = ["GET"])
def getProblems():
    problems = loadProblems()
    return jsonify(problems)

@app.route("/problems", methods = ["POST"])
def createProblem():
    data = request.get_json()
    name = data.get("name")
    pattern = data.get("pattern")
    difficulty = data.get("difficulty")

    addProblem(name, pattern, difficulty)
    return jsonify({"message": f"Added {name}"}), 201

@app.route("/stats", methods=["GET"])
def getStats():
    stats = leastPracticedPattern(knownPatterns)
    result = [{"pattern": p, "count": c} for p, c in stats]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)