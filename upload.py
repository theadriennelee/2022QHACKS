# from asyncio.log import logger
# from cmath import log
from flask import Flask, render_template, request, send_from_directory
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
from transcriber import transcriber
from pdfmake import pdf
import shutil
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
    try:
        if request.method == 'POST':
            f = request.files['myFile']
            f.save(secure_filename(f.filename))
            shutil.copyfile("C:\\Users\\Admin\\Documents\\GitHub\\2022QHACKS\\" + f.filename,
                            "C:\\Users\\Admin\\Documents\\GitHub\\2022QHACKS\\clone1.mp4" )
            test = transcriber(f.filename)
            test.wait()
            foo = test.getparagraphs()
            start, end = test.gettstamps()
            print("C:\\Users\\Admin\\Documents\\GitHub\\2022QHACKS\\" + f.filename)
            #app.logger(bar)
            pdf1 = pdf("Notes", foo,start,end, "C:\\Users\\Admin\\Documents\\GitHub\\2022QHACKS\\clone1.mp4")
            pdf1.gen2()
            #   return 'file uploaded successfully'
            return render_template("transcription.html")
    except:
        error_message = "Please select a file."
        return render_template("theNotebook.html", message=error_message)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    foobar = os.getcwd()
    #uploads = r"C:\Users\Adrienne Lee\Documents\Queens\Year 4\2022QHACKS"
    # Returning file from appended path
    # return send_from_directory(directory=uploads, filename=filename)
    return send_from_directory(foobar, filename)
		
if __name__ == '__main__':
   app.run(debug = True)