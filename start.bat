@echo off
title NexusCommerce AI Server
echo ========================================================
echo   NexusCommerce AI - Autonomous PayPal Agentic Platform
echo ========================================================
echo Starting FastAPI Web Server at http://localhost:8000 ...
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
pause

