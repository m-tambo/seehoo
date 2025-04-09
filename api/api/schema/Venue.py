from sqlalchemy.orm import Mapped, mapped_column

from ..model.database import db

class Venue(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    address: Mapped[str] = mapped_column(unique=False)
    latitude: Mapped[float] = mapped_column(unique=False)
    longitude: Mapped[float] = mapped_column(unique=False)
    type: Mapped[str] = mapped_column(unique=False, nullable=True)
    website: Mapped[str] = mapped_column(unique=False, nullable=True)
    created_at: Mapped[str] = mapped_column(default=db.func.now())
    updated_at: Mapped[str] = mapped_column(default=db.func.now(), onupdate=db.func.now())
    