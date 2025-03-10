 # Load sentiment data
 sentiment_data = pd.read_csv("sentiment_scores.csv")
 # Merge stock price with sentiment scores
 df = pd.merge(stock_data, sentiment_data, on="Date")
 print(df.head()
