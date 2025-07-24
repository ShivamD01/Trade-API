import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyCDbTO7aFtyuq6dS9futfvlcQ-d6DGjlpM"))
async def analyze_sector(sector: str, data: str) -> str:
    model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
    date = datetime.today().strftime("%B %d, %Y")
    prompt = f"""
Generate a markdown report analyzing trade opportunities in the Indian {sector} sector.

**Date:** {date}

Write a detailed, professional report including:
- Executive Summary
- Key Trade Drivers
- Export Opportunities by Product Category
- Market Challenges
- Strategic Recommendations

Focus on real market conditions, trends, and statistics.

You may optionally refer to this text if relevant, but do **not** mention its format or analyze it directly if it’s unclear or off-topic:

\"\"\" 
{data}
\"\"\"

Respond only with the final markdown report, and nothing else.
"""
    convo = model.start_chat()
    response = convo.send_message(prompt)

    # Save to .md file
    filename = f"{sector}_{date}.md"
    filepath = os.path.join("reports", filename)

    os.makedirs("reports", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)
        return response.text
