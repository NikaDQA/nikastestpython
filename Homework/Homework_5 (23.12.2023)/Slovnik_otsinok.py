st_marks = {'Ivanov':[150,1,5,1,5,1], 'Petrov': [5,3,3,3], 'Sidorov':[4,4,5,2], 'Moxov':[2,2,2,2], 'Gorohov':[1], 'Alekseev':[5,5,5,5]}
  # print(st_marks)
for val in st_marks:
  point=sum(st_marks[val])/len(st_marks[val])
  # print(point)
  st_marks.update({val:point})
  # print(st_marks)
for key in st_marks:
  best=max(st_marks.values())
  worse=min(st_marks.values())
for key in st_marks:
  if st_marks[key]==best:
    print(f'The best student is ',key)
   
  if st_marks[key]==worse:
    print(f'The worse student is ',key)