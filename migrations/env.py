from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context
from database.models import Base
import os
from dotenv import load_dotenv

load_dotenv()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online() -> None:
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    connectable = create_engine(db_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline() -> None:
   url = os.getenv("DATABASE_URL")
   context.configure(
       url=url,
       target_metadata=target_metadata,
       literal_binds=True,
       dialect_opts={"paramstyle": "named"},
   )

   with context.begin_transaction():
       context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()