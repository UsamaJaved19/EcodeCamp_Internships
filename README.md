# Ecode Internships

### Overview
This repository contains three major projects developed during my internship at **Ecode Camp**. Each project demonstrates the application of machine learning and deep learning techniques to solve real-world problems in diverse fields such as sentiment analysis, healthcare, and finance. The projects included are:
- **Sentiment Analysis**
- **Breast Cancer Prediction**
- **Stock Price Prediction**

### Projects

#### 1. Sentiment Analysis
This project involves building a model that analyzes and predicts the sentiment (positive or negative) of social media posts or other text data.

- **Model**: Logistic Regression
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Framework**: Flask (Web Application)
- **Dataset**: Social media data or text data (custom dataset)
- **Objective**: To predict whether a given text input expresses positive or negative sentiment.
  
##### Key Features:
- Preprocessing text data including tokenization, stopword removal, and TF-IDF transformation.
- Training a Logistic Regression model to classify sentiments.
- Web application built using **Flask** to allow users to input text and receive sentiment predictions.

##### Usage:
1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000` to use the sentiment prediction tool.

#### 2. Breast Cancer Prediction
This project predicts whether a patient has breast cancer based on input medical features.

- **Model**: Multiple models trained, with the best selected based on accuracy.
- **Dataset**: A breast cancer dataset with 22 features, including tumor size, texture, etc.
- **Framework**: Flask (Web Application)
- **Objective**: Predict whether a breast tumor is benign or malignant.
- **Training Data Shape**: (114, 22)

##### Key Features:
- Multiple classification models trained, including Logistic Regression, Decision Trees, and Random Forest.
- Selection of the model with the highest accuracy for prediction.
- A web application built with **Flask** to allow users to input patient data and receive predictions.

##### Usage:
1. Run the Flask web application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000` to input patient data and get predictions.

#### 3. Stock Price Prediction
This project predicts stock prices using historical data, employing an **LSTM (Long Short-Term Memory)** model for time-series forecasting.

- **Model**: LSTM (Long Short-Term Memory)
- **Feature Engineering**: MinMaxScaler applied for scaling stock prices.
- **Sequence Length**: 200
- **Framework**: Streamlit (Web Application)
- **Dataset**: Stock price data (e.g., from Yahoo Finance)
- **Objective**: Predict future stock prices based on historical data.

##### Key Features:
- Data scaling using **MinMaxScaler**.
- Time-series forecasting using an LSTM network.
- Hyperparameter tuning to optimize model performance, achieving the best RMSE (236.55).

##### Usage:
1. Run the Streamlit web app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the local Streamlit URL to interact with the stock prediction tool.

### Technologies Used
- **Python**: The main programming language.
- **Flask**: Web framework used for the Sentiment Analysis and Breast Cancer Prediction projects.
- **Streamlit**: For building interactive web apps (used in Stock Price Prediction).
- **TensorFlow/Keras**: For building deep learning models (e.g., LSTM for stock price prediction).
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Scikit-learn**: For machine learning algorithms like Logistic Regression, Decision Trees, etc.
- **Matplotlib & Seaborn**: For data visualization and performance analysis.

### Installation
To run any of the projects locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecode-internships.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ecode-internships
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Future Enhancements
- **Sentiment Analysis**: Expand the project to handle multi-class sentiment analysis (e.g., positive, negative, neutral).
- **Breast Cancer Prediction**: Integrate more advanced models or ensemble techniques for better accuracy.
- **Stock Price Prediction**: Improve the forecasting by incorporating additional features like news sentiment or market indicators.

### License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contact Information
For further inquiries or suggestions, feel free to reach out at:
- **Email**: usama11javed@outlook.com
