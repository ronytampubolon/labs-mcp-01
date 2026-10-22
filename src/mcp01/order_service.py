from typing import Any

from mcp01.dummy_data import ORDERS
from mcp01.models import OrderStatus


def track_order(order_no: str) -> dict[str, Any]:
    """Look up a single order by its order number.

    Args:
        order_no: Order number to look up, e.g. "ORD-0007".
    """
    normalized = order_no.strip().upper()
    for order in ORDERS:
        if order.order_no == normalized:
            return {"found": True, "order": order.model_dump(mode="json")}

    return {
        "found": False,
        "order_no": order_no,
        "message": f"No order found with order number '{order_no}'.",
    }


def monitor_status(status: str) -> dict[str, Any]:
    """Count how many orders are currently in the given status.

    Args:
        status: One of PENDING, PAID, SHIPPED, COMPLETED, CANCEL.
    """
    try:
        target = OrderStatus(status.strip().upper())
    except ValueError:
        allowed = ", ".join(item.value for item in OrderStatus)
        return {
            "status": status,
            "count": 0,
            "message": f"Invalid status '{status}'. Allowed values: {allowed}.",
        }

    count = sum(1 for order in ORDERS if order.status is target)
    return {
        "status": target.value,
        "count": count,
        "total_orders": len(ORDERS),
    }
