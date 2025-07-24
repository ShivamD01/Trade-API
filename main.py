from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from auth import verify_token
from Fetch_Data import fetch_sector_data
from analysis import analyze_sector
import traceback

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)


@app.get("/analyze/{sector}", response_class=PlainTextResponse)
@limiter.limit("5/minute")
async def analyze(sector: str, request: Request, token: str = Depends(verify_token)):
    try:
        raw_data = await fetch_sector_data(sector)
        markdown_report = await analyze_sector(sector, raw_data)
        return markdown_report
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")
