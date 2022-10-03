def fun_1(user_input: str) -> float:
    """Takes string with capitals letter and small letters, counts substrings which are more.

    Args:
        user_input : str - string with substrings.

    Returns: float - percentage of substrings with more capitals letter.
    """
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


def fun_with_generator(user_input: str) -> float:
    """Takes string with capitals letter and small letters, counts substrings which are more.

    Args:
        user_input : str - string with substrings.

    Returns: float - percentage of substrings with more capitals letter.
    """
    def generator(word: str) -> int:
        """Takes word and checks if there are more capitals characters in a string.

        Args:
            word : str - some word.

        Yields:
            int : 1 if there are more capitals characters and 0 else.
        """
        for symbol in word:
            # сумма больших в слове минус сумма маленьких в слове
            res = sum(map(lambda x: int(x.isupper()), symbol)) - sum(map(lambda x: int(x.islower()), symbol))
            if res <= 0:
                yield 0
            else:
                yield 1

    words = user_input.split(" ")
    capital_letters = [i for i in generator(words)]
    return round(sum(capital_letters) * 100 / len(capital_letters), 2)


def main():
    user_input = input("Введите через пробел подстроки содержащие заглавные и строчные символы: ")
    print(f"fun_1: Процент подстрок в которых заглавных символов больше = {fun_1(user_input)}%")
    print(f"fun_2: Процент подстрок в которых заглавных символов больше = {fun_with_generator(user_input)}%")


if __name__ == '__main__':
    main()
