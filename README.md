<img src="https://s3.amazonaws.com/owler-image/logo/finnhub_owler_20210827_194040_original.png" width=300></img>

## Daily Stock Portfolio Report
___

This Python software sends a report to the specified email regarding the performance of the stocks in the [theoretical portfolio(s)](data/portfolios_input.xlsx) at the end of every trading day.

This report adds the following datapoints for each stock using the [Finnhub API](https://finnhub.io/):
- **Position PnL**
- **Position Value**
- **Day Open**
- **Day Close**
- **Day Change (%)**
- **Highest Weighted Analyst Trend (buy, strong buy, hold, etc.)**
- **Social Sentiment (Twitter Only)**

Upon initial startup of the bot, it to loads up an excel workbook containing three columns, "Symbol", "Entry Price", and "Shares".

The task is run on a scheduler that fetches all NYSE trading day closing times a year out from the script run date.
The thread sleeps until a trading close date is satisfied, when the report is built and sent.
___
### Local Setup:
1. Configure your local configuration in [_config.py](portfolio_report/_config.py):
   1. Set your SMTP configuration
   2. Specify your finnhub rate limit (default is free subscription)
2. Set required environment variables (.env file supported in root dir):
   ```bash
   FINNHUB_APIKEY=your_finnhub_apikey
   FROM_EMAIL=your_sender_email
   FROM_EMAIL_PASSWORD=your_sender_email_password
   ```
3. Modify the "INPUT_FILEPATH" and "RECIPIENT_EMAILS" variables in [main.py](main.py)
4. Run the script with `python main.py` from the root directory
___
### Email Report Demo:
![report_email_demo](img/demo.png)

### Roadmap:
- Integrate other datasources besides local workbook (TDAmeritrade API)