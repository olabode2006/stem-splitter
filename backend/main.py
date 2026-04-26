from fastapi import FastAPI, File, UploadFile
from separator import separate

# create the fastapi app instance
app = FastAPI()

# GET endpoint — confirms the server is running
@app.get("/")
def read_root():
    return {"message" : "Stem Splitter API is running!"}

# POST endpoint — accepts an audio file upload
@app.post("/upload")
async def upload(file: UploadFile):
    # read the raw bytes of the uploaded file
    contents = await file.read()
    
    # open a new file in the uploads folder and write the bytes to it
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)

    print(f"Starting separation for {file.filename}")
    output_path = separate(file.filename)
    print(f"Separation complete: {output_path}")

    #seperate the file into stem using the function made in seperator.py
    output_path = separate(file.filename)
    
    # return the filename to confirm it was received
    return {"filename" : file.filename, "output_path" : output_path}
