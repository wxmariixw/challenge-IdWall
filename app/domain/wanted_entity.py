import datetime
from sqlalchemy import Column, Numeric, Text
from app.settings.settings import Base

class WantedEntity(Base):
    __tablename__ = "procurado"

    procurado_id: str = Column(Text, primary_key=True, index=True)
    procurado_apelido: str = Column(Text, nullable=True)
    data_de_nascimento: datetime = Column(Text, nullable=True)
    cor_cabelo: str = Column(Text, nullable=True)
    cor_olhos: str = Column(Text, nullable=True)
    procurado_peso: float = Column(Text, nullable=True)
    procurado_altura: float = Column(Numeric, nullable=True)
    procurado_profissao: str = Column(Text, nullable=True)
    marcas_cicatrizes: str = Column(Text, nullable=True)
    procurado_ncic: int = Column(Text, nullable=True)
    recompensa: str = Column(Text, nullable=True)
    aviso: str = Column(Text, nullable=True)
    local_nascimento: str = Column(Text, nullable=True)
    nacionalidade: int = Column(Text, nullable=True)
    sexo: str = Column(Text, nullable=True)
    raca: str = Column(Text, nullable=True)