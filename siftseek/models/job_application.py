from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from siftseek.models.db import db


class JobApplication(db.Model):
    """
    Represents an application made by a job seeker to a job posting in the
    SiftSeek platform.

    This ORM class is used for storing and retrieving applications from the
    database. It includes fields that are editable by the job seeker, as well
    as a select few fields that can only be edited by the company to which
    the application is made.

    #TODO Add: job_posting_id
    This should be added when the corresponding functionality and ORM has been
    created.
    #TODO Fix: relationship to Seeker
    The relationship between job_application and seeker is causing an error.
    Need to investigate why it's not working.
    """

    __tablename__ = "job_applications"

    # Metadata
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    modified_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    marked_for_deletion: Mapped[Boolean] = mapped_column(Boolean, default=False)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    # Foreign Keys
    seeker_id: Mapped[ForeignKey] = mapped_column(ForeignKey("seekers.id"))
    # Following line commented out at the moment since this model does not yet exist
    # job_posting_id: Mapped[ForeignKey] = mapped_column(ForeignKey("job_posting.id"))

    # Application Fields
    submitted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    status: Mapped[String] = mapped_column(String(250), nullable=True)
    cover_letter: Mapped[String] = mapped_column(String(10_000), nullable=True)

    # Company-Owned Attributes
    reviewed_by: Mapped[String] = mapped_column(String(250), nullable=True)
    interview_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[String] = mapped_column(String(250), nullable=True)
    notes: Mapped[String] = mapped_column(String(10_000), nullable=True)

    # Relationships
    # seeker_relationship = relationship("Seeker", back_populates="applications")
