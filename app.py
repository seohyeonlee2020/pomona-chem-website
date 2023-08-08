import csv
from flask import Flask, render_template

app = Flask(__name__)

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/data')
def data():
    data = read_csv('data.csv')  # Replace with your CSV file path
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
