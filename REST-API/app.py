from flask import Flask, jsonify


app = Flask(__name__)


department = [{'dept_id' : '01', 'dept_name' : 'CSE','description':'programmer'},
{'dept_id' : '02', 'dept_name' : 'IT','description':'software engineering'},
{'dept_id' : '03', 'dept_name' : 'ECE','description':'electronics'}]

@app.route('/')
def index():
    return "welcome to the course API"

@app.route("/department",methods=['GET'])
def get():
    return jsonify({'department':department})


@app.route("/department/<int:dept_id>",methods=['GET'])
def get_department(dept_id):
    return jsonify({'department':department[dept_id]})


@app.route("/department",methods=['POST'])
def create():
    dept={'dept_id' : '04', 'dept_name' : 'CSBS','description':'Computer programmer'}
    department.append(dept)
    return jsonify({'create':dept})

@app.route("/department/<int:dept_id>",methods=['PUT'])
def department_update(dept_id):
    department[dept_id]['Desription'] = "XYZ"
    return jsonify({'department':department[dept_id]}) 

@app.route("/department/<int:dept_id>",methods=['DELETE'])
def delete(dept_id):
    department.remove(department[dept_id])              
    return jsonify({'result':True})


if __name__ =="__main__":
    app.run(debug=True)    