## Blake's Practice Project:

### --> _Daily Stock Portfolio Report Bot_ <--

While this project may seem difficult, I think that you'd learn a lot by completing it, and hopefully find it interesting.

**Let's pretend that I'm a client, and I'm giving you this as a job proposal:**

___

I would like to get a report sent to my email regarding the performance of the stocks in my portfolio at the end of every trading day.

This report should contain the following attributes for each stock:
- **PnL**
- **Day Open**
- **Day Close**
- **Day Change (%)**
- **Highest Weighted Analyst Trend (buy, strong buy, hold, etc.)**
- **Social Sentiment**

This software should be written using Python.

Upon initial startup of the bot, I will need it to load up a CSV containing two columns, "symbol" and "entryPrice."
Each row will contain a symbol, and the entryPrice from which I entered into the position (this will just be used to calculate PnL)

I've heard that https://finnhub.io/ has a great API for fetching the data that we need.

You will need to either run the bot on a daily "[cronjob](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800)" or use loop that sleeps until it detects that the end of a trading day has been satisfied.

**Gig Payment:** $20

___