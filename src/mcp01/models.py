from enum import Enum

from pydantic import BaseModel


class OrderStatus(str, Enum):
    """Lifecycle states an order can be in."""

    PENDING = "PENDING"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    COMPLETED = "COMPLETED"
    CANCEL = "CANCEL"


class Order(BaseModel):
    """A single customer order."""

    id: int
    order_no: str
    amount: float
    customer: str
    status: OrderStatus
