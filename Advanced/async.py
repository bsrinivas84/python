import asyncio

import aiohttp


URLS = [
	"https://jsonplaceholder.typicode.com/todos/1",
	"https://jsonplaceholder.typicode.com/todos/2",
	"https://jsonplaceholder.typicode.com/todos/3",
]


async def fetch_todo(session: aiohttp.ClientSession, url: str) -> dict:
	"""Fetch one JSON payload from an API endpoint."""
	async with session.get(url) as response:
		response.raise_for_status()
		payload = await response.json()
		return {
			"url": url,
			"title": payload.get("title", ""),
			"completed": payload.get("completed", False),
			"ok": True,
		}


async def stream_todos(session: aiohttp.ClientSession, urls: list[str]):
	"""Async generator that yields each result as soon as it is available."""
	tasks = [asyncio.create_task(fetch_todo(session, url)) for url in urls]

	for task in asyncio.as_completed(tasks):
		try:
			result = await task
			yield result
		except Exception as exc:
			yield {"ok": False, "error": str(exc)}


async def main():
	timeout = aiohttp.ClientTimeout(total=10)

	async with aiohttp.ClientSession(timeout=timeout) as session:
		async for item in stream_todos(session, URLS):
			if item["ok"]:
				print(f"Title: {item['title']} | Completed: {item['completed']}")
			else:
				print(f"Request failed: {item['error']}")


if __name__ == "__main__":
	asyncio.run(main())
