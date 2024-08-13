from rich.console import Console
from rich.theme import Theme

"""Define custom styles."""
custom_theme = Theme(
    {
        "info": "bold cyan",
        "error": "bold red",
        "warning": "bold yellow",
        "success": "bold green",
    }
)


def create_custom_console() -> Console:
    """Create and return a console with custom styles."""
    return Console(theme=custom_theme)