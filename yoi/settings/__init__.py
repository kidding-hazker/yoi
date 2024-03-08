import json
import yaml
import toml
import os

__all__ = ["load", "save"]

path = lambda name: os.path.join(os.path.dirname(__file__), name)

def load(name: str):
    match name.split(".")[-1]:
        case "toml":
            return toml.load(path(name))
        case _:
            return None

def save(name: str, data: dict):
    match name.split(".")[-1]:
        case "toml":
            with open(path(name), "w") as f: toml.dump(data, f)
        case _:
            pass
