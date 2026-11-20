from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func, String, Integer, Text 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.constants.chamados import ABERTO, MEDIA

if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.comentario import Comentario
    
# --------------

class Chamado(Base):
    __tablename__ = "chamados"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    titulo: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    descricao: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[int] = mapped_column(
        Integer,
        default=ABERTO,
        nullable=False
    )

    prioridade: Mapped[int] = mapped_column(
        Integer,
        default=MEDIA,
        nullable=False
    )
    
    id_usuario: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )
    
    id_tecnico: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=True
    )
    
    data_criacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
    data_atualizacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

# Mapped: indica que o atributo pertence ao mapeamento ORM.
# int, str, bool: indicam o tipo Python esperado.
# mapped_column: configura a coluna no banco.
# Integer, String, Boolean: definem os tipos SQL.

    solicitante: Mapped["Usuario"] = relationship(
        back_populates="chamados_abertos",
        foreign_keys=[id_usuario]
    )
    
    tecnico: Mapped["Usuario | None"] = relationship(
        back_populates="chamados_atribuidos",
        foreign_keys=[id_tecnico]
    )
    
    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="chamado"
    )   
    
# chamados_abertos	Nome do atributo em Python.
# Mapped[list["Chamado"]]	Indica que teremos uma lista de objetos Chamado.
# relationship()	Cria o relacionamento entre os modelos.
# back_populates="solicitante"	Informa o nome do atributo correspondente no modelo Chamado.
# foreign_keys="Chamado.id_usuario"	Indica qual chave estrangeira conecta os modelos.