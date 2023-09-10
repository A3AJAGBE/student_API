import json
from datetime import datetime
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/api")
def student_lookup(slack_name: str, track: str, res: Response):
    res.status_code = 200
    current_day = datetime.today().strftime('%A')
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    status_code = res.status_code
    
    data = {
        "slack_name": "a3ajagbe",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": "backend",
        "github_file_url": "https://github.com/A3AJAGBE/student_API/blob/main/main.py",
        "github_repo_url": "https://github.com/A3AJAGBE/student_API",
        "status_code": status_code
    }
    
    if (data["slack_name"] == slack_name) and (data["track"] == track):
        return data
    else:
        res.status_code = 404
        return "Wrong slack name or track!!!"