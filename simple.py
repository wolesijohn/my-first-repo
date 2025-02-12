from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def hello_world(): 
    return 'This is the Index page'
@app.route('/add', methods=['POST'])
def add():    
    req_data = request.get_json()    
    number_1 = req_data['number_1']    
    number_2 = req_data['number_2']    
    return str(int(number_1)+int(number_2))