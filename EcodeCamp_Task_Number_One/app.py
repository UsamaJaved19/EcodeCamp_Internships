from flask import Flask,render_template,flash,url_for,redirect
from form import Sentiment_Analyze
from prediction import predict
app = Flask(__name__)
app.config['SECRET_KEY']='qwerty123'


@app.route('/',methods=['GET','POST'])
@app.route('/home' ,methods=['GET','POST'])
def home():
    form = Sentiment_Analyze()
    if form.validate_on_submit():
        comment = form.text.data
        result = predict(comment)
        return render_template('index.html' ,form=form,result=result)
        
    
    return render_template('index.html',form=form)


        




if __name__ == '__main__':
    app.run(debug=True)

