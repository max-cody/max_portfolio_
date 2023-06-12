import oandapyV20
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.exceptions import V20Error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import time
import keras
from keras.models import Sequential
from keras.layers import Dense


API_KEY = '836e106e4a1d44276425a3aa4559a74c-8892d73fe2368c087340ffcaa4915bad'
ACCOUNT_ID = '101-004-25992647-001'
BASE_URL = 'https://api-fxtrade.oanda.com/v3/accounts'  # trading api linked to the demo account for testing

# machine learning indicators
symbol = 'EUR_USD'
indicator_window = 10  # number of candles

api = oandapyV20.API(access_token=API_KEY, environment='practice')


# get historical candlestick data
def get_historical_data(symbol, count):
    params = {
        'count': count,
        'granularity': 'D'
    }
    r = oandapyV20.endpoints.instruments.InstrumentsCandles(instrument=symbol, params=params)
    api.request(r)
    data = r.response['candles']
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    df['mid'] = df['mid'].apply(lambda x: (float(x['h']) + float(x['1'])) / 2)
    return df['mid']

# calc the machine learning indicator
def calc_ml_indicator(data, window):
    # prep data
    X = pd.DataFrame(data)
    X.columns = ['close']
    X['returns'] = X['close'].pct_change()
    X['volatility'] = X['returns'].rolling(window).std()
    X['trend'] = X['returns'].rolling(window).mean()
    X['momentum'] = X['returns'].rolling(window).sum()

    # prep target variable
    X['target'] = X['returns'].shift(-1)
    X.dropna(inplace=True)
    X['target'] = X['target'].apply(lambda x: 1 if x > 0 else 0)


     # Split the data into features and target
    X_train, X_test, y_train, y_test = train_test_split(
        X.drop('target', axis=1), X['target'], test_size=0.2, shuffle=False)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    

    #create neural network

    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape =(X_train_scaled.shape[1],)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    #train the model
    model.fit(X_train_scaled, y_train, epochs=10, batch_size=32)

    #make predictions
    predictions = model.predict(X_test_scaled)
    predictions = (predictions > 0.5).astype(int)
    return predictions[-1][0]



def monitor_slippage(instrument, units, expected_price):
    # get the current market price
    params = {
        'instruments': instrument
    }
    r = oandapyV20.endpoints.pricing.PricingInfo(accountID=ACCOUNT_ID, params=params)
    api.request(r)
    price = r.response['prices'][0]['closeoutBid']  # use the closeout bid as the current market price

    # calc slippage
    slippage = expected_price - float(price)

    # print slippage information
    print('Slippage:', slippage)

# Place a market order
def place_market_order(instrument, units):
    request = MarketOrderRequest(instrument=instrument, units=units)
    try:
        response = api.request(oandapyV20.endpoints.order.OrderCreate(ACCOUNT_ID, data=request.data))
        if 'errorMessage' in response:
            print('Order placement failed:', response['errorMessage'])
            return False
        else:
            return True
    except V20Error as e:
        print('An error occurred:', str(e))
        return False


# Main trading loop
while True:
    try:
        # Get historical data for the indicator
        historical_data = get_historical_data(symbol, indicator_window + 1)

        # Calculate the machine learning indicator
        ml_indicator = calc_ml_indicator(historical_data, indicator_window)

        # Determine trading signal
        if ml_indicator == 1:
            # Buy signal
            expected_price = ...  # Set the expected price based on your strategy
            success = monitor_slippage(symbol, 100, expected_price)
            if success:
                print('Buy signal triggered - Placed market buy order')
            else:
                print('Buy signal triggered - Order placement failed')
        elif ml_indicator == 0:
            # Sell signal
            expected_price = ...  # Set the expected price based on your strategy
            success = monitor_slippage(symbol, -100, expected_price)
            if success:
                print('Sell signal triggered - Placed market sell order')
            else:
                print('Sell signal triggered - Order placement failed')

    except Exception as e:
        print('An error occurred:', str(e))

    # Sleep for a day
    time.sleep(24 * 60 * 60)