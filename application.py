"""
This script runs the FlaskWebProject application using Azure App Service.
"""

import os
from FlaskWebProject import app

if __name__ == "__main__":
    # Use Azure's assigned port and bind to all interfaces
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
