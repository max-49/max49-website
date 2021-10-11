import json
import random
import requests
from flask_sitemap import Sitemap
from flask import Flask, render_template, request, send_from_directory, render_template_string

app = Flask(__name__)
ext = Sitemap(app=app)


@app.route('/')
def homepage():
    return render_template("index-pages/index.html", navbar="shared/navbar.html", home="active", num=random.randint(1, 2500))


@app.route('/ctf')
def ctf():
    return render_template("index-pages/ctf.html", navbar="shared/navbar.html", ctf="active", num=random.randint(1, 2500))


@app.route('/projects')
def projects():
    return render_template("index-pages/projects.html", page="index-pages/project-list.html", projects="active", navbar="shared/navbar.html", num=random.randint(1, 2500))


@app.route('/projects/chembot')
def chembot():
    return render_template("index-pages/projects.html", page="index-pages/chembot.html", projects="active", navbar="shared/navbar.html", num=random.randint(1, 2500))

@app.route('/projects/chembot/jsongenerator')
def gen():
    return render_template("index-pages/generator.html", projects="active", navbar="shared/navbar.html", num=random.randint(1, 2500))

@app.route('/projects/challenges')
def challenges():
    with open('mychalls.json') as j:
        writeups = json.load(j)
    return render_template("index-pages/projects.html", page="index-pages/challenges.html", writeups=writeups, projects="active", navbar="shared/navbar.html", num=random.randint(1, 2500))

@app.route('/round-9-writeups')
def round_9_writeups():
    return render_template("writeups/round-9-writeups.html", navbar="shared/navbar.html", ictf="active", num=random.randint(1, 2500))

@app.route('/round-10-writeups')
def round_10_writeups():
    return render_template('writeups/round-10-writeups.html', navbar="shared/navbar.html", ictf="active", num=random.randint(1, 2500))


@app.route('/round-11-writeups')
def round_11_writeups():
    return render_template('writeups/round-11-writeups.html', navbar="shared/navbar.html", ictf="active", num=random.randint(1, 2500))


@app.route('/round-12-writeups')
def round_12_writeups():
    return render_template('writeups/round-12-writeups.html', navbar="shared/navbar.html", ictf="active", num=random.randint(1, 2500))


@app.route('/round-13-writeups')
def round_13_writeups():
    return render_template('writeups/round-13-writeups.html', navbar="shared/navbar.html", ictf="active", num=random.randint(1, 2500))


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
    return render_template('index-pages/ictf-server-info.html', ictf="active", num=random.randint(1, 2500), navbar="shared/navbar.html", solved=solved, unsolved=unsolved, score=score)


@app.route('/password')
def password():
    return render_template('password.html', num=random.randint(1, 2500))


@app.route('/submit', methods=['POST'])
def submit():
    password = request.form['pass']
    if(password == "^P8rv^Y3J}&sz(;dcJRA"):
        with open('writeups.json') as j:
            writeups = json.load(j)
        return render_template('writeups/round-14-writeups.html', navbar="shared/navbar.html", writeups=writeups, ictf="active", num=random.randint(1, 2500))
    else:
        return render_template("password.html", error="Incorrect Password.")


@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.root_path + '/cdn/', filename, as_attachment=True)


@app.route('/robots.txt')
def robots():
    return open('robots.txt').read()


@app.route('/login', methods=["POST"])
def logins():
    username = request.form['username']
    password = request.form['pass']
    if(username == "max49-admin" and password == "MCS_Cypat!1" or username == 'test-admin-acc' and password == 'super-secure-pass'):
        challs = (requests.get('https://imaginaryctf.org/api/challenges/released')).json()
        with open('writeups.json') as j:
            current_writeups = json.load(j)
        current_names = []
        solved_names = []
        for chall in challs:
            current_names.append(chall['title'])
        for writeup in current_writeups:
            solved_names.append(writeup['title'])
        for name in solved_names:
            if(name in current_names):
                current_names.remove(name)
        current_names.reverse()
        return render_template("admin/panel.html", navbar="shared/navbar.html", chall_info='', challs=current_names, num=random.randint(1, 2500))
    else:
        return render_template("index-pages/index.html", navbar="shared/navbar.html", home="active", num=random.randint(1, 2500))

@app.route('/submitwriteup', methods=["POST"])
def submitwriteup():
    selected_chall = request.form['chall']
    challs = (requests.get('https://imaginaryctf.org/api/challenges/released')).json()
    for chall in challs:
        if(selected_chall == chall['title']):
            info_chall = chall
    return render_template("admin/panel.html", navbar='shared/navbar.html', iswriteup="yes", chall_info=info_chall, num=random.randint(1,2500))

@app.route('/addwriteup', methods=["POST"])
def addwriteup():
    chall_id = request.form['id']
    title = request.form['title']
    category = request.form['category']
    description = request.form['description']
    attachments = request.form['attachments']
    author = request.form['author']
    points = request.form['points']
    difficulty = request.form['difficulty']
    writeup = request.form['writeup']
    flag = request.form['flag']
    rating = request.form['rating']
    guessy = request.form['guessy']
    with open('writeups.json') as j:
        writeups = json.load(j)
    writeups.append({'id': int(chall_id), 'title': title, 'category': category, 'description': description, 'attachments': attachments, 'author': author, 'points': points, 'difficulty': difficulty, 'writeup': writeup, 'flag': flag, 'rating': rating, 'guessy': guessy})
    with open('writeups.json', 'w') as j:
        json.dump(writeups, j)
    
    challs = (requests.get('https://imaginaryctf.org/api/challenges/released')).json()
    with open('writeups.json') as j:
        current_writeups = json.load(j)
    current_names = []
    solved_names = []
    for chall in challs:
        current_names.append(chall['title'])
    for writeup in current_writeups:
        solved_names.append(writeup['title'])
    for name in solved_names:
        if(name in current_names):
            current_names.remove(name)
    current_names.reverse()
    return render_template("admin/panel.html", navbar="shared/navbar.html", chall_info='', challs=current_names, info=f"Writeup for {title} successfully added!", num=random.randint(1, 2500))


@app.route('/addmychall', methods=["POST"])
def addmychall():
    selected_chall = request.form['chall']
    return render_template("admin/panel.html", navbar='shared/navbar.html', chall_info=selected_chall, num=random.randint(1,2500))

@app.route('/addchall', methods=["POST"])
def addchall():
    title = request.form['title']
    category = request.form['category']
    description = request.form['description']
    attachments = request.form['attachments']
    author = request.form['author']
    points = request.form['points']
    difficulty = request.form['difficulty']
    topics = request.form['topics']
    flag = request.form['flag']
    released = request.form['released']
    with open('mychalls.json') as j:
        challs = json.load(j)
    challs.append({'title': title, 'category': category, 'description': description, 'attachments': attachments, 'author': author, 'points': points, 'difficulty': difficulty, 'topics': topics, 'flag': flag, 'released': released})
    with open('mychalls.json', 'w') as j:
        json.dump(challs, j)
    
    challs = (requests.get('https://imaginaryctf.org/api/challenges/released')).json()
    with open('writeups.json') as j:
        current_writeups = json.load(j)
    current_names = []
    solved_names = []
    for chall in challs:
        current_names.append(chall['title'])
    for writeup in current_writeups:
        solved_names.append(writeup['title'])
    for name in solved_names:
        if(name in current_names):
            current_names.remove(name)
    current_names.reverse()
    return render_template("admin/panel.html", navbar="shared/navbar.html", chall_info='', challs=current_names, info=f"{title} successfully added!", num=random.randint(1, 2500))

@app.route('/resetwriteupsjson')
def reset():
    writeups = []
    with open('writeups.json', 'w') as j:
        json.dump(writeups, j)
    return render_template_string("writeups.json reset!")

@app.route('/resetmychalls')
def restmychall():
    writeups = []
    with open('mychalls.json', 'w') as j:
        json.dump(writeups, j)
    return render_template_string("mychalls.json reset!")

@app.route('/projects/chembot/jsongenerator', methods=["POST"])
def addjson():
    category = request.form['category']
    question = request.form['question']
    choice_a = request.form['choice-a']
    choice_b = request.form['choice-b']
    choice_c = request.form['choice-c']
    choice_d = request.form['choice-d']
    choice_e = request.form['choice-e']
    answer = request.form['answer']
    image = request.form['image']
    table = request.form['table']
    calc = request.form['calc']
    form_json = request.form['json']
    table = True if table == "1" else False
    calc = True if calc == "1" else False
    image = 0 if image == "" else image
    form_json = '[]' if form_json == "" else form_json
    real_json = json.loads(form_json)
    next_num = 0 if len(real_json) == 0 else (real_json[-1]['number'] + 1)
    real_json.append({"number": next_num, "category": category, "question": question, "choices": [choice_a, choice_b, choice_c, choice_d, choice_e], "answer": answer, "image": image, "Calc": calc, "Table": table})
    sub_json = json.dumps(real_json)
    print(sub_json)
    return render_template("index-pages/generator.html", projects="active", navbar="shared/navbar.html", sub_json=sub_json, num=random.randint(1, 2500))

app.run(host='0.0.0.0', port=5000)
