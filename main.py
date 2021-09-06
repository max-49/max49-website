from flask import Flask, render_template, render_template_string, request, send_file, send_from_directory
from flask_sitemap import Sitemap
import random
import requests
import json
  
app = Flask(__name__)
ext = Sitemap(app=app)

@app.route('/')
def homepage():
  cache = random.randint(1,75308171284612946)
  return render_template("index.html", num=cache)

@app.route('/robots.txt')
def robots():
  return render_template("robots.txt", mimetype='text/plain')

@app.route('/ctf.html')
def ctf():
  cache = random.randint(1,75308171284612946)
  return render_template("ctf.html", num=cache)

@app.route('/projects')
def projects():
  cache = random.randint(1,75308171284612946)
  return render_template("projects.html", num=cache)

@app.route('/projects/chembot.html')
def chembot():
  cache = random.randint(1,75308171284612946)
  return render_template("chembot.html", num=cache)

@app.route('/round-9-writeups.html')
def round9writeups():
  return render_template("round-9-writeups.html")

@app.route('/writeups.html')
def writeups():
  return render_template("writeups.html")

@app.route('/why.html')
def why():
  return render_template("why.html", key="6LfkIcUaAAAAALH9gAiiuFli2rcF2TCpXbbmHQ1M")

@app.route('/why.html', methods=["POST"])
def captcha():
  return render_template("roovoid.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)  
def method_not_allowed(e):
    return render_template('405.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/round-10-writeups.html')
def gone():
  return render_template('round-10-writeups.html')

@app.route('/status-codes/best-code')
def teapot():
  return render_template('status.html', code="418", error="I'm a teapot", image="https://cdn.discordapp.com/emojis/783451741437034497.png?v=1"), 418

@app.errorhandler(429)
def requests_handle(e):
    return render_template('status.html', code="429", error="Too many requests", image="https://cdn.discordapp.com/emojis/811701750260039722.png?v=1"), 429

@app.route('/status-codes/429')
def requestsa():
  return render_template('status.html', code="429", error="Too many requests", image="https://cdn.discordapp.com/emojis/811701750260039722.png?v=1"), 429

@app.route('/status-codes/504')
def gateway():
  return render_template('status.html', code="504", error="Bad Gateway", image="https://cdn.discordapp.com/emojis/802303406525513728.png?v=1"), 504

@app.route('/status-codes/')
def list():
  return render_template('status.html', code="000", error="(placeholder because I didn't set this page up yet.)", image="https://cdn.discordapp.com/emojis/802303406525513728.png?v=1")

@app.errorhandler(504)
def gateway_handle(e):
    return render_template('status.html', code="504", error="Bad Gateway", image="https://cdn.discordapp.com/emojis/802303406525513728.png?v=1"), 504

@app.route('/cookie_test')
def cookie():
  return render_template('likes.html')

@app.route('/round-11-writeups.html')
def round_11_pog():
  return render_template('round-11-writeups.html')

@app.route('/ictf-server-info.html')
def ictf_server():
  all_challs = (requests.get('https://imaginaryctf.org/api/challenges/released')).json()
  my_challs = (requests.get('https://imaginaryctf.org/api/solves/byuserid/86')).json()
  all_solves = []
  all_list = []
  all_list_alt = []
  for i in range(len(my_challs)):
    all_solves.append(my_challs[i]["challenge"]["title"])
  for i in range(len(all_challs)):
    all_list.append(all_challs[i]["title"])
  for thing in all_list:
    all_list_alt.append(thing)
  for thing in all_list_alt:
    if(thing in all_solves):
      all_list.remove(thing)
  score = my_challs[0]["user"]["score"]
  solved = '<br>'.join(all_solves)
  unsolved = '<br>'.join(all_list)
  cache = random.randint(1,75308171284612946)
  return render_template('ictf-server-info.html', num=cache, solved=solved, unsolved=unsolved, score=score)  

@app.route('/password.html')
def password():
  cache = random.randint(1,75308171284612946)
  return render_template('password.html', num=cache)

@app.route('/submit', methods=['POST'])
def submit():
  password = request.form['pass']
  if(password == "^P8rv^Y3J}&sz(;dcJRA"):
    cache = random.randint(1,75308171284612946)
    return render_template('round-13-writeups.html', num=cache)
  else:
    return render_template("password.html", error="Incorrect Password.")

@app.route('/round-12-writeups.html')
def round_12_yo():
  cache = random.randint(1,75308171284612946)
  return render_template('round-12-writeups.html', num=cache)

@app.route('/yo')
def yolol():
  print(request.accept_languages)
  return render_template_string("yo")

@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.root_path + '/cdn/', filename, as_attachment=True)

app.run(host='0.0.0.0', port=8080)