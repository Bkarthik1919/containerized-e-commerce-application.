from flask import Flask,request,jsonify
app=Flask(__name__)
products=[{"id":1,"name":"Laptop","price":55000},{"id":2,"name":"Headphones","price":2500},{"id":3,"name":"Keyboard","price":1800}]
cart={}; orders=[]
@app.get("/")
def home(): return "<h1>Containerized E-Commerce Demo</h1><p>Use /api/products and the cart API.</p>"
@app.get("/health")
def health(): return {"status":"healthy"}
@app.get("/api/products")
def catalogue(): return jsonify(products)
@app.post("/api/cart")
def add():
 d=request.get_json(silent=True) or {}; pid=d.get("product_id"); qty=d.get("quantity",1)
 if not isinstance(qty,int) or qty<1: return {"error":"quantity must be positive integer"},400
 if not any(p["id"]==pid for p in products): return {"error":"product not found"},404
 cart[pid]=cart.get(pid,0)+qty; return jsonify(cart),201
@app.get("/api/cart")
def view():
 items=[{**p,"quantity":cart[p["id"]],"subtotal":p["price"]*cart[p["id"]]} for p in products if p["id"] in cart]
 return {"items":items,"total":sum(x["subtotal"] for x in items)}
@app.post("/api/orders")
def order():
 if not cart: return {"error":"cart empty"},400
 total=sum(p["price"]*cart.get(p["id"],0) for p in products)
 o={"order_id":len(orders)+1,"items":dict(cart),"total":total}; orders.append(o); cart.clear()
 return jsonify(o),201
