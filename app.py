import csv
from flask import Flask, render_template
import pandas as pd
from cleandata import * #import all funcs from cleandata.py
import jinja2
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

file_path = 'data/robbins_speakers.csv'
data = pd.read_csv(file_path)

@app.route('/')
def welcome():
    return render_template('index.html')

#no need to loop through anything. all links are available in directory.html (jinja forloop)
@app.route('/directory')
def directory(data):
    return render_template('directory.html', data = data)

#no need to loop through anything. all links are available in directory.htpython -m pip install Jinja2ml (jinja forloop)
#page_title, image_src, description all come from the same row as link_name. how do i get them through python, tho
@app.route('/<link_name>')
def generate_template(link_name, page_title, image_src, description):
    template_name = '{}.html'.format(link_name)
    return render_template(template_name, page_title = page_title, image_src = image_src, description = description)




if __name__ == '__main__':
    app.run(debug=False)
