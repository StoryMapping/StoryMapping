from flask import Flask
import os
from flask import render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def starting_page(top_story1=None):
    #top_story1 = text_input(url1=None,url2=None,url3=None,url4=None,url5=None)
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('newHome.html')


if __name__ == '__main__':
    app.run(port=5001)
