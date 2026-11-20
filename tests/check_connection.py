from sqlalchemy import text

from app.database.connection import engine


try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("Conexão realizada com sucesso!")
        print(f"Resultado: {result.scalar_one()}")

except Exception as error:
    print("Erro ao conectar com o banco:")
    print(error)

finally:
    engine.dispose()