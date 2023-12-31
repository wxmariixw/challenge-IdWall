from fastapi import status
from fastapi import APIRouter
from typing import List
from app.router.schema.wanted_schema import Wanted
from app.domain.wanted_entity import WantedEntity
from app.settings.settings import SessionLocal

router = APIRouter(redirect_slashes=False)


@router.get(
    "/",
    response_model=List[Wanted],
    status_code=status.HTTP_200_OK,
)
def get_wanted():
    db = SessionLocal()
    procurados = db.query(WantedEntity).all()
    db.close()
    return procurados
