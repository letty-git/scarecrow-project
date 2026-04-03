#III модуль создания файлов
import os
fake_paths = [r'C:\Windows\System32\drivers\vboxguest.sys',
    r'C:\Windows\System32\drivers\vboxmouse.sys',
    r'C:\Windows\System32\drivers\vmmouse.sys',
    r'C:\Program Files\Windows Defender\MpCmdRun.exe',
    r'C:\Program Files\Kaspersky Lab\avp.exe',
    r'C:\Program Files\ESET\ESETSecurity\tcmd.exe']
created_files =[]
def create_files():
    for path in fake_paths:
        if not os.path.exists(path):
            open(path, 'x').close()
        created_files.append(path)

def delеte_files():
    try:
        for fl in created_files:
            os.remove(fl)
    except:pass

def is_created():
    for path in fake_paths:
        if os.path.exists(path):
            return True
    return False