import logging

from datetime import datetime, timedelta

from flask import request, jsonify
from marshmallow import ValidationError

from siftseek.models.db import db
from siftseek.models.seeker import Seeker

logger = logging.getLogger(__name__)


def cron_delete_marked_seeker_records():
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
