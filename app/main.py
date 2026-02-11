from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import api_router

app = FastAPI(title="My API")

# Настройка CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # список разрешённых источников
    allow_credentials=True,     # разрешаем cookies
    allow_methods=["*"],        # разрешаем все HTTP методы
    allow_headers=["*"],        # разрешаем все заголовки
)

app.include_router(api_router)
