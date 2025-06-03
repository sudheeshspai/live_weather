from flask import Flask, request, render_template_string, session, redirect, url_for
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for sessions

api_key = os.getenv("WEATHERBIT_API_KEY")

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>🌤️ Weather App</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #333;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        overflow: hidden;
        position: relative;
    }

    /* Floating weather emojis background */
    body::before {
        content: "☀️🌤️⛅🌥️🌦️🌧️⛈️🌩️🌨️❄️🌫️";
        font-size: 5rem;
        position: absolute;
        top: 10%;
        left: 0;
        right: 0;
        text-align: center;
        opacity: 0.4;
        animation: float 20s linear infinite;
        pointer-events: none;
        user-select: none;
        white-space: nowrap;
    }

    @keyframes float {
        0% {transform: translateX(-100%);}
        100% {transform: translateX(100%);}
    }

    .container {
        background: rgba(255,255,255,0.95);
        border-radius: 25px;
        padding: 3rem 4rem;
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
        max-width: 700px;
        width: 90%;
        text-align: center;
        z-index: 1;
    }

    h1 {
        margin-bottom: 1.5rem;
        font-size: 2rem;
    }

    input[type=text] {
        width: 100%;
        padding: 15px;
        margin: 10px 0 25px 0;
        border: 1px solid #ccc;
        border-radius: 12px;
        font-size: 1.1rem;
    }

    button {
        background-color: #4a90e2;
        color: white;
        border: none;
        padding: 15px 25px;
        font-size: 1.1rem;
        border-radius: 12px;
        cursor: pointer;
        width: 100%;
    }

    button:hover {
        background-color: #357abd;
    }

    .result {
        margin-top: 30px;
        font-size: 1.3rem;
        font-weight: 600;
    }

    .error {
        margin-top: 30px;
        color: red;
        font-weight: 700;
    }

    .small-btn {
        margin-top: 20px;
        background-color: #888;
        font-size: 1rem;
        padding: 10px 20px;
        border-radius: 10px;
        width: auto;
    }

    .small-btn:hover {
        background-color: #555;
    }

    p {
        font-size: 1.1rem;
        margin: 1rem 0;
    }
</style>
</head>
<body>
    <div class="container">
        <h1>🌍 Global Average Temperature: {{ avg_temp if avg_temp is not none else 'N/A' }} °C</h1>

        {% if not session.get('username') %}
            <form method="post" action="{{ url_for('set_name') }}">
                <input type="text" name="username" placeholder="Enter your name to start" required autofocus />
                <button type="submit">Start</button>
            </form>
        {% else %}
            <p>Hello, <strong>{{ session['username'] }}</strong>! Queries left: {{ 3 - session.get('usage', 0) }}</p>
            
            {% if session.get('usage', 0) >= 3 %}
                <p class="error">You have reached your query limit (3 per session).</p>
                <form method="post" action="{{ url_for('reset_usage') }}">
                    <button class="small-btn" type="submit">Reset Usage</button>
                </form>
            {% else %}
                <form method="post">
                    <input type="text" name="user_input" placeholder='Ask for weather like "weather in Mumbai"' required autofocus />
                    <button type="submit">Get Weather</button>
                </form>
            {% endif %}

            {% if city %}
                <div class="result">
                    🌤️ Weather in <strong>{{ city.title() }}</strong>:<br>
                    Temperature: <strong>{{ temp }} °C</strong><br>
                    Condition: <strong>{{ desc }}</strong>
                </div>
            {% elif error %}
                <div class="error">{{ error }}</div>
            {% endif %}

            <form method="post" action="{{ url_for('logout') }}">
                <button class="small-btn" type="submit">Logout</button>
            </form>
        {% endif %}
    </div>
</body>
</html>
'''


def get_global_avg_temp():
    cities = ["New York", "London", "Tokyo", "Sydney", "Moscow", "Cairo"]
    temps = []
    for city in cities:
        url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}&units=M"
        response = requests.get(url)
        data = response.json()
        if "data" in data:
            temps.append(data["data"][0]["temp"])
    return round(sum(temps) / len(temps), 2) if temps else None

@app.route("/", methods=["GET", "POST"])


def home():
    if not session.get('username'):
        return redirect(url_for('set_name'))

    avg_temp = get_global_avg_temp()
    city = temp = desc = error = None

    if session.get('usage', 0) >= 3:
        # No more queries allowed
        return render_template_string(HTML, avg_temp=avg_temp, city=None, temp=None, desc=None, error=None)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").lower()
        # For simplicity: extract city as last word after "weather in" phrase
        city_found = None
        if "weather in " in user_input:
            city_found = user_input.split("weather in ")[-1].strip()
        else:
            error = "Please ask like 'weather in <city>'."

        if city_found and not error:
            url = f"https://api.weatherbit.io/v2.0/current?city={city_found}&key={api_key}&units=M"
            response = requests.get(url)
            data = response.json()
            if "data" in data:
                info = data["data"][0]
                city, temp, desc = city_found, info["temp"], info["weather"]["description"]
                session['usage'] = session.get('usage', 0) + 1
            else:
                error = f"Sorry, couldn't find weather data for '{city_found}'."

    return render_template_string(HTML, avg_temp=avg_temp, city=city, temp=temp, desc=desc, error=error)

@app.route("/set_name", methods=["GET", "POST"])
def set_name():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            session['username'] = username
            session['usage'] = 0
            return redirect(url_for('home'))
    return render_template_string(HTML, avg_temp=get_global_avg_temp(), city=None, temp=None, desc=None, error=None)

@app.route("/reset_usage", methods=["POST"])
def reset_usage():
    session['usage'] = 0
    return redirect(url_for('home'))

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
