# 🌤️ Weather App

A simple Flask-based weather application that allows users to check the weather for a specific city and displays the global average temperature. The app uses the Weatherbit API for fetching weather data.

---

## Features

- 🌍 Displays the **global average temperature**.
- 🌤️ Allows users to query the weather for specific cities.
- 🔒 Session-based user management with a query limit (3 queries per session).
- 🎨 Beautiful and responsive UI with floating weather emojis.

---

## Project Structure

```
weather/
├── app.py                # Main Flask application
├── .env                  # Environment variables (e.g., API keys)
├── templates/            # HTML templates (if used separately)
├── static/               # Static files (CSS, JS, images)
└── README.md             # Project documentation
```

---

## Prerequisites

- Python 3.7 or higher
- Flask
- Requests
- python-dotenv

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Weatherbit API key:
   ```
   WEATHERBIT_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage

1. Enter your name to start the session.
2. Query the weather by typing phrases like:
   ```
   weather in Mumbai
   ```
3. View the global average temperature and weather details for the queried city.
4. Reset your query limit or log out as needed.

---
## API Reference

This app uses the [Weatherbit API](https://www.weatherbit.io/) to fetch weather data. Ensure you have a valid API key.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Weatherbit API](https://www.weatherbit.io/) - Weather data provider
- UI inspiration from modern web design trends
