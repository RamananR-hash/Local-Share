import socket 
import os
from flask import *  
try:
    os.mkdir("Files")
except:
    pass    
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save("Files/"+str(f.filename))
        return render_template("success.html", name = "Files/"+str(f.filename))   
  
if __name__ == '__main__':  
    app.run(host="192.168.1.102",port=80)  