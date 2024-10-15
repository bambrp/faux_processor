from os import environ
from process import process


def handler(event, context):
    """Lambda event handler function"""
    process(
        environ.get("bucket", "faux-processor-uk"),
        event.get("file"),
        event.get("retry", True),
        event.get("retry_attempts", 4),
    )
