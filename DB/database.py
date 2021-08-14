from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 接続したいDBの基本情報を設定
user_name = "hisano"
password = "hisanoa303"
host = "localhost"  # docker-composeで定義したMySQLのサービス名
database_name = "fastapi_demo"

DATABASE = 'mysql://%s:%s@%s/%s' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if __name__  == '__main__':
    print(SessionLocal)
