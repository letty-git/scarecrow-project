# II модуль имитации процессов
import subprocess, os, shutil
pr_catalog = ['VBoxSerice.exe', 'VBoxTray.exe', 'Wireshark.exe', 'ProcessHacker.exe', 'ghidra.exe', 'avp.exe', 'MsMpEng.exe', 'avastui.exe']
active_pr = []
path_ =r'C:\ybc'
def start_process():
    def folder():
        attribute = '0x02'
        os.makedirs(path_, exist_ok=True)
        subprocess.run(['attrib', '+h', path_], check=True)
    folder()
    for p in pr_catalog:
        shutil.copy('C:\Windows\System32\ping.exe', os.path.join(path_,p))
        fake_path = os.path.join(path_, p)
        pr = subprocess.Popen([fake_path, '-t', '127.0.0.1'], creationflags=subprocess.CREATE_NO_WINDOW)
        active_pr.append(pr)
        
def stop_process():
    for pr in active_pr:
        pr.terminate() 
    shutil.rmtree(path_)

def is_started():
    for p in active_pr:
        if p.poll() is None:
            return True
    return False