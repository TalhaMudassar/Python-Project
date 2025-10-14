from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello to python learner from talha mudassar "


@app.route('/about')
def about_page():
    return 'This is about page '

if __name__ == '__main__':
    app.run(debug=True)
    
    