from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)
        

# create_engine()	Cria o mecanismo de conexão com o banco
# pool_pre_ping=True	Verifica se a conexão está válida antes de reutilizá-la
# sessionmaker()	Cria uma fábrica de sessões     
        
        
# -----------------

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        
# SessionLocal() abre uma sessão, o código realiza a consulta.
# yield db disponibiliza a sessão para a rota.
# db.close() fecha a sessão ao terminar a requisição.