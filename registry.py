#IV модуь модификации реестра
import winreg, getmac
paths = ['SOFTWARE\Oracle\VirtualBox',
'SOFTWARE\Oracle\VirtualBox',
'SYSTEM\CurrentControlSet\Services\VBoxDrv']
created_regs=[]
c=0
def mod_registry():
    while c != 2:
        winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, paths[0], 0, winreg.KEY_WRITE)
        winreg.SetValueEx('HKEY_LOCAL_MACHINE',"Version", 0, winreg.REG_SZ, '6.1.0')
        c +=1
prefixs = ['08.00.27', '00:05:69', '00:0C:29', '00:50:56', '00:03:FF']
def check():
    mac = getmac.get_mac_address
