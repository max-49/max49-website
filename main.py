import random
import requests
from flask_sitemap import Sitemap
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
ext = Sitemap(app=app)


@app.route('/')
def homepage():
    return render_template("index-pages/index.html", navbar="shared/navbar.html", num=random.randint(1, 2500))


@app.route('/ctf')
def ctf():
    return render_template("index-pages/ctf.html", navbar="shared/navbar.html", num=random.randint(1, 2500))


@app.route('/projects')
def projects():
    return render_template("index-pages/projects.html", page="index-pages/project-list.html", navbar="shared/navbar.html", num=random.randint(1, 2500))


@app.route('/projects/chembot')
def chembot():
    return render_template("index-pages/projects.html", page="index-pages/chembot.html", navbar="shared/navbar.html", num=random.randint(1, 2500))


@app.route('/round-9-writeups')
def round_9_writeups():
    return render_template("writeups/round-9-writeups.html", num=random.randint(1, 2500))


@app.route('/round-10-writeups')
def round_10_writeups():
    return render_template('writeups/round-10-writeups.html', num=random.randint(1, 2500))


@app.route('/round-11-writeups')
def round_11_writeups():
    return render_template('writeups/round-11-writeups.html', num=random.randint(1, 2500))


@app.route('/round-12-writeups')
def round_12_writeups():
    return render_template('writeups/round-12-writeups.html', num=random.randint(1, 2500))


@app.route('/round-13-writeups')
def round_13_writeups():
    return render_template('writeups/round-13-writeups.html', num=random.randint(1, 2500))


@app.route('/writeups')
def writeups():
    return render_template("writeups/writeups.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('status-codes/404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('status-codes/405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('status-codes/500.html'), 500


@app.route('/ictf-server-info')
def ictf_server():
    all_challs = (requests.get(
        'https://imaginaryctf.org/api/challenges/released')).json()
    my_challs = (requests.get(
        'https://imaginaryctf.org/api/solves/byuserid/86')).json()
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
    return render_template('index-pages/ictf-server-info.html', num=random.randint(1, 2500), solved=solved, unsolved=unsolved, score=score)


@app.route('/password')
def password():
    return render_template('password.html', num=random.randint(1, 2500))


@app.route('/submit', methods=['POST'])
def submit():
    password = request.form['pass']
    if(password == "^P8rv^Y3J}&sz(;dcJRA"):
        return render_template('writeups/round-14-writeups.html', num=random.randint(1, 2500))
    else:
        return render_template("password.html", error="Incorrect Password.")


@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.root_path + '/cdn/', filename, as_attachment=True)


@app.route('/robots.txt')
def robots():
    return open('robots.txt').read()


app.run(host='0.0.0.0', port=5000)
