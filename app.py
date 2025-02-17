from flask import Flask, render_template
import yaml

app = Flask(__name__)

with open('data/projects.yaml', 'r') as file:
    projects = yaml.safe_load(file)

@app.route('/')
def index():

    
    
    return render_template('index.html', projects=projects)

@app.route('/test_page')
def test_page():
    return render_template('test_page.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_2')
def about2():
    return render_template('about_2.html')


if __name__ == '__main__':
    app.run(debug=True)

