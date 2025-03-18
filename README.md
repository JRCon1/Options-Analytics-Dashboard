# Options Analytics Dashboard

A comprehensive options analytics dashboard built with Dash, featuring real-time options data, Greeks calculations, and strategy analysis tools.

## Features

- Real-time options chain data from Yahoo Finance
- Interactive 3D visualization of options Greeks
- Options strategy builder (Iron Condor, Butterfly, Calendar Spread)
- Backtesting capabilities with IV adjustment
- Payoff diagram generation
- Export functionality (CSV and Excel)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/JRCon1/options-analytics-dashboard.git
cd options-analytics-dashboard
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The dashboard will be available at `http://localhost:8050`

## Deployment

This application is configured for deployment on Render. To deploy:

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:server`

## License

MIT License

## Acknowledgments
- Data provided by Yahoo Finance
- Built with Plotly Dash
- Icons from Font Awesome

## Future Enhancements
- Real-time data streaming
- Interactive charts and visualizations
- Additional data sources
- Portfolio tracking functionality
- Advanced analytics tools

## Contact
For questions and support, please open an issue in the GitHub repository.

---
*Note: This project is for educational and research purposes only. Please ensure compliance with all relevant financial data usage terms and conditions.* 
