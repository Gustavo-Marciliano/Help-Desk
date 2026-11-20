from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.constants.usuarios import CLIENTE


if TYPE_CHECKING:
    from app.models.chamado import Chamado
    from app.models.comentario import Comentario

# --------------

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    senha: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    tipo: Mapped[int] = mapped_column(
        Integer,
        default=CLIENTE,
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

# Mapped: indica que o atributo pertence ao mapeamento ORM.
#int, str, bool: indicam o tipo Python esperado.
#mapped_column: configura a coluna no banco.
#Integer, String, Boolean: definem os tipos SQL.

    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="autor",
        foreign_keys="Comentario.id_usuario"
    )
    
    chamados_abertos: Mapped[list["Chamado"]] = relationship(
        back_populates="solicitante",
        foreign_keys="Chamado.id_usuario"
    )
    
    chamados_atribuidos: Mapped[list["Chamado"]] = relationship(
        back_populates="tecnico",
        foreign_keys="Chamado.id_tecnico"
    )
    
# chamados_abertos	Nome do atributo em Python.
# Mapped[list["Chamado"]]	Indica que teremos uma lista de objetos Chamado.
# relationship()	Cria o relacionamento entre os modelos.
# back_populates="solicitante"	Informa o nome do atributo correspondente no modelo Chamado.
# foreign_keys="Chamado.id_usuario"	Indica qual chave estrangeira conecta os modelos.