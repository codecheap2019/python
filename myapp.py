from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")

def home(): 
	return "Hello World!"
	
@app.route("/about")

def about():
	return "This About"
	
if __name__ == '__main__':
	app.run(debug=True)
