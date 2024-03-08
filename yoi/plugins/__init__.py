import os
from .. import settings

__all__ = ["install", "uninstall", "enable", "disable"]

plugins = settings.load("plugins.toml")

def install(name: str):
    pass

def uninstall(name: str):
    pass

def enable(name: str):
    __import__(f"yoi.plugins.{name}")

def disable(name: str):
    pass

def list() -> list[str]:
    return [f for f in os.listdir(os.path.dirname(__file__)) if f != "__init__.py"]
