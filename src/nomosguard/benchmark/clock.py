"""Clock for benchmark artifacts.

SOURCE_DATE_EPOCH is the reproducible-builds convention: when it is set,
otherwise identical runs must not differ in their ``run_at`` header.
"""

from __future__ import annotations

import os
from datetime import UTC, datetime


def run_at() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch is None:
        return datetime.now(UTC).isoformat()
    try:
        seconds = int(epoch)
    except ValueError:
        raise ValueError(
            "SOURCE_DATE_EPOCH must be an integer number of seconds"
        ) from None
    return datetime.fromtimestamp(seconds, UTC).isoformat()
