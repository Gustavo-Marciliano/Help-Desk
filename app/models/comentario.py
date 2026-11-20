from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func, Integer, Text 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.chamado import Chamado
    from app.models.usuario import Usuario
# --------------

class Comentario(Base):
    __tablename__ = "comentarios"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    mensagem: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    id_chamado: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("chamados.id"),
        nullable=False
    )

    id_usuario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )
    
    data_criacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
# Mapped: indica que o atributo pertence ao mapeamento ORM.
# int, str, bool: indicam o tipo Python esperado.
# mapped_column: configura a coluna no banco.
# Integer, String, Boolean: definem os tipos SQL.

    chamado: Mapped["Chamado"] = relationship(
        back_populates="comentarios",
        foreign_keys=[id_chamado]
    )
    
    autor: Mapped["Usuario"] = relationship(
        back_populates="comentarios",
        foreign_keys=[id_usuario]
    )
    
# chamados_abertos	Nome do atributo em Python.
# Mapped[list["Chamado"]]	Indica que teremos uma lista de objetos Chamado.
# relationship()	Cria o relacionamento entre os modelos.
# back_populates="solicitante"	Informa o nome do atributo correspondente no modelo Chamado.
# foreign_keys="Chamado.id_usuario"	Indica qual chave estrangeira conecta os modelos.