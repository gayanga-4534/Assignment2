from application import app
from flask import render_template,request
from application import db_ctrl

@app.route("/")
def index():
    return render_template("index.html", index=True)

@app.route('/', methods=['POST'])
def my_form_post():
    u_id = request.form['u_id']
    load_amount = request.form['load_amount']
    confirmed_user_id = request.form['confirmed_user_id']
    user = db_ctrl.UserLoan()
    user.u_id = u_id
    user.load_amount = load_amount
    user.confirmed_user_id = confirmed_user_id

    if_valid = user.getSingleUserIfValid()
    return if_valid