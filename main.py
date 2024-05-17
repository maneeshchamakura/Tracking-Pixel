from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Global counter
test_counter = 0

@app.get("/get-image")
async def get_image():
    global test_counter
    test_counter += 1

    image_path = "local_image.png"

    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    else:
        return Response(content="Image not found", media_type="text/plain", status_code=404)

@app.get("/get-counter")
async def get_counter():
    global test_counter
    return {"test": test_counter}

@app.get("/reset-counter")
async def get_counter():
    global test_counter
    test_counter = 0
    return {"reset": test_counter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
