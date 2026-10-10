# utility functions
import uuid


def generate_id() -> str:
    uid = str(uuid.uuid4()).split("-")
    return f"{uid[0]}-{uid[-1]}"