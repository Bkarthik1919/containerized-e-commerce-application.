# Containerized E-Commerce Application
A simple Flask REST API with product catalogue, in-memory cart, and order creation.

## Run
`docker compose up --build -d`
Open http://localhost:5004

## API
`GET /api/products`
`POST /api/cart` JSON: `{"product_id":1,"quantity":2}`
`GET /api/cart`
`POST /api/orders`

This is a learning demo only: cart and orders reset when the container restarts. No authentication or payment processing is included. Do not use for real transactions.
