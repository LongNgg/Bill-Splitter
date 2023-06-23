# write your code here
import random
number_of_friends = int(input('Enter the number of friends joining (including you):\n'))
if number_of_friends <= 0:
    print('\nNo one is joining for the party')
    exit()

friend_list = []
print('\nEnter the name of every friend (including you), each on a new line:')
for _ in range(number_of_friends):
    friend_list.append(input())

total_bill = int(input('\nEnter the total bill value:\n'))


lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if lucky_feature == 'Yes':
    lucky_person = random.choice(friend_list)
    print(f'\n{lucky_person} is the lucky one!')
    split_bill = round(total_bill / (number_of_friends - 1), 2)
    friend_dict = dict.fromkeys(friend_list, split_bill)
    friend_dict[lucky_person] = 0
else:
    print('\nNo one is going to be lucky')
    split_bill = round(total_bill / number_of_friends, 2)
    friend_dict = dict.fromkeys(friend_list, split_bill)

print('\n', friend_dict)