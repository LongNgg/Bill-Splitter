money = int(input())
if money >= 6769:
    print('{} sheep'.format(money // 6769))
elif money >= 3848:
    number = money // 3848
    print(f'{number} cow' if number == 1 else f'{number} cows')
elif money >= 1296:
    number = money // 1296
    print(f'{number} pig' if number == 1 else f'{number} pigs')
elif money >= 678:
    number = money // 678
    print(f'{number} goat' if number == 1 else f'{number} goats')
elif money >= 23:
    number = money // 23
    print(f'{number} chicken' if number == 1 else f'{number} chickens')
else:
    print('None')
