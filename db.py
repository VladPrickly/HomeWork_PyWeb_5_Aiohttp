import atexit
from datetime import datetime
import os
from sqlalchemy.orm import sessionmaker, DeclarativeBase, MappedColumn, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import create_engine, Integer, Text, String, DateTime, Column, func
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    id: MappedColumn[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Advertisement(Base):
    __tablename__ = 'adv_aiohttp'

    title: MappedColumn[str] = mapped_column(String)
    description: MappedColumn[str] = mapped_column(Text)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, server_default=func.now())
    owner: MappedColumn[str] = mapped_column(String)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'owner': self.owner,
        }


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_orm():
    await engine.dispose()
