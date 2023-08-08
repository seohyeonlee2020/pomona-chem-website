import csv
from flask import Flask, render_template
import pandas as pd
import sqlite3
from cleandata import * #import all funcs from cleandata.py

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

file_path = 'data/robbins_speakers.csv'
data = pd.read_csv(file_path)

# Define a single function for generating templates
@app.route('/row/<int:index>')
def generate_template(index):
    if 0 <= index < len(data):
        template_name = 'row_{}.html'.format(index)
        row = data.iloc[index].to_dict()
        return render_template(template_name, row=row)
    else:
        return "Invalid row index."

if __name__ == '__main__':
    app.run(debug=False)
