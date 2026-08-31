import json
from mcp.server import MCPServer

from mcp_server.database import (
    get_order,
    get_product,
    add_return,
    load_data,
)
from mcp_server.audit import log_tool_call


mcp = MCPServer("E-Commerce Order MCP Server")


@mcp.tool()
def track_order(order_id: str) -> dict:
    """Track the current status of an e-commerce order."""

    log_tool_call("track_order", {"order_id": order_id})

    order = get_order(order_id)

    if order is None:
        return {
            "success": False,
            "error": f"Order '{order_id}' not found."
        }

    return {
        "success": True,
        "order_id": order["order_id"],
        "status": order["status"]
    }


@mcp.tool()
def check_stock(product_id: str) -> dict:
    """Check the available stock for a product."""

    log_tool_call("check_stock", {"product_id": product_id})

    product = get_product(product_id)

    if product is None:
        return {
            "success": False,
            "error": f"Product '{product_id}' not found."
        }

    return {
        "success": True,
        "product_id": product["product_id"],
        "product_name": product["name"],
        "stock": product["stock"]
    }


@mcp.tool()
def initiate_return(order_id: str) -> dict:
    """Initiate a return for an eligible e-commerce order."""

    log_tool_call("initiate_return", {"order_id": order_id})

    success, message = add_return(order_id)

    if not success:
        return {
            "success": False,
            "error": message
        }

    return {
        "success": True,
        "order_id": order_id,
        "message": message
    }


@mcp.resource("orders://recent")
def recent_orders() -> str:
    """Return the recent e-commerce orders."""

    data = load_data()

    recent = data["orders"][-5:]

    return json.dumps(recent, indent=2)


if __name__ == "__main__":
    mcp.run()