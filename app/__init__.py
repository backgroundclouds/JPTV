from flask import Flask, render_template
import yaml
import os

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    
    # Enable caching for static files
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600  # Cache for 1 hour

    # Enable compression if possible
    app.config['COMPRESS_MIMETYPES'] = ['text/html', 'text/css', 'application/json', 'application/javascript', 'image/png', 'image/jpeg', 'video/mp4']
    app.config['COMPRESS_LEVEL'] = 6
    

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

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)




# if __name__ == '__main__':
#     app.run(debug=True)

