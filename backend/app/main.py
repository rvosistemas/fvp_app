from fastapi import FastAPI
from app.routes import fund_routes, transaction_routes

app = FastAPI()

app.include_router(fund_routes.router)
app.include_router(transaction_routes.router)
