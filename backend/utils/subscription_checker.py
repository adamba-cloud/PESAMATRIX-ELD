from datetime import datetime
from backend.utils.db import get_db


def expire_old_subscriptions():
    """
    Marks expired subscriptions as 'expired'
    """
    conn = get_db()

    now = datetime.utcnow()

    conn.execute(
        """
        UPDATE subscriptions
        SET status = 'expired'
        WHERE status = 'active' AND end_date < ?
        """,
        (now,)
    )

    conn.commit()
    conn.close()
