from fastapi import FastAPI, Query
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

# Defina as informações de conexão com o banco de dados PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/idwall"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Defina o modelo da tabela do banco de dados
class Procurado(Base):
    __tablename__ = 'procurado'

    procurado_id = Column(Integer, primary_key=True)
    procurado_nome = Column(String(collation='pg_catalog.default'))
    procurado_apelido = Column(String(collation='pg_catalog.default'))
    data_nascimento = Column(Date)
    cor_cabelo = Column(String(collation='pg_catalog.default'))
    cor_olhos = Column(String(collation='pg_catalog.default'))
    procurado_peso = Column(Float)
    procurado_altura = Column(Float)
    procurado_profissao = Column(String(collation='pg_catalog.default'))
    marcas_cicatrizes = Column(String(collation='pg_catalog.default'))
    procurado_ncic = Column(Integer)
    recompensa = Column(String(collation='pg_catalog.default'))
    comentario = Column(Text(collation='pg_catalog.default'))
    aviso = Column(Text(collation='pg_catalog.default'))
    local_nascimento = Column(String(collation='pg_catalog.default'))
    nacionalidade = Column(Integer)
    sexo = Column(String(collation='pg_catalog.default'))
    raca = Column(String(collation='pg_catalog.default'))

Base.metadata.create_all(bind=engine)

# Defina os modelos de dados para entrada e saída
class ProcuradoCreate(BaseModel):
    procurado_nome: str
    procurado_apelido: str
    data_nascimento: date
    # Adicione outros campos conforme necessário

class ProcuradoRead(ProcuradoCreate):
    procurado_id: int

# Rotas
@app.get("/itens", response_model=List[ProcuradoRead])
def listar_procurados():
    db = SessionLocal()
    procurados = db.query(Procurado).all()
    db.close()
    return procurados

@app.get("/itens/filtrar", response_model=List[ProcuradoRead])
def filtrar_procurados(nome: str = Query(...)):
    db = SessionLocal()
    procurados_filtrados = db.query(Procurado).filter(Procurado.procurado_nome.ilike(f"%{nome}%")).all()
    db.close()
    return procurados_filtrados

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
