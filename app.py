import os
import sys
import logging
from DashPublic import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get port from environment variable or use 8050
try:
    port = int(os.environ.get("PORT", 8000))
except ValueError as e:
    logger.error(f"Invalid port number: {e}")
    sys.exit(1)

if __name__ == '__main__':
    try:
        logger.info(f"Starting server on port {port}")
        app.run_server(
            debug=False,
            host='0.0.0.0',
            port=port
        )
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1) 
