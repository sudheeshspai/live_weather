# 🌤️ Flask Weather App

A simple, elegant Flask web application to check current weather conditions for any city worldwide using the [Weatherbit.io API](https://www.weatherbit.io/).  
Additionally, it displays the global average temperature based on selected major cities and limits each user to 3 weather queries per session to prevent abuse.

---

## Features

- **User session support:** Enter your name to start and track usage limits.
- **Weather queries:** Ask for the weather of any city with a natural language style input like `"weather in Mumbai"`.
- **Global average temperature:** Shows the current average temperature for a fixed set of cities globally.
- **Usage limit:** Each user can query weather data up to 3 times per session.
- **Reset usage:** Easily reset your query count without logging out.
- **Logout:** Clear session and start fresh.
- **Beautiful UI:** Clean, modern design with floating weather emoji background and responsive layout.

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pip` package manager
- Weatherbit API Key — get a free API key from [Weatherbit.io](https://www.weatherbit.io/account/create)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sudheeshspai/live_weather                    
   cd live_weather/weather
2. Create and activate a virtual environment (optional but recommended):
      
   ```bash                                        
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate 

3. Install dependencies:
     ```bash
     pip install -r requirements.txt

### ⚠️ Important: Create Your `.env` File

Create a `.env` file in the **project root** directory and add your Weatherbit API key exactly as shown below.  
**This step is essential** — without the API key, the app **will not work**.

  ```ini
     WEATHERBIT_API_KEY=your_weatherbit_api_key_here
   ```
### Run the app

   ```bash
    python app.py
```
### Open your browser and visit
  ```cpp
     http://127.0.0.1:5000/
```
## License
### MIT License © 2025 sudheesh_s_pai
