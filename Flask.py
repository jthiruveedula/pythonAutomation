from flask import Flask

app= Flask(__name__)
@app.route('/')
def home():
    return "Welcome to python Flask page"

@app.route('/about/')
def about():
    return "Welcome to python about page"

if __name__=="__main__":
    app.run(debug=True)