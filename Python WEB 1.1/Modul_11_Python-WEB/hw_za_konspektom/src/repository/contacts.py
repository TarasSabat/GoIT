from datetime import date, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, extract
from src import schemas
from src.database.models import Contact
from src.schemas import ContactBase


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Optional[Contact]:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(contact: schemas.ContactCreate, db: Session):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


async def update_contact(contact_id: int, body: ContactBase, db: Session) -> Optional[Contact]:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in body.dict().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)  # Додано оновлення контакту після commit
    return contact


async def remove_contact(contact_id: int, db: Session) -> Optional[Contact]:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(db: Session, query: str) -> List[Contact]:
    return db.query(Contact).filter(
        or_(
            Contact.first_name.contains(query),
            Contact.last_name.contains(query),
            Contact.email.contains(query)
        )
    ).all()


async def get_upcoming_birthdays(db: Session) -> List[Contact]:
    today = date.today()
    upcoming = today + timedelta(days=7)

    contacts = db.query(Contact).filter(
        or_(
            (extract('month', Contact.birthday) == today.month) &
            (extract('day', Contact.birthday) >= today.day) &
            (extract('day', Contact.birthday) <= upcoming.day),
            (extract('month', Contact.birthday) == upcoming.month) &
            (extract('day', Contact.birthday) <= upcoming.day),
            (extract('month', Contact.birthday) == today.month) &
            (extract('day', Contact.birthday) < today.day)
        )
    ).all()

    return contacts
