"""Mock AI engine for meeting suggestions."""


def suggest_meeting(demande):
    """Return a suggested date and location."""
    # This is a placeholder that simply returns current time and no location
    return demande.date or None, demande.lieu
