from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FoodExpress API", version="1.0.0")

# ---------- In-memory "database" ----------
orders = [
    {"id": 1, "customer": "Alice",   "item": "Burger",   "quantity": 2, "status": "pending"},
    {"id": 2, "customer": "Bob",     "item": "Pizza",    "quantity": 1, "status": "delivered"},
    {"id": 3, "customer": "Charlie", "item": "Sushi",    "quantity": 3, "status": "preparing"},
]
next_id = 4


# ---------- Request body schema ----------
class OrderCreate(BaseModel):
    customer: str
    item: str
    quantity: int
    status: Optional[str] = "pending"


class OrderUpdate(BaseModel):
    customer: Optional[str] = None
    item: Optional[str] = None
    quantity: Optional[int] = None
    status: Optional[str] = None


# ---------- Routes ----------

@app.get("/")
def root():
    return {"message": "Welcome to FoodExpress API", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# GET all orders
@app.get("/orders")
def get_orders():
    return {"orders": orders, "total": len(orders)}


# GET single order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order


# POST create new order
@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    global next_id
    new_order = {"id": next_id, **order.dict()}
    orders.append(new_order)
    next_id += 1
    return {"message": "Order created successfully", "order": new_order}


# # PUT update an existing order
# @app.put("/orders/{order_id}")
# def update_order(order_id: int, order_update: OrderUpdate):
#     order = next((o for o in orders if o["id"] == order_id), None)
#     if not order:
#         raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
#     for field, value in order_update.dict(exclude_none=True).items():
#         order[field] = value
#     return {"message": "Order updated successfully", "order": order}


# # DELETE an order
# @app.delete("/orders/{order_id}")
# def delete_order(order_id: int):
#     order = next((o for o in orders if o["id"] == order_id), None)
#     if not order:
#         raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
#     orders.remove(order)
#     return {"message": f"Order {order_id} deleted successfully"}
