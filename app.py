
from flask import Flask, render_template
import pandas as pd
import cleandata
from cleandata import * #import all funcs from cleandata.py

app = Flask(__name__)

df = cleandata.data
df_dict = df.to_dict('records')

@app.route('/')
def welcome():
    return render_template('index.html')

#no need to loop through anything. all links are available in directory.html (jinja forloop)
@app.route('/directory')
def directory():
    return render_template('directory.html', data = df_dict)

#no need to loop through anything. all links are available in directory.htpython -m pip install Jinja2ml (jinja forloop)
#page_title, image_src, description all come from the same row as link_name. how do i get them through python, tho
@app.route('/<string:link_name>')
def generate_template(link_name):
    if link_name in set(data.link_name):
        template_data = df.loc[df.link_name==link_name].to_dict('records')[0]
        print(template_data)

        return render_template('template.html', data = template_data)
    else:
        return "Template not found"

if __name__ == '__main__':#
    app.run(debug=True)



