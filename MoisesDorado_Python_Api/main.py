from fastapi import FastAPI
from controller.task_controller import router as task_router

app = FastAPI()

app.include_router(task_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)