from typing import Optional
from collections import Counter


def most_common_letter(s: str) -> Optional[str]:
    """Finds the most common letter in a given string.
    
    - Ignore case
    - Ignore non-letter characters
    - If tie, return alphabetically first
    - If no letters, return None
    """
    letters = [c.lower() for c in s if c.isalpha()]

    if not letters:
        return None

    counts = Counter(letters)
    max_count = max(counts.values())

    # Get all letters with max frequency, then return alphabetically first
    most_common = [c for c, count in counts.items() if count == max_count]
    return min(most_common)
