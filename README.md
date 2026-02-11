# fastapi_architecture_sample
This repo is devoted to Computer Science students as a sample project to create backends

Қосу үшін:
cd app
uvicorn main:app --reload

http://localhost:8000/docs


DATABASE МОДЕЛЬДЕРІН ЖАСАУ ҮШІН:

alembic init alembic (1-ақ рет істеледі!!!!!!!)

alembic revision --autogenerate -m "created users"

### ӘРБІР МОДЕЛЬ БӨЛЕК МИГРАЦИЯМЕН БОЛУЫ КЕРЕК

### МЫНАУ 
alembic upgrade head
