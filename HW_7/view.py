
def batton_click_read_or_writing ():
    flag = input('\nЕсли Вы хотите вывести все данные из документ, нажмите "1"\
                \nЕсли хотите вывести только ФИ, нажмите "0"\
                \nесли хотите записать новый контакт, нажмите "9"\
                \nЕсли хотите завершить, нажмите "q":  ')
    return flag

def Batton_click_name_or_id ():
    flag = input('\nесли Вы хотите вывести список ФИ сортированный по ID, нажмите "1"\
            \nесли хотите вывести список ФИ сортированный по алфавиту, нажмите "2"\
            \nесли хотите завершить работу нажмите "q"')
    return flag