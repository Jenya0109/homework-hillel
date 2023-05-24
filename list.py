print('1)')
debtors_june = {'Timothy Sarratt', 'Teddy Young', 'Mirabelle Powers', 'Cecil Pierce',
        'John Woolery', 'Bob Thornton', 'Paul Boyd', 'Pandora Ball'}
debtors_july = {'Timothy Sarratt', 'John Woolery', 'Bob Thornton', 'Paul Boyd', 'Clarissa Clark',
        'Hubert Swanson', 'Willette Olson', 'Priscilla Cobb', 'Milo Moore'}
print(f'Debtors for June and July: {",".join(debtors_june&debtors_july)}')
print(f'Debtors for only July: {",".join(debtors_july-debtors_june)}')

print('2)')
camel_list = ['FirstItem', 'FriendsList', 'MyTuple']
snake_list = []
for camel_case in camel_list:
    snake = '_'
    for new_list in camel_case:
        if new_list.isupper():
            snake += '_'
        snake += new_list.lower()
    snake_list.append(snake.lstrip('_'))
print(camel_list,'\n',snake_list)
