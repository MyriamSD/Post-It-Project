import datetime
from flask import Flask, render_template

app = Flask(__name__)



notes = [{'title': 'Note One',
             'content': 'Note One Content'},
            {'title': 'Note Two',
             'content': 'Note Two Content'}
            ]
# Would like to add am id

@app.route("/")
def index():
    return render_template('index.html', notes=notes)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)

# What my app needs:

# To be able to write a note and save it and then retrieve it and delete it.

# first: retrieve user data
    
# a place that stores the notes
# a textbox that collects the notes
# a funtion to retrieve the notes that were previously written