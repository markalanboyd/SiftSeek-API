from datetime import datetime
from enum import Enum

from sqlalchemy import String, Integer, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from siftseek.models.db import db
from siftseek.shared.enums import EducationLevel


class Seeker(db.Model):
    __tablename__ = "seekers"
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
    first_name: Mapped[String] = mapped_column(String(255))
    last_name: Mapped[String] = mapped_column(String(255))
    contact_email: Mapped[String] = mapped_column(String(255), unique=True)
    work_phone: Mapped[String] = mapped_column(String(255), nullable=True)
    work_phone_ext: Mapped[String] = mapped_column(String(255), nullable=True)
    cellphone: Mapped[String] = mapped_column(String(255), nullable=True)
    address: Mapped[String] = mapped_column(String(255), nullable=True)
    city: Mapped[String] = mapped_column(String(255), nullable=True)

    # URLs
    profile_pic_url: Mapped[String] = mapped_column(
        String(2000), default=DEFAULT_PROFILE_PIC_URL
    )
    resume_url: Mapped[String] = mapped_column(String(2000), nullable=True, unique=True)
    linkedin_url: Mapped[String] = mapped_column(
        String(2000), nullable=True, unique=True
    )
    portfolio_url: Mapped[String] = mapped_column(
        String(2000), nullable=True, unique=True
    )

    # Resume Info
    summary: Mapped[String] = mapped_column(String(10_000), nullable=True)
    education_level: Mapped[EducationLevel] = mapped_column(
        Enum(EducationLevel), nullable=True
    )
    remote_option: Mapped[Boolean] = mapped_column(
        Boolean, default=False, nullable=True
    )

    # Relationships
    # applications = relationship("Application", back_populates="seeker")
