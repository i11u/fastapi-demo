from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user_name = "demo0813"
password = "fastapi_demo"
host = "mysql"  # docker-composeで定義したMySQLのサービス名
database_name = "fastapi_demo"

DATABASE_URL = 'mysql://%s:%s@%s/%s' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
engine = create_engine(
    DATABASE_URL,
    encoding="utf-8",
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
