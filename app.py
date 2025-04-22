# app.py
from flask import Flask, render_template

# Vytvoření instance aplikace
app = Flask(__name__)

# Definování základní cesty
@app.route('/')
def home():
    return render_template('index.html')

# Spuštění aplikace
if __name__ == '__main__':
    app.run(debug=True)
