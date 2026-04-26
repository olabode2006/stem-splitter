import subprocess #module that helps with running terminal commands

#to actually seperate file into different parts
def separate(filename):
    subprocess.run(["venv/bin/python3", "-m", "demucs", "--out", "outputs/", f"uploads/{filename}"])
    return f"outputs/htdemucs/{filename}"   #returns the path where the stems were saved so main.py knows where to find them.