from flask import Flask, render_template,url_for
from form import BreastCancerForm
from predict import prediction

app = Flask(__name__)
app.config['SECRET_KEY'] = "qwerty123"


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = BreastCancerForm()
    result = None
    if form.validate_on_submit():
        # Collect all 22 features from form

        features = []
        cols = ['texture_mean', 'smoothness_mean', 'compactness_mean',
                'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                'texture_se', 'area_se', 'smoothness_se', 'compactness_se',
                'concavity_se', 'concave_points_se', 'symmetry_se',
                'fractal_dimension_se', 'texture_worst', 'area_worst',
                'smoothness_worst', 'compactness_worst', 'concavity_worst',
                'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst']
        for i in range(len(cols)): 
            feature_value = float(getattr(form, cols[i]).data)
            features.append(feature_value)

        result = prediction(features)

    return render_template("index.html", form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
