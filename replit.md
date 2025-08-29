# Flask Practice Web Application

## Overview

This is a learning project based on a FreeCodeCamp Flask tutorial, designed to build foundational skills in Python web development. The application serves as a practice environment for understanding Flask framework concepts, web application architecture, and full-stack development principles.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Framework
- **Flask**: Chosen as the primary web framework for its simplicity and educational value
- **Python**: Server-side language providing clean syntax ideal for learning web development concepts
- **Development Server**: Flask's built-in development server for local testing and iteration

### Application Structure
- **Minimal Setup**: Following tutorial-driven approach with straightforward file organization
- **Route-based Architecture**: Using Flask's decorator pattern for URL routing and view functions
- **Template Rendering**: Likely implementing Jinja2 templating for dynamic HTML generation

### Development Approach
- **Tutorial-guided Learning**: Architecture decisions follow educational best practices rather than production optimization
- **Incremental Building**: Structure allows for step-by-step feature addition as tutorial progresses
- **Local Development Focus**: Configuration optimized for learning environment rather than deployment

## Recent Changes

### August 29, 2025
- **Initial Setup Complete**: Created basic Flask application structure with app.py
- **Replit Integration**: Configured Flask to work with Replit's proxy environment (host='0.0.0.0')
- **Basic Routes**: Implemented home (/) and about (/about) routes with inline HTML
- **Workflow Configuration**: Set up Flask App workflow running on port 5000
- **Deployment Ready**: Configured autoscale deployment target for production

## Project Structure

```
flask-practice/
├── app.py              # Main Flask application with routes
├── requirements.txt    # Python dependencies
├── replit.md          # Project documentation
└── README.md          # Basic project description
```

## External Dependencies

### Core Dependencies (Installed)
- **Flask 3.1.2**: Primary web framework for handling HTTP requests and responses
- **Jinja2 3.1.6**: Template engine (bundled with Flask) for dynamic content rendering
- **Werkzeug 3.1.3**: WSGI utility library (Flask dependency) for development server
- **Click, Blinker, ItsDangerous, MarkupSafe**: Additional Flask dependencies

### Development Setup
- **Python 3.11**: Server-side language environment
- **Replit Environment**: Configured for proxy compatibility with host='0.0.0.0' and port 5000
- **Debug Mode**: Enabled for development with auto-reload functionality