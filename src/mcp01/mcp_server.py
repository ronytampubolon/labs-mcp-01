from typing import Any

from fastmcp import FastMCP

from mcp01 import order_service

mcp = FastMCP("My MCP Server 01")

@mcp.tool
def greet(name:str) -> str:
    return f"Hello {name}!"

@mcp.tool
def track_order(order_no: str) -> dict[str, Any]:
    """Look up a single order by its order number."""
    return order_service.track_order(order_no)


@mcp.tool
def monitor_status(status: str) -> dict[str, Any]:
    """Count how many orders are currently in the given status."""
    return order_service.monitor_status(status)

if __name__ == "__main__":
    mcp.run()
