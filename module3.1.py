calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    calls += 1
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.lower()
    for i in list_to_search:
        i = i.lower()
        if string in i or i in string:
            return True
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

