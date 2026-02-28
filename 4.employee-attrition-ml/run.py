import threading
import uvicorn
from gradio_app import launch_gradio

def start_fastapi():
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )

if __name__ == "__main__":
    print("🚀 Starting complete ML system (FastAPI + Gradio)")

    # Start FastAPI in background thread
    api_thread = threading.Thread(target=start_fastapi)
    api_thread.start()

    # Start Gradio UI
    launch_gradio()
