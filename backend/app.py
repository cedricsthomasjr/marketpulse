from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load the JSON file (Ensure the path is correct)
file_path = os.path.join(os.path.dirname(__file__), "stocks.json")
print("Loading stocks from:", file_path)

with open(file_path, "r") as f:
    stock_data = json.load(f)
    print(f"Loaded {len(stock_data)} stocks.")

@app.route("/api/search", methods=["GET"])
def search_stocks():
    query = request.args.get("q", "").lower()
    print("Query received:", query)

    if not query:
        return jsonify(stock_data)  # Return all data if no query is provided

    matches = [
        stock for stock in stock_data
        if query in stock["symbol"].lower() or query in stock["name"].lower()
    ]

    return jsonify(matches)


if __name__ == "__main__":
    app.run(debug=True)
