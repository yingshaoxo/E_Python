import sys
import os
import subprocess

EXEC = sys.executable #local pythonw.exe

def run_py_file(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return str(result.stdout)

def run_py_codes(py_codes):
    codes = str(py_codes)
    if codes.count('print(')==0 and codes.count('import ')==0:
        try:
            result = str(eval(codes))
        except:
            result = 'error'
        return result
    else:
        py_path = os.path.dirname(os.path.realpath(__file__)) + '\\codes.txt'
        code_bytes = codes.encode('utf-8',  'ignore')
        open(py_path, 'wb').write(code_bytes)
        result = str(run_py_file(py_path))
        return result



from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home_page(): #http://127.0.0.1:5000
    return 'POST codes to http://127.0.0.1:5000/Python/'
    
@app.route('/Python/', methods = ['POST', 'GET'])
def run_python():
    if request.method == 'GET': #http://127.0.0.1:5000/Python
        return 'Only support POST!'

    elif request.method == 'POST': #POST codes to http://127.0.0.1:5000/Python/
        try:
            codes = request.data.decode('utf-8')
        except:
            codes = request.data.decode('gb2312')
        print(codes)
        
        if codes=='':
            return 'You give me nothing!'
        else:
            return run_py_codes(codes)

@app.errorhandler(500)
def handle_bad_request():
    return '500\nInternal Server Error'

if __name__ == '__main__':
    app.run()
