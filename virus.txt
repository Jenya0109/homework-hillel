action_dict={
'read': 'R',
'write': 'W',
'execute': 'X'
}

file_permissions = {}
for i in range(int(input('Enter number of files: '))):
    file, *permissions = input('Enter file name : ').split()
    file_permissions[file] = set(permissions)
result = []
for i in range(int(input('Enter the number of requests: '))):
    action_file = input('Enter the operation on the file: ')
    name_file = input('Enter the file name: ')
    files = action_dict.get(action_file)
    if files and file_permissions.get(name_file):
        if files in file_permissions[name_file]:
            result.append('OK')
        else:
            result.append('Access denied')
print('\n'.join(result))
