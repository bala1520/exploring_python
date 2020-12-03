from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)
@app.route('/<username>/<int:game_id>')
def hello_world_root(username=None,game_id=None):
    return render_template("about.html", name=username, id=game_id)
@app.route('/hello/')
def hello_world():
    return 'i m Hello, World!'
@app.route('/blog/')
def hello_world_blog():
    return 'these are my blogs'
@app.route('/blog/2020/dogs')
def hello_world_blogs():
    return 'these are my dogs'

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def our_home(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        #return render_template('thank_you.html')
        return redirect('/thank_you.html')
    else:
    	return ("something went wrong")

@app.route('/login', methods=['POST', 'GET'])
def submi():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return ("submited form successfully")
    else:
    	return ("something went wrong")
