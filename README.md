# Server Traffic Analysis

This project analyzes server log data to extract insights about IP traffic, hourly requests, and major contributors. The application allows users to specify a date and visualize key metrics in an interactive Streamlit dashboard.

## Features
- Extract distinct IP addresses that accessed the server on a given day.
- Display hourly traffic trends for better analysis.
- Identify IPs contributing to 85% of total traffic.
- Determine hours contributing to 70% of the traffic.
- Interactive dashboard for visualization.

## Tech Stack
- **Python** (Data Processing)
- **Streamlit** (Dashboard Visualization)
- **Pandas** (Data Handling)
- **Regular Expressions** (Log Parsing)

## How to Use
1. **Clone the repository:**
   ```sh
   git clone https://github.com/kunal534/Sawal_web_test.git
   cd Sawal_web_test
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Streamlit dashboard:**
   ```sh
   streamlit run app.py
   ```
4. **Specify a date in the dashboard** to view the traffic analysis.

## Links
- **GitHub Repo:** [Sawal_web_test](https://github.com/kunal534/Sawal_web_test)
- **Live Dashboard:** [Streamlit App](https://sawalweb.streamlit.app)


