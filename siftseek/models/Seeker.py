from .db import db
from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column as mc
from datetime import datetime


class Seeker(db.Model):
    id: Mapped[int] = mc(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mc(
        DateTime, default=datetime.utc.now, nullable=False
    )
    modified_at: Mapped[DateTime] = mc(DateTime, nullable=False)
    deleted_at: Mapped[DateTime] = mc(DateTime)
    personal_details_id: Mapped[int] = mc()
