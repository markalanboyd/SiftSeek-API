from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from siftseek.models.db import db


class Company(db.Model):
    __tablename__ = "companies"
    DEFAULT_PROFILE_PIC_URL: str = "https://as1.ftcdn.net/v2/jpg/05/16/27/58/1000_F_516275801_f3Fsp17x6HQK0xQgDQEELoTuERO4SsWV.jpg"

    # Metadata
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    modified_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    marked_for_deletion: Mapped[Boolean] = mapped_column(Boolean, default=False)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    # Personal Info
    username: Mapped[String] = mapped_column(String(20), unique=True)
    company_name: Mapped[String] = mapped_column(String(255))
    contact_email: Mapped[String] = mapped_column(String(255), unique=True)
    phone: Mapped[String] = mapped_column(String(255), nullable=True)
    address: Mapped[String] = mapped_column(String(255), nullable=True)
    city: Mapped[String] = mapped_column(String(255), nullable=True)

    # URLs
    profile_pic_url: Mapped[String] = mapped_column(
        String(2000), default=DEFAULT_PROFILE_PIC_URL
    )
