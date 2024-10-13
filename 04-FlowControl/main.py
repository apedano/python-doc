
def age_test(age):
    if age < 18:
        print('Minorenne')
    elif age <= 50:
        print('Maggiorenne')
    else:
        print('Vecchio')

input_age = int(input('Insert age: '))

#age_test(input_age)

print('Minorenne' if input_age < 18 else 'Maggiorenne' if input_age < 50 else 'Vecchio')


