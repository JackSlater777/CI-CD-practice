# Написать функцию to_roman, которая принимает целое число, а возвращает строку, отображающую это число римскими
# цифрами. Например, на вход подается 6, возвращается - "VI"; на вход подается 23, возвращается "XXIII".
# Входные данные должны быть в диапазоне от 1 до 5000, если подается число не из этого диапазона,
# или не число, то должны выбрасываться ошибка типа NonValidInput. Этот тип ошибки надо создать отдельно.
# Также необходимо в папке с файлом, содержащим вашу функцию, создать файл tests.py, внутри которой
# необходимо определить тесты для вашей функции. Тесты должны покрывать все возможное поведение функции,
# включая порождения ошибки при некорректных входных данных.

# Задаем свой класс исключений
# Обязательно должен наследоваться от встроенного класса Exception
class NonValidInput(Exception):
    # Как правило, тело класса исключения остается пустым
    pass


def to_roman(n):
    # Если ввод некорректный, выбрасываем исключение
    if type(n) != int or n < 1 or n > 5000:
        raise NonValidInput
    # Превращаем число в строку
    s = str(n)
    # Прописываем словари для конверсии - выясняем зависимости
    # 9 = IX - XC - CM
    # 8 = VIII - LXXX - DCCC
    # 7 = VII - LXX - DCC
    # 6 = VI - LX - DC
    # 5 = V - L - D - V
    # 4 = IV - XL - CD - MV
    # 3 = III - XXX - CCC - MMM
    # 2 = II - XX - CC - MM
    # 1 = I - X - C - M
    # 0 =
    d1 = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
    d2 = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
    d3 = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
    d4 = {'0': '', '1': 'M', '2': 'MM', '3': 'MMM', '4': 'MV', '5': 'V'}
    lst = [d1, d2, d3, d4]
    # Создаем новый список под конверсию (строку нельзя, т.к. нет метода присоединить строку к голове строки)
    roman_list = []
    # Индекс элемента-буквы в строке
    i = len(s) - 1
    # Индекс элемента-словаря в списке
    j = 0
    # Итерируем по строке с конца и вставляем в голову списка замены по словарям
    while i >= 0:
        # Если цифра есть в словаре
        if s[i] in lst[j]:
            # Вставляем замену из словаря в голову списка
            roman_list.insert(0, lst[j][s[i]])
        # Переходим к предыдущей цифре и следующему словарю
        j += 1
        i -= 1
    # Выводим список
    print(roman_list)
    # Превращаем список в строку
    roman_number = ''.join(roman_list)
    # Выводим и возвращаем искомый результат
    print(roman_number)
    return roman_number


if __name__ == "__main__":
    try:
        to_roman(4125)
    except NonValidInput: # обрабатываем только свой тип исключений
        print('Incorrect input!')