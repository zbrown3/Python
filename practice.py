def reversed_list(lst1,lst2):
  new_list = []
  for i in range(len(lst2)):
    new_list.append(lst2[-((len(lst2) - 1) - i)])


#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))