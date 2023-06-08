print('1)')
def change(lst):
   lst[0], lst[-1] = lst[-1], lst[0]
   return lst
print(change([100, 50, 1]))
print(change(['!!!', 'world', 'Hello']))
print(change(['e', 'k', 'r', 'a', 'i', 'n', 'U']))

print('2)')
def to_dict(lst):
   return {element: element for element in lst}
print(to_dict([1, 50, 100]))
print(to_dict(['a', 'b', 'c']))
print(to_dict(['Hello', (1, 100), -8.9]))

print('3)')
def sum_range(start, end):
   if start > end:
      end, start = start, end
   return sum(range(start, end + 1))
print(sum_range(3, 2))
print(sum_range(-1, 1))
print(sum_range(5, 5))
