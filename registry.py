#IV модуь модификации реестра
import winreg
paths = ['SYSTEM\CurrentControlSet\Services\VBoxNetAdp',
'SOFTWARE\Oracle\VirtualBox',
'SYSTEM\CurrentControlSet\Services\VBoxDrv',
'SOFTWARE\Kaspersky\protected',
'SOFTWARE\ESET\ESETSecurity\CurrentVersion\Info',
'SOFTWARE\Microsoft\Windows Defender\Real-Time Protection']
created_regs=[]
cpu_key = r'HARDWARE\DESCRIPTION\System\CentralProcessor\0'
new_name = 'VBox CPU'
old_name =''
def mod_registry():
    global old_name 
    success = True
    for p in paths:
        try:
             winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, p)
        except FileNotFoundError:
            try:
                with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, p, 0, winreg.KEY_WRITE) as my_key:
                    created_regs.append(p)
                    winreg.SetValueEx(my_key,"Version", 0, winreg.REG_SZ, '6.1.0')
            except: success = False
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_WRITE | winreg.KEY_READ) as key:
            oldname, reg_type = winreg.QueryValueEx(key, "ProcessorNameString")
            old_name=oldname
            winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, new_name)
    except: success = False
    return success

def is_modded():
    try: 
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_READ) as key:
            s, _ = winreg.QueryValueEx(key, 'ProcessorNameString')
            if s == new_name:
                return True
        for p in paths:
            try:
                winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, p, 0, winreg.KEY_READ)
                return True
            except FileNotFoundError:
                continue
    except:
        return False
    return False

def res_registry():
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, old_name)

    try:
        for k in created_regs:
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, k)
    except: pass