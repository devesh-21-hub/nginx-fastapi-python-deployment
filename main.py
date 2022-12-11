from fastapi import FastAPI
import threading
import time

# Instantiate the class
app = FastAPI()
funtions={"start":False}
count = 0
# Define a GET method on the specified endpoint

def main_function():
    global count
    while funtions["start"]:
        time.sleep(3)
        count+=1
        print(count)

    return 


@app.get("/start")
async def start_function():
    funtions["start"]=True
    main_function()
    return {"msg":" program started"}


@app.get("/isProgramRunning")
def check_status():
    if funtions["start"]:
        return {"msg":"Running"}
    else:
        return {"msg":"Not running"}

@app.get("/stop")
def stop_function():
    funtions["start"]=False
    return {"msg":" program stopped"}

@app.get("/")
def hello():
    return {"result": "Welcome to FastAPI"}
