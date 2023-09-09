from typing import Optional

from datetime import datetime
from fastapi import FastAPI, Response
from pydantic import BaseModel


app = FastAPI()

class Info(BaseModel):
    slack_name: str
    current_day: str
    utc_time: datetime
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: Optional[int] = None

Students = [
    {
        "slack_name": "example_name",
        "current_day": "Monday",
        "utc_time": "2023-08-21T15:04:05Z",
        "track": "backend",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/username/repo",
        "status_code": 200
    },
    {
        "slack_name": "name2",
        "current_day": "Wednesday",
        "utc_time": "2023-09-21T15:04:05Z",
        "track": "frontend",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name2.ext",
        "github_repo_url": "https://github.com/username2/repo",
        "status_code": 200
    },
    {
        "slack_name": "example_name2",
        "current_day": "Tuesday",
        "utc_time": "2023-10-21T15:04:05Z",
        "track": "frontend",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name3.ext",
        "github_repo_url": "https://github.com/username3/repo",
        "status_code": 200
    },
    {
        "slack_name": "example",
        "current_day": "Thursday",
        "utc_time": "2023-07-21T15:04:05Z",
        "track": "frontend",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name4.ext",
        "github_repo_url": "https://github.com/username4/repo",
        "status_code": 200
    },
    {
        "slack_name": "Waau",
        "current_day": "Friday",
        "utc_time": "2023-05-21T15:04:05Z",
        "track": "frontend",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name5.ext",
        "github_repo_url": "https://github.com/username5/repo",
        "status_code": 200
    }
]

@app.get("/")
def index():
    return Students


@app.post("/students/add")
def add_student(new_student: Info, res: Response):         
    student = new_student.dict()
    res.status_code = 201
    student["status_code"] = res.status_code
    Students.append(student)
    return student


@app.get("/students/student_lookup")
def student_lookup(slack_name: str, track: str, res: Response):
    all = [student for student in Students if  slack_name.lower() in student["slack_name"] and track.lower() in student["track"]]
    
    if not all:
        res.status_code = 404
        return {"message": "Student not found."}
    else:
        return all if len(all) > 1 else all[0]
    