from flask import Flask, render_template
import yaml
import os

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    
    # Enable caching for static files
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600  # Cache for 1 hour
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 604800  # Cache static files for 1 week


    # Load data from YAML file
    with open('data/projects.yaml', 'r') as file:
        projects = yaml.safe_load(file)

    @app.route('/')
    def index():

        return render_template('index.html', projects=projects)

    @app.route('/about')
    def about():
        return render_template('about.html')
    

    return app

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)