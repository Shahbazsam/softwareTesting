from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/reverse', methods=['POST'])
def reverse_integer():
    """Handles the reverse integer request."""
    try:
        x = int(request.form.get('integer'))
        result = Solution().reverse(x)
        return render_template('index.html', result=result, integer=x)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a valid integer.", integer=x)

if __name__ == '__main__':
    app.run(debug=True)