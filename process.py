# II модуль имитации процессов
import subprocess, os, ctypes, sys, psutil, shutil
pr_catalog = ['VBoxSerice.exe', 'VBoxTray.exe', 'Wireshark.exe', 'ProcessHacker.exe', 'ghidra.exe']
active_pr = []
path_ =r'C:\ybc'
def start_process():
    def folder():
        attribute = '0x02'
        os.makedirs(path_, exist_ok=True)
        subprocess.run(['attrib', '+h', path_], check=True)
    folder()
    c =0
    while c != 5:
        shutil.copy('C:\Windows\System32\ping.exe', os.path.join(path_,pr_catalog[c]))
        fake_path= os.path.join(path_,pr_catalog[c])
        pr = subprocess.Popen([fake_path, '-t', '127.0.0.1'], creationflags=subprocess.CREATE_NO_WINDOW)
        active_pr.append(pr)
        c+=1