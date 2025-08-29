from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

PROMPTS = [
    {
        'id' : 1,
        'prompt' : 'Your all-time favourite song'
    },
    {
        'id' : 2,
        'prompt' : 'Your guilty pleasure'
    },
    {
        'id' : 3,
        'prompt' : 'Makes you cry everytime'
    },
    {
        'id' : 4,
        'prompt' : 'Great song, not-so-great artist'
    },
    {
        'id' : 5,
        'prompt' : 'Reminds you of your ex'
    },
]

PLAYER1NAME = 'ApplestoApples'
PLAYER2NAME = 'BananasforMonkeys'
# Basic route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/start')
def start():
    return render_template('start.html', player1name=PLAYER1NAME, player2name=PLAYER2NAME)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/prompt')
def prompt():
    return render_template('prompt.html', prompts=PROMPTS, player1name=PLAYER1NAME, player2name=PLAYER2NAME)

@app.route('/selection')
def selection():
    return render_template('selection.html', player1name=PLAYER1NAME, player2name=PLAYER2NAME)

@app.route('/sessend')
def sessend():
    return render_template('sessend.html', player1name=PLAYER1NAME, player2name=PLAYER2NAME)

@app.route('/sharing')
def sharing():
    return render_template('sharing.html', player1name=PLAYER1NAME, player2name=PLAYER2NAME)

@app.route('/waiting')
def waiting():
    return render_template('waiting.html')

if __name__ == '__main__':
    # Configure for Replit environment
    # Use 0.0.0.0 to bind to all interfaces (required for Replit)
    # Enable debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)