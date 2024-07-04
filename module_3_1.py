calls = 0#Создать переменную calls = 0 вне функций.
def count_calls():
    global calls
    calls += 1
    return calls

#Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре
def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = list(map(str.upper, list_to_search))
    if string not in list_to_search:
        return False
    else:
        return True


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
