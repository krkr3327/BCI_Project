"""
Main entry point for the Python backend application.
"""
from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="My Python App",
    description="Backend API for My Python App",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "Backend is running!"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    
    # Read host and port from environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    
    uvicorn.run(app, host=host, port=port)
