# from your_cli_module import process_command  # Import your CLI app's processing function
from fastapi import FastAPI
from utils import *  # example utility import
from db import *  # example database access import

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Example of integrating your existing game logic
@app.post("/play")
def play_game(move: str):
    # Incorporate your game logic here
    # result = some_util_function(move)
    return {"result": "Hello World! this is a test."}

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import sys
# from io import StringIO

# app = FastAPI()

# class Command(BaseModel):
#     command: str

# @app.post("/run")
# async def run_cli(command: Command):
#     # Redirect stdout to capture output
#     sys.stdout = output = StringIO()
#     try:
#         process_command(command.command)  # Run your CLI command function
#     finally:
#         sys.stdout = sys.__stdout__
    
#     return {"result": output.getvalue()}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
