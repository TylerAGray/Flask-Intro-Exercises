from flask import Flask, request
from operations import add, sub, mult, div

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b parameters from the query string and return the result."""
    a = int(request.args.get('a'))  # Get the 'a' parameter from the query string and convert it to an integer
    b = int(request.args.get('b'))  # Get the 'b' parameter from the query string and convert it to an integer
    result = add(a, b)  # Call the add function from operations.py
    return str(result), 200  # Return the result as a string with a 200 OK status

@app.route('/sub')
def do_sub():
    """Subtract b from a parameters from the query string and return the result."""
    a = int(request.args.get('a'))  # Get the 'a' parameter from the query string and convert it to an integer
    b = int(request.args.get('b'))  # Get the 'b' parameter from the query string and convert it to an integer
    result = sub(a, b)  # Call the sub function from operations.py
    return str(result), 200  # Return the result as a string with a 200 OK status

@app.route('/mult')
def do_mult():
    """Multiply a and b parameters from the query string and return the result."""
    a = int(request.args.get('a'))  # Get the 'a' parameter from the query string and convert it to an integer
    b = int(request.args.get('b'))  # Get the 'b' parameter from the query string and convert it to an integer
    result = mult(a, b)  # Call the mult function from operations.py
    return str(result), 200  # Return the result as a string with a 200 OK status

@app.route('/div')
def do_div():
    """Divide a by b parameters from the query string and return the result."""
    a = int(request.args.get('a'))  # Get the 'a' parameter from the query string and convert it to an integer
    b = int(request.args.get('b'))  # Get the 'b' parameter from the query string and convert it to an integer
    result = div(a, b)  # Call the div function from operations.py
    return str(result), 200  # Return the result as a string with a 200 OK status

@app.route('/math/<operation>')
def do_math(operation):
    """
    Perform the specified operation (add, sub, mult, div) on a and b parameters from the query string.
    Return the result.
    """
    a = int(request.args.get('a'))  # Get the 'a' parameter from the query string and convert it to an integer
    b = int(request.args.get('b'))  # Get the 'b' parameter from the query string and convert it to an integer
    
    # Determine which operation to perform based on the operation parameter
    if operation == 'add':
        result = add(a, b)  # Call the add function from operations.py
    elif operation == 'sub':
        result = sub(a, b)  # Call the sub function from operations.py
    elif operation == 'mult':
        result = mult(a, b)  # Call the mult function from operations.py
    elif operation == 'div':
        result = div(a, b)  # Call the div function from operations.py
    else:
        return "Invalid operation", 400  # Return a 400 Bad Request status if the operation is invalid
    
    return str(result), 200  # Return the result as a string with a 200 OK status

# Run the application in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
