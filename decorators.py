
def colorize(color: str):
    """Decorator to change text color using ANSI escape codes"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            colors = {"red": "\033[91m", "green": "\033[92m", "blue": "\033[94m"}
            reset = "\033[0m"
            return f"{colors.get(color, '')}{func(*args, **kwargs)}{reset}"
        return wrapper
    return decorator
