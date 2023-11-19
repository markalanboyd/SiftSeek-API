from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from siftseek.models.db import db


class Seeker(db.Model):
    """
    Represents a job seeker's profile in the SiftSeek platform.

    This ORM class is used for storing and managing information about job seekers.
    It includes metadata such as creation and modification timestamps, flags for deletion,
    and timestamps for when the profile is marked for deletion. Personal information
    like the seeker's name, contact details, and address is also stored.

    The class contains URLs for the seeker's profile picture, resume, LinkedIn, and
    portfolio, allowing seekers to provide comprehensive information about themselves.
    Resume-related information like a summary, education level, and remote work preference
    are also included.

    Each seeker may have multiple job applications, which are represented by a
    relationship with the JobApplication class (currently commented out due to a
    pending fix). This relationship is crucial for linking seekers with their
    respective job applications on the platform.

    TODO: Add and fix the relationship to JobApplication
    The relationship between job_application and seeker is causing an error.
    Need to investigate why it's not working.
    """

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
    education_level: Mapped[String] = mapped_column(String, nullable=True)
    remote_option: Mapped[Boolean] = mapped_column(
        Boolean, default=False, nullable=True
    )

    # Relationships
    # job_applications_relationship = relationship(
    #     "JobApplication", back_populates="seeker"
    # )
