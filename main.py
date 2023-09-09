from fastapi import FastAPI

app = FastAPI()

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