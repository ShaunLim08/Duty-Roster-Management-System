@echo off
start cmd /k "cd backend && pip install -r requirements.txt && uvicorn main:app --reload"
start cmd /k "cd frontend && npm install && npm run dev"
echo System is starting...
echo Backend will run on http://localhost:8000
echo Frontend will run on http://localhost:5173
pause
