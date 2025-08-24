#!/usr/bin/env python3
"""
Startskript für den Orientierungsfahrt Server
"""

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
