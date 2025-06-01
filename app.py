# app.py
import multiprocessing
import subprocess
import uvicorn
from api import app as fastapi_app

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

def run_streamlit():
    subprocess.run(["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=127.0.0.1"])

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_fastapi)
    p2 = multiprocessing.Process(target=run_streamlit)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
