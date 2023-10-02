from typing import Optional
from pydantic import BaseModel, Field


class Wanted(BaseModel):
    procurado_id: str = Field(..., title="ID")
    procurado_apelido: Optional[str] = Field(..., title="Apelido e outros nomes")
    data_de_nascimento: Optional[str] = Field(..., title="Data de nascimento")
    local_nascimento: Optional[str] = Field(..., title="Local de nascimento")
    nacionalidade: Optional[str] = Field(..., title="Nacionalidade")
    cor_cabelo: Optional[str] = Field(..., title="Cor do cabelo")
    cor_olhos: Optional[str] = Field(..., title="Cor dos olhos")
    sexo: Optional[str] = Field(..., title="Sexo")
    raca: Optional[str] = Field(..., title="Raça")
    procurado_peso: Optional[str] = Field(..., title="Peso")
    procurado_altura: Optional[float] = Field(..., title="Altura")
    procurado_profissao: Optional[str] = Field(..., title="Profissão")
    marcas_cicatrizes: Optional[str] = Field(
        ..., title="Marcas, cicatrizes e tatuagens"
    )
    procurado_ncic: Optional[str] = Field(..., title="NCIC")
    aviso: Optional[str] = Field(..., title="Avisos")
    recompensa: Optional[float] = Field(..., title="Recompensa")
