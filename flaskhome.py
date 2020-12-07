from flask import Flask, escape, request
app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/edit')
def edit():
    return f'<h1>Edit!</h1>'

if __name__=='__main__':
	app.run(debug=True)