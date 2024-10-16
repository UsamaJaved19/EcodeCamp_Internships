import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
load_model = pickle.load(open('model.pkl','rb'))
load_tfdif = pickle.load(open('tfidf.pkl','rb'))
nltk.download('stopwords')
english_stopwords = stopwords.words('english')
def predict(comment):
    #preprocessing
    porter_stemmer = PorterStemmer()
    stemmed_data = re.sub('[^a-zA-Z]',' ' , comment)
    stemmed_data = stemmed_data.lower()
    stemmed_data = stemmed_data.split()  
    stemmed_data = [porter_stemmer.stem(word) for word in stemmed_data if word not in english_stopwords]
    stemmed_data = ' '.join(stemmed_data)
    stemmed_data

    #conversion into feature vector
    x = load_tfdif.transform([stemmed_data])

    # model prediction
    predictions = load_model.predict(x)[0]

    message=''
    if predictions == 0:
        message = 'Negative'
        return message
    else:
        message = 'Positive'
        return message
    


