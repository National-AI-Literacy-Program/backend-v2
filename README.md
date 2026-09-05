Steps to run the backend
    1.Copy the .env.example into .env and add the postgresql url
    2.Run these following commands to locally rnu the backend
        uv sync
        uv run uvicorn src.main:app --reload
