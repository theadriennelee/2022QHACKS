# from asyncio.log import logger
# from cmath import log
from flask import Flask, render_template, request
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
app = Flask(__name__)

@app.route('/')
def home():
    # return("Hello World")
    return render_template('homepage.html')

@app.route('/theNotebook')
def theNotebook():
    return render_template('theNotebook.html')

# @app.route('/upload')
# def upload_file():
#    return render_template('transcription.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    # return render_template('transcription.html')
    # app.logger("hello")
    if request.method == 'POST':
      f = request.files['myFile']
      f.save(secure_filename(f.filename))
    #   return 'file uploaded successfully'
    return render_template("transcription.html")
		
if __name__ == '__main__':
   app.run(debug = True)