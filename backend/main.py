# import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


# if __name__ == "__main__":
# print("Starting server on http://0.0.0.0:8003")
# uvicorn.run(app, host="0.0.0.0", port=8003)
