import json
from typing import Optional

from datetime import datetime
from fastapi import FastAPI, Response
from pydantic import BaseModel


app = FastAPI()

class Info(BaseModel):
    slack_name: str
    current_day: Optional[str] = None
    utc_time: Optional[datetime] = None
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: Optional[int] = None

Students_data = []


@app.get("/")
def index():
    json_data=open("./students.json").read()
    data = json.loads(json_data)
    return data
 
 
@app.post("/students/add")
def add_student(new_student: Info, res: Response):     
    student = new_student.model_dump()
    res.status_code = 201
    student["current_day"] = datetime.today().strftime('%A')
    student["utc_time"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    student["status_code"] = res.status_code
    
    with open("students.json", "w") as file:
        Students_data.append(student)
        data = {"Students_data": Students_data}
        json.dump(data, file, indent=4)
        return "Student Added successfully"
    

@app.get("/students/student_lookup")
def student_lookup(slack_name: str, track: str, res: Response):
    json_data=open("./students.json").read()
    data = json.loads(json_data)
    Students = data["Students_data"]
    
    all_students = [student for student in Students if  slack_name.lower() in student["slack_name"] and track.lower() in student["track"]]
    
    if not all_students:
        res.status_code = 404
        return {"message": "Student not found."}
    else:
        return all_students if len(all_students) > 1 else all_students[0]
    