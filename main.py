from fastapi import FastAPI
import time
import hashlib

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI server is running!"}

@app.get("/heavy")
def heavy_task():
    """Simulate a CPU-intensive task"""
    time.sleep(5)  # Simulates a slow response
    return {"message": "This request was slow!"}

@app.get("/no-rate-limit")
def no_rate_limit():
    """Endpoint with no rate limiting"""
    return {"message": "This endpoint has no rate limiting!"}

@app.get("/cpu-intensive")
def cpu_intensive():
    """Endpoint with a computationally expensive task"""
    for _ in range(1000000):
        hashlib.sha256(b"some random data").hexdigest()
    return {"message": "This request was CPU intensive!"}

@app.get("/large-file")
def large_file():
    """Endpoint serving a large file"""
    return {"file": "A" * 10**6}  # 1 MB of 'A's

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
