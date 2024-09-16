import asyncio

import uvicorn

from src.database.manager import db


async def initialize_db():
    await db.setup()


if __name__ == "__main__":
    asyncio.run(initialize_db())
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000)
