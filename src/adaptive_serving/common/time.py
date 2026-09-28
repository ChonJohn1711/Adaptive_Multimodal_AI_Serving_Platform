def utc_now():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)
