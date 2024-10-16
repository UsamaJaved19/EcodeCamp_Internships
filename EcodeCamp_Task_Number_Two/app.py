# Required Libraries

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
import pickle

st.image('img.jpg',use_column_width='always')
st.title("Stock Price Prediction")

stock_id= st.text_input("Enter Stock ID e.g TSLA")

if stock_id:

    end= datetime.now()
    start =datetime(end.year-20,end.month,end.day)

    stock_data = yf.download(stock_id,start,end)

    model = pickle.load(open('stock_price_model.pkl','rb'))
    if not stock_data.empty:
        st.subheader("Stock Data")
        st.write(stock_data)

        split = int(len(stock_data)*0.7)

        x_stock = pd.DataFrame(stock_data[split:])
        def graphs(MA,stock_data):
            fig = plt.figure(figsize=(15,6))
            plt.plot(MA,'Orange')
            plt.plot(stock_data['Close'],'b')
            return fig

        st.subheader("Close Price and Mean Average for 250 days")
        stock_data['Close Price and Mean Average for 250 days']=stock_data['Close'].rolling(250).mean()

        MA= stock_data[['Close Price and Mean Average for 250 days']]
        st.pyplot(graphs(MA,stock_data))

        st.subheader("Close Price and Mean Average for 100 days")
        stock_data['Close Price and Mean Average for 100 days']=stock_data['Close'].rolling(100).mean()

        MA= stock_data[['Close Price and Mean Average for 100 days']]
        st.pyplot(graphs(MA,stock_data))

        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(x_stock[['Close']])

        x = []
        y = []

        for i in range(100,len(scaled_data)):
            x.append(scaled_data[i-100:i])
            y.append(scaled_data[i])

        x = np.array(x)
        y = np.array(y)

        predictions = model.predict(x)

        predictions = scaler.inverse_transform(predictions)
        y = scaler.inverse_transform(y)

        predictions_data = pd.DataFrame(
            {
                'Original': y.reshape(-1),
                'Predictions': predictions.reshape(-1)
            },
            index = stock_data.index[split+100:]
        )

        st.subheader("Original VS Predictions")
        st.write(predictions_data)
        st.subheader("Original VS Predictions")

        complete = pd.concat([stock_data['Close'][:split+100],predictions_data],axis=0)
        

        fig = plt.figure(figsize=(15,6))
        plt.plot(complete)
        plt.legend(["Data","Original",'Predicted'])
        st.pyplot(fig)
    else:
        st.warning("Please enter Valid Stock ID")