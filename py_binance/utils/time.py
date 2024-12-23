from datetime import datetime


def get_timezone_offset_relative_to_utc() -> str:
    local_now = datetime.now().astimezone()

    utc_offset = local_now.utcoffset()

    total_seconds = utc_offset.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int(abs(total_seconds % 3600) // 60)

    # Format as HH:MM
    formatted_offset = f"{hours:+03d}:{minutes:02d}"
    return formatted_offset
