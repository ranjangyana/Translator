from flask import Flask, render_template, request
from textblob import TextBlob

# initialize the app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit', methods = ["POST"])
def form_data():

    data = request.form.get('text')

    # Perform translation according to the language selected in dropdown

    lng = request.form.get('language')

    blob = TextBlob(data)
    trans = ''
    if lng=='hindi':
        trans = blob.translate(to='hi')
    elif lng=='odia':
        trans = blob.translate(to='or')
    elif lng=='gujarati':
        trans = blob.translate(to='gu')
    elif lng=='telugu':
        trans = blob.translate(to='te')
    elif lng=='tamil':
        trans = blob.translate(to='ta')
    elif lng=='malayalam':
        trans = blob.translate(to='ml')
    elif lng=='punjabi':
        trans = blob.translate(to='pa')
    elif lng=='kannada':
        trans = blob.translate(to='kn')
    elif lng=='bengali':
        trans = blob.translate(to='bn')

    # Detect original language

    ori_lng = blob.detect_language()
    
    if ori_lng == 'hi':
        ori_lng = 'Hindi'
    elif ori_lng == 'or':
        ori_lng = 'Odia'
    elif ori_lng == 'gu':
        ori_lng = 'Gujarati'
    elif ori_lng == 'te':
        ori_lng = 'Telugu'
    elif ori_lng == 'ta':
        ori_lng = 'Tamil'
    elif ori_lng == 'ml':
        ori_lng = 'Malayalam'
    elif ori_lng == 'pa':
        ori_lng = 'Punjabi'
    elif ori_lng == 'kn':
        ori_lng = 'Kannada'
    elif ori_lng == 'bn':
        ori_lng = 'Bengali'
    else:
        ori_lng = 'English'

    return render_template('form.html', data_trans = trans, data_ori_lang = ori_lng)
    

if __name__ == '__main__':
    app.run(debug=True)