"""Handle chained inputs."""
from typing import Dict, List, Optional

_TEXT_COLOR_MAPPING = {
    "blue": "36;1",
    "yellow": "33;1",
    "pink": "38;5;200",
    "green": "32;1",
    "red": "31;1",
}


def get_color_mapping(
    items: List[str], excluded_colors: Optional[List] = None
) -> Dict[str, str]:
    """Get mapping for items to a support color."""
    colors = list(_TEXT_COLOR_MAPPING.keys())
    if excluded_colors is not None:
        colors = [c for c in colors if c not in excluded_colors]
    color_mapping = {item: colors[i % len(colors)] for i, item in enumerate(items)}
    return color_mapping


def get_colored_text(text: str, color: str) -> str:
    """Get colored text."""
    color_str = _TEXT_COLOR_MAPPING[color]
    return f"\u001b[{color_str}m\033[1;3m{text}\u001b[0m"


def print_text(text: str, color: Optional[str] = None, end: str = "") -> None:
    """Print text with highlighting and no end characters."""
    if color is None:
        text_to_print = text
    else:
        text_to_print = get_colored_text(text, color)
    print(text_to_print, end=end)

    # custom logging to file
    import re
    import os

    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    text_to_log = re.sub(ansi_escape, "", text_to_print)
    text_to_log = re.sub(r"[\xc2\x99]", "", text_to_log)
    with open("logs/output_now.log", "a") as f:
        print(text_to_log, file=f)
    if os.getenv("MYLANGCHAIN_SAVE_CHAT_HISTORY") == "1":
        with open("logs/output_recent.log", "a") as f:
            print(f"======\n{text_to_log}\n", file=f)
