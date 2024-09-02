import requests
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def get_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
