# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, render_template, request, redirect, url_for, flash

from models import *

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

app = Flask(__name__)
app.config['SECRET_KEY']='jdsnijf493fs9fjsa09wf9ds7g'

@app.route('/')
def index():
    docs = db.collection('employees').get()
    employees = [Employee.from_dict(doc.to_dict()) for doc in docs]
    return render_template('index.html', employees=employees)

@app.route('/new-employee', methods=['POST'])
def new_employee():
    try:
        name=request.form.get('name')
        email=request.form.get('email')
        age=int(request.form.get('age'))
        address=request.form.get('address')
        employed=bool(request.form.get('employed'))

        result = db.collection('employees').where('email', '==', email).get()
        if result:
            flash("Empregado já existe","warning")
            return redirect(url_for('index'))

        employee = Employee(name=name, email=email, age=age, address=address, employed=employed)

        db.collection('employees').document().set(employee.to_dict())
        flash("Dados inseridos com sucesso!!", "success")
    except:
        pass
    return redirect(url_for('index'))

@app.route('/delete-employee/<string:email>')
def delete_employee(email):
    result = db.collection('employees').where('email', '==', email).get()[0]

    if result:
        db.collection('employees').document(result.id).delete()
        flash("Dados excluídos com sucesso!!", "success")
    else:
        flash(f"Não foi possível encontrar empregado com email={email}", "warning")
    return redirect(url_for('index'))

@app.route('/update-employee/<string:email>', methods=['POST'])
def update_employee(email):
    result = db.collection('employees').where('email', '==', email).get()[0]

    if result:
        name=request.form.get('name')
        email=request.form.get('email')
        age=int(request.form.get('age'))
        address=request.form.get('address')
        employed=bool(request.form.get('employed'))
        employee = db.collection('employees').document(result.id)
        employee.update({
            'name': name,
            'email': email,
            'age': age,
            'address': address,
            'employed': employed
        })
        flash("Dados atualizados com sucesso!!", "success")

    return redirect(url_for('index'))
    



if __name__=="__main__":
    app.run(debug=True)

"""# Add documents
data={'name':'John Smith', 'age':40, 'employed':True}
db.collection('people').add(data)"""

