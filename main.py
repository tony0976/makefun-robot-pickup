# The joke grows out of machine logic — a diagnostic, an error code —
# and lands as charm, not a human line with a beep pasted on.
"""Writes one robot pickup line to /output/entry.txt."""
import os

TEXT = "I ran a full diagnostic on my heart. The only error it found was that you weren't in the room."

# Rule: the pickup line must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
