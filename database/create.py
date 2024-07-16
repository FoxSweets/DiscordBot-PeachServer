import aiosqlite
import asyncio


async def create_db():
	async with aiosqlite.connect("database/data.db") as db:
		cursor = await db.cursor()

		query = """
		CREATE TABLE IF NOT EXISTS "users" (
			"id"	INTEGER,
			"name"	TEXT
		)
		"""

		await cursor.executescript(query)
		await db.commit()