from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('main.html')
@app.route('/square')
def square():
  return render_template('square.html')
@app.route('/circle')
def circle():
  return render_template('circle.html')
@app.route('/pyramid')
def pyramid():
  return render_template('pyramid.html')



app.run(host='0.0.0.0', port=8020)