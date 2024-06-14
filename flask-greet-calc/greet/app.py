from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """
    Define a route for '/welcome'.
    
    This function handles requests to the '/welcome' URL and returns a 
    welcome message with a 200 OK status.
    """
    return 'Welcome', 200  # Return 'Welcome' message with a 200 OK status

@app.route('/welcome/home')
def welcome_home():
    """
    Define a route for '/welcome/home'.
    
    This function handles requests to the '/welcome/home' URL and returns a 
    welcome home message with a 200 OK status.
    """
    return 'Welcome home', 200  # Return 'Welcome home' message with a 200 OK status

@app.route('/welcome/back')
def welcome_back():
    """
    Define a route for '/welcome/back'.
    
    This function handles requests to the '/welcome/back' URL and returns a 
    welcome back message with a 200 OK status.
    """
    return 'Welcome back', 200  # Return 'Welcome back' message with a 200 OK status

# Run the application in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
