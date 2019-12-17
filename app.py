from flask import Flask , render_template , url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database1.sqlite3"
db = SQLAlchemy(app)

class company_suggestion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(120), unique=True, nullable=False)
	reason = db.Column(db.String (600), unique=False, nullable=False)
	share_price = db.Column(db.Integer(), unique=False, nullable=True)
	date = db.Column(db.DateTime, default = datetime.now())
db.create_all()



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/company_invested/", methods = ["GET","POST"])
def company_suggested():
	if request.method == "GET":
		return render_template('company_invested.html',title='Companies')

	if request.method == "POST":
		if request.form["share_price"]:
			print(request.form["company_name"])
			com_sugg=company_suggestion(company_name = request.form["company_name"], reason = request.form["reason"],share_price = request.form["share_price"])
		else:
			com_sugg=company_suggestion(company_name = request.form["company_name"], reason = request.form["reason"])
		try:
			db.session.add(com_sugg)
			db.session.commit()
		except:
			return "Sorry, there was issue while inserting the values."
		li = company_suggestion.query.all()
		dic = 	{
		'Stock_Price':0,
		'title': '',
		'content':'',
		'date_posted':0
		}
		post = []
		for row in li:	
			dic["Stock_Price"] = row.share_price	
			dic["title"] = row.company_name
			dic["reason"] = row.reason
			dic["date_posted"] = row.date
			print(dic)
			post.append(dic)
		print(post)
		return render_template('home.html',posts=post)
		

if __name__ == "__main__":
	app.run(debug=True)