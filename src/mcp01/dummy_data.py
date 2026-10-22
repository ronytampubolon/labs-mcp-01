from mcp01.models import Order, OrderStatus

ORDERS: list[Order] = [
    Order(id=1, order_no="ORD-0001", amount=1250.00, customer="Andi Pratama", status=OrderStatus.COMPLETED),
    Order(id=2, order_no="ORD-0002", amount=349.90, customer="Budi Santoso", status=OrderStatus.PAID),
    Order(id=3, order_no="ORD-0003", amount=89.50, customer="Citra Lestari", status=OrderStatus.PENDING),
    Order(id=4, order_no="ORD-0004", amount=2100.00, customer="Dewi Anggraini", status=OrderStatus.SHIPPED),
    Order(id=5, order_no="ORD-0005", amount=560.75, customer="Eko Wijaya", status=OrderStatus.COMPLETED),
    Order(id=6, order_no="ORD-0006", amount=75.20, customer="Fajar Nugroho", status=OrderStatus.CANCEL),
    Order(id=7, order_no="ORD-0007", amount=1899.99, customer="Gita Permata", status=OrderStatus.PAID),
    Order(id=8, order_no="ORD-0008", amount=430.00, customer="Hendra Gunawan", status=OrderStatus.SHIPPED),
    Order(id=9, order_no="ORD-0009", amount=129.99, customer="Indah Sari", status=OrderStatus.COMPLETED),
    Order(id=10, order_no="ORD-0010", amount=999.00, customer="Joko Susilo", status=OrderStatus.PENDING),
    Order(id=11, order_no="ORD-0011", amount=2450.50, customer="Kartika Dewi", status=OrderStatus.PAID),
    Order(id=12, order_no="ORD-0012", amount=320.00, customer="Lukman Hakim", status=OrderStatus.COMPLETED),
    Order(id=13, order_no="ORD-0013", amount=145.75, customer="Maya Kirana", status=OrderStatus.SHIPPED),
    Order(id=14, order_no="ORD-0014", amount=78.30, customer="Nanda Putra", status=OrderStatus.CANCEL),
    Order(id=15, order_no="ORD-0015", amount=1575.00, customer="Oscar Simbolon", status=OrderStatus.PENDING),
    Order(id=16, order_no="ORD-0016", amount=640.40, customer="Putri Ayu", status=OrderStatus.COMPLETED),
    Order(id=17, order_no="ORD-0017", amount=289.99, customer="Rizky Ramadhan", status=OrderStatus.PAID),
    Order(id=18, order_no="ORD-0018", amount=1120.00, customer="Sinta Maharani", status=OrderStatus.SHIPPED),
    Order(id=19, order_no="ORD-0019", amount=95.60, customer="Taufik Hidayat", status=OrderStatus.PENDING),
    Order(id=20, order_no="ORD-0020", amount=3800.00, customer="Umi Kalsum", status=OrderStatus.PAID),
]
