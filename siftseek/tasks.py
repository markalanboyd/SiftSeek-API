"""
The tasks.py file collects chron jobs and various as-needed tasks for maintenance.
"""

import logging

from datetime import datetime, timedelta

from siftseek.models.db import db
from siftseek.models.seeker import Seeker

logger = logging.getLogger(__name__)


def cron_delete_marked_seeker_records():
    """
    Periodically deletes Seeker records that are marked for deletion.

    This function is intended to be run as a cron job or scheduled task. It
    queries the database for Seeker records where the 'marked_for_deletion'
    flag is set to True and the 'deleted_at' timestamp is older than 30 days
    from the current date and time.

    Each qualifying record is deleted from the database. If an exception
    occurs during the deletion of a record, it logs the error without halting
    the entire process. After processing all records, a commit is made to the
    database to finalize the deletions.

    Note:
        - This function should be used with caution as it performs permanent
        deletion of data.
        - Ensure that it's scheduled appropriately according to the
        application's data retention policies.
    """
    records_to_delete = Seeker.query.filter(
        Seeker.marked_for_deletion == True,
        Seeker.deleted_at <= datetime.utcnow() - timedelta(days=30),
    ).all()

    for record in records_to_delete:
        try:
            db.session.delete(record)
        except Exception as e:
            logger.error(e)

    db.session.commit()
