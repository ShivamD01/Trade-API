from fastapi import Header, HTTPException

async def verify_token(authorization: str = Header(None)):
    if authorization != "Bearer test-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
