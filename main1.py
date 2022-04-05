from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

class Users(db.Model):
	uid = db.Column(db.Integer, primary_key=True)
	f_name = db.Column(db.String(50), unique=True)
	l_name = db.Column(db.String(50), unique=True)
	age = db.Column(db.Float)

#db.create_all()

@app.route('/', methods=['GET'])
def home() -> 'html':

	return render_template('home.html')


@app.route('/cred')
def cred() -> 'html':

	return render_template('index.html')


@app.route('/well', methods=['POST'])
def greet() -> str:
	
	if request.method == 'POST':

		f_name = request.form['fn']
		l_name = request.form['ln']
		age = request.form['ag']

		create_user = Users(f_name=f_name, l_name=l_name, age=age)
		db.session.add(create_user)
		db.session.commit()

	return render_template('welcome.html', f_name=f_name, l_name=l_name, age=age)	



if __name__ == "__main__":
	app.run(debug=True)		

