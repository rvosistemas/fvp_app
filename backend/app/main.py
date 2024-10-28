from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import fund_routes, transaction_routes, subscription_routes

app = FastAPI()

app.include_router(fund_routes.router)
app.include_router(transaction_routes.router)
app.include_router(subscription_routes.router)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
