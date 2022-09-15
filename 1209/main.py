def fun_1(user_input):
    words = user_input.split(" ")  # список слов введных пользователем
    capital_letters = []  # список в котором значение 1-- в подстроке больше больших символов, 0 -маленьких

    # проходим по словам в списке слов
    for word in words:
        upper_letter = 0
        lower_letter = 0
        # проходим по символам в слове
        for letter in word:
            if letter.isupper():
                upper_letter += 1
            elif letter.islower():
                lower_letter += 1
            else:
                continue

        capital_letters.append(upper_letter > lower_letter)

    return round(sum(capital_letters) * 100 / len(capital_letters), 2)


def fun_with_generator(user_input):
    def generator(words):
        for word in words:
            # сумма больших в слове минус сумма маленьких в слове
            res = sum(map(lambda x: int(x.isupper()), word)) - sum(map(lambda x: int(x.islower()), word))
            if res <= 0:
                yield 0
            else:
                yield 1

    words = user_input.split(" ")
    capital_letters = [i for i in generator(words)]
    return round(sum(capital_letters) * 100 / len(capital_letters), 2)


def main():
    user_input = input("Введите через пробел подстроки содержащие заглавные и строчные символы: ")
    print("fun_1: Процент подстрок в которых заглавных символов больше = {0}%".format(fun_1(user_input)))
    print("fun_2: Процент подстрок в которых заглавных символов больше = {0}%".format(fun_with_generator(user_input)))



if __name__ == '__main__':
    main()
