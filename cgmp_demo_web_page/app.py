from flask import Flask, render_template, request
import os
from database import Database
from utils import generate_number
app = Flask(__name__) # flask object

@app.route('/')  #home page address
def index():   # function that will run when the home address is given
    return render_template('index.html')

@app.route('/blog')  #home page address
def blog():   # function that will run when the home address is given
    page_name = 'home'
    return render_template('blog.html',page_name = page_name)
@app.route('/about')  #home page address
def about():   # function that will run when the home address is given
    page_name = 'about'
    return render_template('about.html',page_name = page_name)
@app.route('/contact')  #home page address
def contact():   # function that will run when the home address is given
    page_name = 'contact'
    return render_template('contact.html',page_name = page_name)
@app.route('/404')  #home page address
def error():   # function that will run when the home address is given
    page_name = 'error'
    return render_template('404.html',page_name = page_name)
@app.route('/single')  #home page address
def single():   # function that will run when the home address is given
    page_name = 'single'
    return render_template('single.html',page_name = page_name)
@app.route('/expenseform',methods = ['GET','POST'])  #home page address
def expenseform():   # function that will run when the expenseform address is given
    page_name = 'expenseform'
    msg = ''
    if request.method == 'POST':
        item = request.form.get('item')
        price = request.form.get('price')
        print(item,price)
        db = Database()
        db.create_table()
        status = db.add(item,price)
        if status:
            msg = 'successfully saved'
        else:
            msg = "could'nt save"
    results = Database().view()

    return render_template('expenseform.html',page_name = page_name,msg = msg,results=results)
@app.route('/results')  #home page address
def results():   # function that will run when the home address is given
    numbers = generate_number(100)
    return render_template('results.html',num = numbers,page_name = 'results')
    # here we send the result of the 'numbers' variable as 'num' variable in 'results.html' page 
if __name__ == "__main__":
    app.run(debug=True) # starts the webserver when we run app.py

