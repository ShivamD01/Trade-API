# Trade Opportunities API

An AI-powered FastAPI service that analyzes market data and generates structured markdown reports on trade opportunities for various sectors in India. Uses Google Gemini to deliver rich, insightful summaries, and saves them as `.md` files.


## Features

- FastAPI backend with async support
- Token-based authentication
- Per-user rate limiting (5 requests/minute)
- Market data fetched from DuckDuckGo API
- AI-powered report generation using Google Gemini
- Report auto-saved as `.md` files (e.g., `reports/agriculture_20250723_190000.md`)
- Secure `.env` environment setup

## Project Structure

main.py # FastAPI app entry point
auth.py # Token validation
Fetch_Data.py # Sector data fetching logic
analysis.py # Gemini AI integration & markdown saving
.env.example # Environment variable template
requirements.txt # Dependencies
README.md # Project documentation
reports/ # Output markdown reports (.md)


## Setup Instructions

### 1. Clone the Repository

git clone <repo-url>
cd trade_api
### 2. Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Create .env File
add your Google Gemini API key:
# .env
GEMINI_API_KEY=your_actual_gemini_api_key_here

Run the App
uvicorn main:app --reload

### API Usage
# I used Postman to test the API endpoints. You can use any HTTP client of your choice.
Endpoint: /analyze/{sector}
Method: GET

Path Param: sector (e.g., agriculture, technology, pharmaceuticals)

Header Required:
Authorization: Bearer test-token
Example Request (Curl)
curl -H "Authorization: Bearer test-token" http://localhost:5000/analyze/agriculture

### Response
Returns: Markdown-formatted market analysis
Also saves the report to: reports/agriculture_YYYYMMDD_HHMMSS.md

### Technologies Used
1. FastAPI (Backend)
2. httpx (Async data fetch)
3. Google Gemini (via google-generativeai) (AI integration)
4. slowapi (Rate limiting)
5. dotenv (Environment variable management)

# Security Note
Do not share your .env file or API keys.
Only include .env.example for submission or upload.

### Contact
### Developed by Shivam Dhargalkar
### For technical assignment purposes (AI + FastAPI Developer Role)

