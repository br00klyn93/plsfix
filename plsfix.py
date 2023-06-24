from flask import Flask, request, render_template, redirect
from flask import make_response, Response
import json

app = Flask(__name__)

f = open('prompts.json')
p = json.load(f)

@app.route('/')
def main():
    print("All working!")
    return render_template('index.html')

@app.route('/getFix')
def getFix():
    print(p['prompts'][-1])
    return(p['prompts'][-1])
    
    

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
