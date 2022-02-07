from flask import Blueprint, render_template    

views = Blueprint('views', __name__)
#rout page for home of website
@views.route('/')
def home():
    return render_template("home.html")