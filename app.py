from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Flask Practice App</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    max-width: 800px; 
                    margin: 50px auto; 
                    padding: 20px;
                    text-align: center;
                }
                h1 { color: #333; }
                p { color: #666; line-height: 1.6; }
            </style>
        </head>
        <body>
            <h1>Welcome to Flask Practice!</h1>
            <p>This is a learning project based on the FreeCodeCamp Flask tutorial.</p>
            <p>The Flask web application is now running successfully in the Replit environment!</p>
        </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <html>
        <head>
            <title>About - Flask Practice App</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    max-width: 800px; 
                    margin: 50px auto; 
                    padding: 20px;
                }
                h1 { color: #333; }
                p { color: #666; line-height: 1.6; }
                a { color: #007bff; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>About This Project</h1>
            <p>This Flask practice application is designed to build foundational skills in Python web development.</p>
            <p>Features:</p>
            <ul>
                <li>Route-based architecture using Flask decorators</li>
                <li>Template rendering with dynamic content</li>
                <li>Clean, educational code structure</li>
            </ul>
            <p><a href="/">← Back to Home</a></p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Configure for Replit environment
    # Use 0.0.0.0 to bind to all interfaces (required for Replit)
    # Enable debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)