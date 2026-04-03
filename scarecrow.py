import ctypes, sys, tkinter, files, registry, process
#I модуль запуска
def start_all():
    process.start_process()
    files.create_files()
    registry.mod_registry()
def stop_all():
    process.stop_process()
    files.delеte_files()
    registry.res_registry()
def main_window():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, 0)

    root = tkinter.Tk()
    root.title('Scarecrow.alpha')
    root.geometry('450x250')

    ind_frame = tkinter.Frame(root)
    ind_frame.grid(row=6, column=0, columnspan=3, pady=15)
    lab_files = tkinter.Label(ind_frame, text='Файлы: Нет', fg='red')
    lab_files.grid(row=6, column=0, sticky="nsew", pady=15)
    lab_proc = tkinter.Label(ind_frame, text='Процессы: Выключены', fg='red')
    lab_proc.grid(row=6, column=2, sticky="nsew", pady=15)
    lab_reg = tkinter.Label(ind_frame, text='Реестр: Чист', fg='red')
    lab_reg.grid(row=6, column=1, sticky="nsew", pady=15)

    def ind_update():
        if files.is_created():
            lab_files.config(text='Файлы: OK', fg='green')
        else: lab_files.config(text='Файлы: Нет', fg='red')
        if process.is_started():
            lab_proc.config(text='Процессы: Запущены', fg='green')
        else: lab_proc.config(text='Процессы: Выключены', fg='red')
        if registry.is_modded():
            lab_reg.config(text='Реестр: изменён', fg='green')
        else: lab_reg.config(text='Реестр: Чист', fg='red')
        root.update_idletasks()
    ind_update()

    all_start_btn = tkinter.Button(root, text='запуск всех функций', command=lambda: [start_all(), ind_update()])
    all_start_btn.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)

    all_stop_btn = tkinter.Button(root, text="полное выключение и очистка", command=lambda: [stop_all(), ind_update()])
    all_stop_btn.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)

    sub_functions = [
            ("Создать Файлы", files.create_files),
            ("Модифицировать Реестр", registry.mod_registry),
            ("Запустить Процессы", process.start_process),
            ("Удалить Файлы", files.delеte_files), 
            ("Откатить Реестр", registry.res_registry),
            ("Завершить Процессы", process.stop_process)
        ]

    for i, item in enumerate(sub_functions):
            name, func = item
            row = (i // 3) + 3
            col = i % 3
            btn = tkinter.Button(root, text=name, command=lambda f=func: [f(), ind_update()])
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    label = tkinter.Label(root, text='scarecrow.alpha')
    label.grid(row=0, column=0, columnspan=3, pady=10)
    root.mainloop()
def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if not admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
else: main_window()