from flask import Flask, render_template, redirect, url_for, request
import json

app= Flask(__name__)

Start= 0

@app.route('/')
def index():
    # global start
    global Start

    return render_template('index.html', start= Start)

@app.route('/start', methods=['POST', 'GET'])
def start():
    global Start
    Start+= 1

    # Fetching the data from the json.
    with open('questions.json', 'r') as file:
        questions = json.load(file)

    return render_template('index.html', start= Start, questions= questions, status= 'correct')

@app.route('/input', methods=['POST', 'GET'])
def next():
    global Start

    # Getting the user entered value from html.
    user_input = request.form.get('answer')
    print(user_input)

    # Fetching the date from the json.
    with open('questions.json', 'r') as file:
        questions = json.load(file)

    if user_input== questions[Start- 1][-1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
        

    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

if __name__== '__main__':
    app.run(debug = True)
