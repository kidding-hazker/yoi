import os

__all__ = ["install", "uninstall", "enable", "disable"]

def install(name: str):
    pass

def uninstall(name: str):
    pass

def enable(name: str):
    plugin = __import__(f"yoi.plugins.{name}")

def disable(name: str):
    pass

def plugins() -> list[str]:
    return [*filter(lambda f: f != "__init__.py", os.listdir(os.path.dirname(__file__)))]
