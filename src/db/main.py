from sqlmodel import create_engine,text ,SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
async_engine=create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800
    
)


async def init_db():
    async with async_engine.begin() as connection:
        from src.db.models import Shoe,User
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:

    Session=sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False

    )
    async with Session() as session:
        yield session

        


