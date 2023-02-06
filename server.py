from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 

@app.route('/fanClub', methods=['GET', 'POST'])
def atriFan():
#   user_name = request.args.get("userName", "unknown")
  if request.method == 'POST':
    print(request.get('postTitle'))
    return render_template('index.html') 
  return render_template('index.html') 

# @app.route('/submit', methods=['GET','POST'])
# def atriFan():
#   if request.method = 'POST':
#     user_name = request.get('postTitle')
#   else:
#     user_name = " "
#   return render_template('check.html', user_name = user_name) 