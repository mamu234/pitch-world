from flask import Flask,render_template

app = Flask(__name__)

posts = [
    {

    'author': 'student',
    'title':'pitches',
    'content':'welcome to pitches',
    'date':'may 10,2022'
    },
    {

    'author': 'student2',
    'title':'pitches',
    'content':'welcome to pitches',
    'date':'may 10,2022'
    },
    {

    'author': 'student3',
    'title':'pitches',
    'content':'welcome to pitches',
    'date':'may 10,2022'
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html',posts = posts)

if __name__ == '__main__':
    app.run(debug = True)