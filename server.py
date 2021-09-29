from flask import Flask, render_template, session, redirect, request

app = Flask (__name__)
app.secret_key = 'secret2021'

@app.route('/', methods=['GET'])
def index():
    print(session)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def route():
    print (request.form)
    session['fullname'] = request.form['fullname']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print (session)
    return redirect('/result')

@app.route('/result', methods=['GET'])
def result():
    return render_template('results.html')

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)