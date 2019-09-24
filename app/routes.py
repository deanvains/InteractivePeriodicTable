from flask import render_template, flash, redirect, url_for, request, make_response
from app.models import periodicTable
from app.forms import DescForm, newElement
from app import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    pt = periodicTable.query.all()
    return render_template("homepage.html", title='Home Page', pt=pt)

@app.route('/element/<id>', methods=['GET', 'POST'])
def element(id):
    pt = periodicTable.query.get(id)
    return render_template('element.html', title='Element', pt=pt)
    
@app.route('/change/<id>', methods=['GET', 'POST'])
def change(id):
    element = periodicTable.query.get(id)
    form = DescForm()
    if form.validate_on_submit():
        element.description += '\n' + form.newDesc.data
        #error coming from not being able to find element
        db.session.commit()
        return render_template('element.html', title='Element', pt=element)
    return render_template('change.html', title='Change Description', pt=element, form=form)

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = newElement()
    if form.validate_on_submit():
        pt = pt = periodicTable(id=form.eid.data,name=form.ename.data)
        db.session.add(pt)
        db.session.commit()
        return render_template('input.html', form=form)
    return render_template('input.html', form=form)
