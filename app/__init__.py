from flask import Flask, render_template
import yaml
import os

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Load data from YAML file
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
    
    return app



# if __name__ == '__main__':
#     app.run(debug=True)

