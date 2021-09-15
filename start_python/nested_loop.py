fruits = ['apple', 'banana', 'mango', 'strawberry', 'berry']
fruits2 = ['apple', 'banana', 'mango']
# banana
for fruit in fruits: # 5
    print('fruits ', fruit)
    for fruit2 in fruits2: # 3
        print('fruit2 ',fruit2)
        for i in range(5):
            print('loop i')

# nested loop with if statement
for data in fruits:
    if data == 'apple':
        if data in fruits2:
            print(data)
        else:
            print('its wrong')
    else:
        print('its wrong')
