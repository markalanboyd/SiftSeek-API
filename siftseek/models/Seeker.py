from .db import db
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Seeker(db.Model):
    __tablename__ = "seekers"
    DEFAULT_PROFILE_PIC_URL: str = "https://as1.ftcdn.net/v2/jpg/05/16/27/58/1000_F_516275801_f3Fsp17x6HQK0xQgDQEELoTuERO4SsWV.jpg"

    # Metadata
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    _created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utc.now, nullable=False
    )
    modified_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime)

    # Personal Info
    username: Mapped[String] = mapped_column(String(15), unique=True)
    first_name: Mapped[String] = mapped_column(String(255), nullable=False)
    last_name: Mapped[String] = mapped_column(String(255), nullable=False)
    contact_email: Mapped[String] = mapped_column(
        String(255), nullable=False, unique=True
    )
    work_phone: Mapped[String] = mapped_column(String(255))
    work_phone_ext: Mapped[String] = mapped_column(String(255))
    cell_phone: Mapped[String] = mapped_column(String(255))
    address: Mapped[String] = mapped_column(String(255))
    city: Mapped[String] = mapped_column(String(255))

    # URLs
    resume_url: Mapped[String] = mapped_column(
        String(2000), default=DEFAULT_PROFILE_PIC_URL, unique=True
    )
    resume_url: Mapped[String] = mapped_column(String(2000), unique=True)
    linkedin_url: Mapped[String] = mapped_column(String(2000), unique=True)
    portfolio_url: Mapped[String] = mapped_column(String(2000), unique=True)

    # Resume Info
    summary: Mapped[String] = mapped_column(String(10_000))
    education_level_id: Mapped[Integer] = mapped_column(Integer)
    remote_option: Mapped[Boolean] = mapped_column(Boolean, default=False)

    @property
    def created_at(self) -> datetime:
        return self._created_at
