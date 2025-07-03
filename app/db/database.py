from sqlalchemy import URL


# DATABASE_URL = URL.create(
#     drivername="postgresql+asyncpg",
#     username="fastapi_user",
#     password="fastapi_password",
#     host="postgres",
#     port="5432",
#     database="fastapi_db"
# )

DATABASE_URL = "postgresql+asyncpg://fastapi_user:fastapi_password@postgres:5432/fastapi_db"