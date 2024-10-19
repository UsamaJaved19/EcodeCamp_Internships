import pickle
import numpy as np

def prediction(features):
    model = pickle.load(open('breast_cancer_prediction_model.pkl','rb'))
    scaler = pickle.load(open('scaler.pkl','rb'))
    features_array = np.array(features).reshape(1, -1)
    normalized_feature = scaler.transform(features_array)
    result = model.predict(normalized_feature)
    disease = ''
    if int(result[0]) == 1:
        disease = 'Malignant'
        return disease
    else:
        disease = 'Benign'
        return disease

