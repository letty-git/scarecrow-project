import os, winreg, psutil, time

SUSPICIOUS_FILES = [
    r'C:\Windows\System32\drivers\vboxguest.sys',
    r'C:\Windows\System32\drivers\vboxmouse.sys',
    r'C:\Windows\System32\drivers\vboxvideo.sys'
    r'C:\Program Files\Windows Defender\MpCmdRun.exe',
    r'C:\Program Files\Kaspersky Lab\avp.exe',
    r'C:\Program Files\ESET\ESETSecurity\tcmd.exe']

SUSPICIOUS_PROCESSES = [
    'VBoxService.exe',
    'VBoxTray.exe',
    'Wireshark.exe',
    'ProcessHacker.exe',
    'ghidra.exe',
    'avp.exe',
    'MsMpEng.exe',
    'avastui.exe']

def check_files():
    print("[*] Проверка файловой системы...")
    detected = False
    for file_path in SUSPICIOUS_FILES:
        if os.path.exists(file_path):
            print(f" [!] НАЙДЕН ПОДОЗРИТЕЛЬНЫЙ ФАЙЛ: {file_path}")
            detected = True
    if not detected:
        print(" [+] Подозрительных файлов не обнаружено.")
    return detected

def check_processes():
    print("\n[*] Сканирование запущенных процессов...")
    detected = False

    running_processes = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]
    
    for proc in SUSPICIOUS_PROCESSES:
        if proc in running_processes:
            print(f" [!] НАЙДЕН ПРОЦЕСС АНАЛИЗА: {proc}")
            detected = True
    if not detected:
        print(" [+] Процессов анализатора не обнаружено.")
    return detected

def check_registry():
    print("\n[*] Анализ ключей реестра и оборудования...")
    detected = False
    
    try:
        access = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\CentralProcessor\0', 0, access) as key:
            cpu_name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            print(f" [i] Текущий процессор: {cpu_name}")
            if "VBox" in cpu_name or "Virtual" in cpu_name:
                print(" [!] ОБНАРУЖЕН ВИРТУАЛЬНЫЙ ПРОЦЕССОР (Признак песочницы!)")
                detected = True
    except Exception as e:
        print(f" [-] Ошибка доступа к реестру процессора: {e}")

    anty_keys = [
        'SOFTWARE\Kaspersky\protected',
        'SOFTWARE\ESET\ESETSecurity\CurrentVersion\Info',
        'SOFTWARE\Microsoft\Windows Defender\Real-Time Protection']
    for ant_mal in anty_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, ant_mal, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
                print(f" [!] ОБНАРУЖЕНА ВЕТКА РЕЕСТРА АНТИВИРУСА: {ant_mal}")
                detected = True
        except FileNotFoundError:
            pass 
    if not detected:
        print(" [+] Следов антивирусов в реестре не найдено.")
    return detected

def check_registry_2():
    vbox_keys = [
        r"SOFTWARE\Oracle\VirtualBox",
        r"SYSTEM\ControlSet001\Services\VBoxGuest"]
    for v_key in vbox_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, v_key, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
                print(f" [!] ОБНАРУЖЕНА ВЕТКА РЕЕСТРА VIRTUALBOX: {v_key}")
                detected = True
        except FileNotFoundError:
            pass 

    if not detected:
        print(" [+] Следов виртуальной машины в реестре не найдено.")
    return detected

def main():
    print("="*50)
    print(" ЗАПУСК СИСТЕМЫ ПРОВЕРКИ ОКРУЖЕНИЯ")
    print("="*50)
    time.sleep(1)

    files_bad = check_files()
    time.sleep(0.5)
    
    proc_bad = check_processes()
    time.sleep(0.5)
    
    reg_bad = check_registry()
    time.sleep(0.5)

    reg_2_bad = check_registry_2()
    time.sleep(0.5)

    print("\n" + "="*50)
    print(" ИТОГОВЫЙ ВЕРДИКТ:")
    
    if files_bad or proc_bad or reg_bad or reg_2_bad:
        print(" [!!!] СРЕДА НЕБЕЗОПАСНА [!!!]")
        print(" Обнаружены признаки виртуальной машины или анализатора трафика.")
        print(" Действие вредоноса: САМОЗАВЕРШЕНИЕ (Остановка выполнения).")
    else:
        print(" [OK] СРЕДА БЕЗОПАСНА [OK]")
        print(" Признаков анализа не найдено. Это реальный физический ПК.")
        print(" Действие вредоноса: ЗАПУСК ОСНОВНОЙ ПОЛЕЗНОЙ НАГРУЗКИ.")
    print("="*50)
    
    input("\nНажмите Enter для выхода")
    
if __name__ == "__main__":
    main()