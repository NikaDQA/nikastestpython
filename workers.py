
workers = {
  'with_education':{
    'engineer' : '1000',
    'teacher':'800',
    'doctor' :'1000',
    "manager":'800'},
  'without_education':{
    'cleaner' : '600',
    'zoo_keeper':'1000',
    'hairdresser' :'800',
    "nail_master":'2000'},
  'time':{
    'engineer' : '8',
    'teacher':'6',
    'doctor' :'4',
    "manager":'12',
    'cleaner' : '6',
    'zoo_keeper':'8',
    'hairdresser' :'12',
    "nail_master":'16'
  }
}

def workertime(education,time):
  if education == 'with_education':
    print(workers.get('with_education').get(time)) 
    print(workers.get('time').get(time)) 
  elif education == 'without_education':
    print(workers.get('without_education').get(time))
    print(workers.get('time').get(time))
  else:
    print('error')

workertime('without_education','nail_master')




