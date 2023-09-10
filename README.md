# Create an Endpoint

This is the first task for HNG Internship. To create an endpoint using any language of choice. The endpoint should accept two GET request query parameters and return specific information in JSON format.

## API Reference

#### Get the data

```https
  GET /api
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `slack_name` | `string` | **Required**.|
| `track` | `string` | **Required**. |

## Deployment

To deploy this project run

```zsh
  uvicorn main:app --reload
```

## Sample

```JSON
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
```

## Installation

Clone this repo, then

```zsh
  cd student_API
  python3 -m venv env
  source venv/bin/activate
  pip install -r requirements.txt
```
