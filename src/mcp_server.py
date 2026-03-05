import asyncio
from mcp import Tool
from mcp.server import Server
from mcp.types import TextContent, PromptMessage
from activities import activities

server = Server("activity-server")

@server.tool()
async def get_activities() -> str:
    """Get the list of all activities with their details."""
    return str(activities)

if __name__ == "__main__":
    import mcp.server.stdio
    mcp.server.stdio.run_server(server)