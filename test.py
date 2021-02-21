from winreg import *

modes = ["~ HIGHDPIAWARE", "~ DPIUNAWARE", "~ GDIDPISCALING DPIUNAWARsE"]

REG_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"


def set_reg(name, value):
    try:
        CreateKey(HKEY_CURRENT_USER, REG_PATH)
        registry_key = OpenKey(HKEY_CURRENT_USER, REG_PATH, 0, KEY_WRITE)
        SetValueEx(registry_key, name, 0, REG_SZ, value)
        CloseKey(registry_key)
        return True
    except WindowsError:
        return False


def get_reg(name):
    try:
        key = OpenKey(HKEY_CURRENT_USER, REG_PATH)
        key_value = QueryValueEx(key, name)
        
        print(key_value)
        return True
    except WindowsError:
        return False


get_reg(r"C:\Users\PEF\Music\Outlook Express\Movie Maker\moviemk.exe")
