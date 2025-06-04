from pydantic import BaseModel
from fastapi import FastAPI
from supabase import create_client
from typing import Optional
from dotenv import load_dotenv
import os
from fastapi.encoders import jsonable_encoder
import apiService
import dataService
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Number(BaseModel):
    x: int
    y: int
    
@app.get("/message")
def read_root():
    return {"message": "Hello World"}

@app.post("/add")
def add(number: Number):
    return {"result": number.x + number.y}


@app.post("/create_challengeAll")
async def create_challenge(challengeAll: dataService.ChallengeAll):
    try:  
       
        return await apiService.BuilderDef.create_challengeAll(challengeAll)
            
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.post("/create_reward")
async def create_reward(reward: dataService.Rewards):
    try:       
        return await apiService.BuilderDef.create_reward(reward)
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/get_challenges")
async def get_challenges():
    try:               
        return await apiService.BuilderDef.get_challenges()
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
    
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=7860)