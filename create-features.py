df['Previous Close'] = df['Close'].shift(1)
df['Sentiment Score Shifted'] = df['Sentiment Score'].shift(1)
df['MA_5'] = df['Close'].rolling(window=5).mean()
df['MA_10'] = df['Close'].rolling(window=10).mean()
 # Drop NaN values
 df.dropna(inplace=True)
 print(df.head()
