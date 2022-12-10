from flask import Blueprint,render_template,request,flash

views = Blueprint(__name__,"views")

@views.route("/")
def index():
	flash("What's Your Name ?")
	return render_template("index.html")
	
@views.route("/greet",methods=['POST','GET'])
def greet():
	flash("Hi " + str(request.form['name_input']) +", Glad to see you")
	return render_template("index.html")