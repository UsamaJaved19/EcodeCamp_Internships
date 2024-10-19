from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class BreastCancerForm(FlaskForm):
    texture_mean = StringField("Texture Mean",validators=[DataRequired()])
    smoothness_mean = StringField("Smoothness Mean",validators=[DataRequired()])
    compactness_mean = StringField("Compactness Mean",validators=[DataRequired()])
    concave_points_mean = StringField("Concave Points Mean",validators=[DataRequired()])
    symmetry_mean = StringField("Symmetry Mean",validators=[DataRequired()])
    fractal_dimension_mean = StringField("Fractal Dimension Mean",validators=[DataRequired()])
    texture_se = StringField("Texture Standard Error",validators=[DataRequired()])
    area_se = StringField("Area Standard Error",validators=[DataRequired()])
    smoothness_se = StringField("Smoothness Standard Error",validators=[DataRequired()])
    compactness_se = StringField("Compactness Standard Error",validators=[DataRequired()])
    concavity_se = StringField("Concavity Standard Error",validators=[DataRequired()])
    concave_points_se = StringField("Concave Points Standard Error",validators=[DataRequired()])
    symmetry_se = StringField("Symmetry Standard Error",validators=[DataRequired()])
    fractal_dimension_se = StringField("Fractal Dimension",validators=[DataRequired()])
    texture_worst = StringField("Texture Worst",validators=[DataRequired()])
    area_worst = StringField("Area Worst",validators=[DataRequired()])
    smoothness_worst = StringField("Smoothness",validators=[DataRequired()])
    compactness_worst = StringField("Compactness",validators=[DataRequired()])
    concavity_worst = StringField("Concavity Worst",validators=[DataRequired()])
    concave_points_worst = StringField("Concave Points Worst",validators=[DataRequired()])
    symmetry_worst = StringField("Symmetry Worst",validators=[DataRequired()])
    fractal_dimension_worst = StringField("Fractal Dimension Worst",validators=[DataRequired()])
    submit = SubmitField("Predict")