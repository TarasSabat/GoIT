from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship
    )
from sqlalchemy.ext.hybrid import hybrid_property

from app.db import Base


class GoodsForClients(Base):
    __tablename__ = "goods_for_clients"
    
    
    assoc_id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    goods_id: Mapped[int] = mapped_column(ForeignKey("goods.id"))
    
    goods: Mapped["Goods"] = relationship(back_populates="client_assoc")
    client: Mapped["Client"] = relationship(back_populates="goods_assoc")
    

class Client(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50), default="Black")
    addresses: Mapped[list["Address"]] = relationship(
        back_populates="client",
        cascade="all, delete-orphan")
    
    goods_assoc: Mapped[list["GoodsForClients"]] = relationship(back_populates="client")
    
    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __repr__(self) -> str:
        return f"Client({self.id}, {self.first_name}, {self.last_name})"
    
    
class Goods(Base):
    __tablename__ = "goods"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    
    client_assoc: Mapped[list["GoodsForClients"]] = relationship(back_populates="goods")


class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(50))
    street: Mapped[str] = mapped_column(String(100))
    building: Mapped[int] = mapped_column()
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    
    client: Mapped["Client"] = relationship(
        back_populates="addresses")
    
    def __repr__(self) -> str:
        return f"Address({self.id}, {self.city}, {self.street}, {self.building})"
    