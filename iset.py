"""
Get Settings
"""
import json

path = None


def create(path):
    with open(path, "w") as obj:
        app = {"conf_ver": 3,
               "general": {"clipboard": True, "start_menu_mode": False, "shell_gui": "cmd", "acrylic_enabled": True},
               "graphics": {"window_mode": "multi"},
               "putty": {"ip": None},
               "distro_blacklist": ["docker"],
               "app_blacklist": ["exampleblock"],
               "xserver_profiles": {"Plain VcXsrv": []
                                   }}

        json.dump(app, obj, indent=True)
        obj.close()


def read():
    with open(path, "r") as obj:
        current = json.load(obj)
        obj.close()
        return current


def set(json_f):
    with open(path, "w") as obj:
        json.dump(json_f, obj, indent=True)
        obj.close()
