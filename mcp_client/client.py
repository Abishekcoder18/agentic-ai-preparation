import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["-m", "mcp_server.server"],
)


async def call_tool(session, tool_name, arguments):
    result = await session.call_tool(tool_name, arguments)

    print(f"\n{tool_name}:")
    print(json.dumps(json.loads(result.content[0].text), indent=2))


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("\nAvailable MCP Tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            print("\n========== TOOL TESTS ==========")

            await call_tool(
                session,
                "track_order",
                {"order_id": "ORD1001"},
            )

            await call_tool(
                session,
                "track_order",
                {"order_id": "ORD9999"},
            )

            await call_tool(
                session,
                "check_stock",
                {"product_id": "P100"},
            )

            await call_tool(
                session,
                "check_stock",
                {"product_id": "P999"},
            )

            await call_tool(
                session,
                "initiate_return",
                {"order_id": "ORD1002"},
            )

            await call_tool(
                session,
                "initiate_return",
                {"order_id": "ORD1003"},
            )


if __name__ == "__main__":
    asyncio.run(main())