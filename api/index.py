"""
Vercel serverless entry-point.
Vercel's @vercel/python builder looks for a module-level `app` (ASGI)
inside every file under /api/.  We simply re-export the FastAPI app that
lives in backend/main.py so that all routes stay in one place.
"""
import sys
import os

# Make sure Python can resolve `backend.*` imports from the project root.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from backend.main import app  # noqa: F401  – Vercel needs this name
