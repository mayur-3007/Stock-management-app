from flask import Flask , render_template , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
db = SQLAlchemy(app)

class company_suggestion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(120), unique=True, nullable=False)
	reason = db.Column(db.String (600), unique=False, nullable=False)
	share_price = db.Column(db.Integer(), unique=False, nullable=True)
db.create_all()

	
posts = [
	{
		'Stock_Price':'Stock Price',
		'title': 'Company 1',
		'content':'Short content',
		'date_posted':'April 21,2019'
	},
	{
		'Stock_Price':'Stock Price',
		'title': 'Company 2',
		'content':'Short content',
		'date_posted':'April 21,2019'
	},
	{
		'Stock_Price':'Stock Price',
		'title': 'Company 66',
		'content':'Short content',
		'date_posted':'April 21,2019'
	},
	{
		'Stock_Price':'Stock Price',
		'title': 'Company 543',
		'content':'Short content',
		'date_posted':'April 21,2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=posts)

@app.route("/company_invested")
def about():
	return render_template('company_invested.html',title='Companies')

if __name__ == "__main__":
	app.run(debug=True)