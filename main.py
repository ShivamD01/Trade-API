from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from auth import verify_token
from Fetch_Data import fetch_sector_data
from analysis import analyze_sector
import traceback

app = FastAPI(
    title="Trade Opportunities API",
    description="An AI-powered API that analyzes Indian sector trade data and returns markdown reports.",
    version="1.0.0",
    contact={
        "name": "Shivam Dhargalkar",
        "email": "dharshiva111@gmail.com"
    }
)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)


@app.get(
        "/analyze/{sector}",
    response_class=PlainTextResponse,
    summary="Generate trade report for a sector",
    description="  Accepts a sector name (e.g., 'agriculture', 'pharmaceuticals') and returns a structured markdown report.\n\n"
        "The report is AI-generated using the Google Gemini API, based on real-time market data. "
        "The response is also saved as a `.md` file under the `reports/` folder.",
    tags=["Analysis"]
)
@limiter.limit("5/minute")
async def analyze(sector: str, request: Request, token: str = Depends(verify_token)):
    try:
        raw_data = await fetch_sector_data(sector)
        markdown_report = await analyze_sector(sector, raw_data)
        return markdown_report
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")
