import httpx

async def fetch_sector_data(sector: str) -> str:
    url = f"https://api.duckduckgo.com/?q={sector}+sector+India&format=json"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        if res.status_code != 200:
            raise Exception("Failed to fetch data")
        return res.text
