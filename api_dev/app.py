from fastapi import FastAPI
from config import RequestModel, ResponseModel 


app = FastAPI() 

@app.get("/")
async def root():
    return {"message": "Welcome to the Eligibility Checker API!"}
@app.post("/check_eligibility", response_model=ResponseModel)
async def check_eligibility(request: RequestModel):
    if request.age >= 18:
        return ResponseModel(message=f"{request.name} is eligible to vote in {request.region}.", status=True)
    else:
        return ResponseModel(message=f"{request.name} is not eligible to vote in {request.region}.", status=False)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.01.0", port=8000)