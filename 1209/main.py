"""main file for check_sub_str."""
from check_sub_str import fun_one
if __name__ == '__main__':
    text_one = "Введите через пробел подстроки содержащие заглавные и строчные символы: "
    user_input = input()
    print("fun_1: Процент подстрок в которых заглавных символов больше = {0}%".format(fun_one(user_input)))
