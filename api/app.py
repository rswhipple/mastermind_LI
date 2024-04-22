from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
from io import StringIO
from your_cli_module import process_command  # Import your CLI app's processing function

app = FastAPI()

class Command(BaseModel):
    command: str

@app.post("/run")
async def run_cli(command: Command):
    # Redirect stdout to capture output
    sys.stdout = output = StringIO()
    try:
        process_command(command.command)  # Run your CLI command function
    finally:
        sys.stdout = sys.__stdout__
    
    return {"result": output.getvalue()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
