from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def my_home():
	return render_template('index.html',title="My Portfolio")

@app.route('/<string:pagename>')
def html_render(pagename):
	title = pagename.split('.')[0].capitalize()
	return render_template(pagename,title=title)

def write_to_file(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open('database.txt',mode='a') as file:
		line = f'\n{email},{subject},{message}'
		file.write(line)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		return redirect('thankyou.html')
	else:
		return 'somethign went wrong'