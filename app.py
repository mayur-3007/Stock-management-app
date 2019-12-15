from flask import Flask , render_template , url_for

app = Flask(__name__)

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
		'title': 'Company 3',
		'content':'Short content',
		'date_posted':'April 21,2019'
	},
	{
		'Stock_Price':'Stock Price',
		'title': 'Company 4',
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