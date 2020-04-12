if __name__ == '__main__':
  s1= ['Ahmad', 18, 17, 19.5, 8, 25]
  s2= ['Sami', 20, 20, 19, 9, 28]
  s3= ['Faris', 14.5, 16, 13, 7, 23]

  name = input("Enter student's name: ")
  if s1[0] == name:
    total = sum(s1[1:])
    print(name, total)
  elif s2[0] == name:
    total = sum(s2[1:])
    print(name, total)
  elif s3[0] == name:
    total = sum(s3[1:])
    print(name, total)
  else:
    print('Student is not recorded 0')