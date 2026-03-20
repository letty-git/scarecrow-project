#III модуль создания файлов
import os
fake_paths = [r'C:\Windows\System32\drivers\vboxguest.sys',
    r'C:\Windows\System32\drivers\vboxmouse.sys',
    r'C:\Windows\System32\drivers\vmmouse.sys']
created_files =[]
def create_files():
    for path in fake_paths:
        if not os.path.exists(path):
            open(path, 'x').close()