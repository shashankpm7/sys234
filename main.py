from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "fd55fdc3"
BASE_URL = f"https://www.omdbapi.com/?apikey={API_KEY}"


@app.route('/')
def home():
    recommended_movies = ["Inception", "Interstellar", "Joker"]
    recommended_data = []
    for title in recommended_movies:
        response = requests.get(f"{BASE_URL}&t={title}")
        if response.status_code == 200 and response.json().get("Response") == "True":
            recommended_data.append(response.json())
    return render_template('index.html', recommended_movies=recommended_data)


@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if len(query) < 3:
        return jsonify([])

    response = requests.get(f"{BASE_URL}&s={query}")
    if response.status_code == 200 and response.json().get("Response") == "True":
        return jsonify(response.json().get("Search", []))
    return jsonify([])


if __name__ == "__main__":
    app.run(debug=True)
