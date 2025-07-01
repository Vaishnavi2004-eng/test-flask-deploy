from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('home.html')
=======
    return render_template('home.html')
>>>>>>> bd24c4bbedfb82e8e11d5e269760a8d785d1a39e
