"""
Cloud Run Hackathon Server - Ready to Deploy!

This server runs your hackathon agent on Cloud Run.
"""

import os
import logging
import uvicorn
from agent import app

# Configure logging for Cloud Run
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    logging.info(f"Starting Cloud Run Hackathon Agent on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port) 