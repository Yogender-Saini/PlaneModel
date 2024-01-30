from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the model page
@app.route('/model')
def model():
    return render_template('model.html')

# Route for the unknown page
@app.route('/unknown')
def unknown():
    return render_template('unknown.html')

if __name__ == '__main__':
    app.run(debug=True)
