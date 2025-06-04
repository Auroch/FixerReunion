"""Simple scheduling utilities."""
from datetime import datetime
from .caldav_service import get_free_busy


def find_meeting_slot(users, duration):
    """Return the first available slot as a datetime."""
    # This is a placeholder implementation
    return datetime.now()
