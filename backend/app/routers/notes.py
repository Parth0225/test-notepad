from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Note
from app.schemas import NoteCreate, NoteOut, NoteUpdate

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=list[NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()


@router.post("/", response_model=NoteOut, status_code=201)
def create_note(body: NoteCreate, db: Session = Depends(get_db)):
    note = Note(**body.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("/{item_id}", response_model=NoteOut)
def get_note(item_id: int, db: Session = Depends(get_db)):
    note = db.get(Note, item_id)
    if not note:
        raise HTTPException(404, "Note not found")
    return note


@router.put("/{item_id}", response_model=NoteOut)
def update_note(item_id: int, body: NoteUpdate, db: Session = Depends(get_db)):
    note = db.get(Note, item_id)
    if not note:
        raise HTTPException(404, "Note not found")
    for k, v in body.model_dump(exclude_none=True).items():
        setattr(note, k, v)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{item_id}", status_code=204)
def delete_note(item_id: int, db: Session = Depends(get_db)):
    note = db.get(Note, item_id)
    if not note:
        raise HTTPException(404, "Note not found")
    db.delete(note)
    db.commit()
