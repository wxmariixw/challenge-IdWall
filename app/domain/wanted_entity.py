from datetime import datetime
from pydantic import BaseModel, Field

class WantedModel(BaseModel):
    procurado_id: str = Field(...)
    procurado_apelido: str = Field(...)
    data_nascimento: datetime = Field(...)
    cor_cabelo: str = Field(...)
    cor_olhos: str = Field(...)
    procurado_peso: float = Field(...)
    procurado_altura: float = Field(...)
    procurado_profissao: str = Field(...)
    marcas_cicatrizes: str = Field(...)
    procurado_ncic: int = Field(...)
    recompensa: str = Field(...)
    aviso: str = Field(...)
    local_nascimento: str = Field(...)
    nacionalidade: int = Field(...)
    sexo: str = Field(...)
    raca: str = Field(...)