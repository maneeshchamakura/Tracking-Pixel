from fastapi import FastAPI, Response
import httpx

app = FastAPI()

# Global counter
test_counter = 0

@app.get("/get-image")
async def get_image():
    global test_counter
    test_counter += 1

    image_url = "https://via.placeholder.com/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)

    # Return the image as a response
    return Response(content=response.content, media_type="image/png")

@app.get("/get-counter")
async def get_counter():
    global test_counter
    return {"test": test_counter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
