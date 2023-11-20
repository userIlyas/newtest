from tkinter import *
import os


# окно для регистрации
def registration():
    global registration_screen
    registration_screen = Toplevel(main_screen)
    registration_screen.title("Регистрация")
    registration_screen.geometry("500x250")
    registration_screen.configure(bg='white')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(registration_screen, text="Введите данные", bg="pink").pack()
    Label(registration_screen, text="", bg="white").pack()
    username_lable = Label(registration_screen, bg="pink", text="Логин")
    username_lable.pack()
    username_entry = Entry(registration_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(registration_screen, bg="pink", text="Пароль")
    password_lable.pack()
    password_entry = Entry(registration_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(registration_screen, text="", bg="white").pack()
    Button(registration_screen, text="Зарегистрироваться", width=20, height=1, bg="pink", command=registration_user).pack()


# Окно для логина

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Вход")
    login_screen.geometry("500x250")
    login_screen.configure(bg='white')
    Label(login_screen, text="Введите свои данные", bg="white").pack()
    Label(login_screen, text="", bg='white').pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Логин", bg="white").pack()
    username_login_entry = Entry(login_screen, bg="white", textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, bg="white", text="").pack()
    Label(login_screen, text="Пароль", bg="white").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg='white').pack()
    Button(login_screen, text="Login", bg="pink", width=10, height=1, command=login_verify).pack()


# кнопка регистрации

def registration_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(registration_screen, text="Регистрация успешна", fg="green", font=("calibri", 11)).pack()


# кнопка логина

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# проектирование всплывающего окна для успешного входа в систему

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success", fg ="green").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# разработка всплывающего окна для ввода недействительного пароля

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Успешно")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Неверный пароль", fg="red").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# проектирование всплывающего окна для пользователя, который не найден

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Успешно")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Пользователь не найден", fg= 'red').pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Удаление всплывающих окон

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Основное окно

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg='white')
    main_screen.geometry("1000x1300")
    main_screen.title("Идентификация и аутентификация")
    Label(text="Выберите раздел", bg="pink", width="30", height="10", font=("Arial", 13)).pack()
    Label(text="", bg="white").pack()
    Button(text="Вход", bg="pink", height="10", width="30", command=login).pack()
    Label(text="", bg="white").pack()
    Button(text="Регистрация", bg="pink", height="10", width="30", command=registration).pack()

    main_screen.mainloop()


main_account_screen()