from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



@app.get("/casualty/{casualty_id}", status_code=status.HTTP_200_OK)
async def get_casualty(casualty_id: str, db: db_dependency):
    db_casualty = db.query(models.Casualties).filter(models.Casualties.Accident_Index == casualty_id).first()
    if db_casualty is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Casualty not found")
    return db_casualty

# @app.get("/casualties", status_code=status.HTTP_200_OK)
# async def get_all_casualties(db: db_dependency):
#     db_casulties = db.query(models.Casualties).all()
#     return db_casulties


@app.get("/casualties", status_code=status.HTTP_200_OK)
async def get_all_casualties(db: db_dependency, skip: int = 0, limit: int = 100):
    db_casulties = db.query(models.Casualties).offset(skip).limit(limit).all()
    if db_casulties is None:
        raise HTTPException(status_code=404, detail="Casualties not found")
    return db_casulties

