from sklearn.ensemble import RandomForestClassifier
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import accuracy_score
 # Define Features and Target
 X = df[['Previous Close', 'Sentiment Score Shifted', 'MA_5', 'MA_10']]
 df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)  # 1 = Price Up, 0 = Price Down
 y = df['Target']
 # Split Data
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 # Train Model
 model = RandomForestClassifier(n_estimators=100, random_state=42)
 model.fit(X_train, y_train)
 # Predict and Evaluate
 predictions = model.predict(X_test)
 accuracy = accuracy_score(y_test, predictions)
 print(f"Model Accuracy: {accuracy:.2f}")

# Last accuracy test: 97%
