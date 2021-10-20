from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nama']
        return redirect(url_for('main', nama = user))
    return render_template('login.html')

@app.route("/login/main")
def main():
    return render_template('main.html')

@app.route("/login/main/profile_group")
def profile():
    return render_template('profile.html')

@app.route("/login/main/application")
def application():
    return render_template('application.html')

@app.route("/login/main/application/simple_calculator", methods=['POST','GET'])
def calculator():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        if request.form['op'] == '+':
            hasil = n1 + n2
            op = '+'
        elif request.form['op'] == '-':
            hasil = n1 - n2
            op ='-'
        elif request.form['op'] == 'x':
            hasil = n1 * n2
            op = 'x'
        elif request.form['op'] == '/':
            hasil = n1 / n2
            op = '/'
        elif request.form['op'] == '//':
            hasil = n1 // n2
            op = '//'
        return render_template('result.html',n1= n1,n2= n2,op= op, hasil=hasil)
    return render_template('calculator.html')

 

@app.route("/login/main/application/adventure_game")
def game():
    return render_template('tahun_kabisat.py')

@app.route("/logout")
def logout():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
