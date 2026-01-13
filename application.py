"""
This script runs the FlaskWebProject application locally.
"""

from FlaskWebProject import app

if __name__ == "__main__":
    # For testing locally
    app.run(host="0.0.0.0", port=5555, debug=True)
