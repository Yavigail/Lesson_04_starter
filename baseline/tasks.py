"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""
import json


def count_selected(media_ids: list[str]) -> int:
    """Return the number of DIFFERENT media ids."""
    return len(set(media_ids))  # set removes duplicates, len counts what's left


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    """Group media items {"gallery_id": ..., "id": ...} by gallery.

    Return a dict: gallery id -> list of media ids, in input order.
    """
    groups: dict[str, list[str]] = {}
    for item in media:  # go over items in input order
        groups.setdefault(item["gallery_id"], []).append(item["id"])  # new gallery -> empty list, then add id
    return groups


def total_price(prices_minor: list[int | None]) -> int:
    """Return the sum of the prices (in agorot), ignoring None."""
    return sum(p for p in prices_minor if p is not None)  # sum only real prices


def first_missing(required: list[str], present: list[str]) -> str | None:
    """Return the first item of `required` that is not in `present`, or None."""
    present_set = set(present)  # fast lookup
    for item in required:  # keep the order of `required`
        if item not in present_set:
            return item  # first one that is missing
    return None  # nothing is missing


def load_events(path) -> list[dict]:
    """Read a JSON file encoded in UTF-8 and return its content (a list of events)."""
    with open(path, encoding="utf-8") as f:  # utf-8 keeps Hebrew titles correct on Windows
        return json.load(f)