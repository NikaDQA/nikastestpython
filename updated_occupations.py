


occupations = [{
  'title': 'engineer',
  'salary': 1000,
  'time': 160,
  'education_required': True,
  'education_type': 'technical'
},
{
  'title': 'teacher',
  'salary': 800,
  'time': 120,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'doctor',
  'salary': 1000,
  'time': 80,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'manager',
  'salary': 800,
  'time': 240,
  'education_required': True,
  'education_type': 'humanitarian'
},
{
  'title': 'cleaner',
  'salary': 600,
  'time': 120,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'zoo_keeper',
  'salary': 1000,
  'time': 160,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'hairdresser',
  'salary': 800,
  'time': 240,
  'education_required': False,
  'education_type': ''
},
{
  'title': 'nail_master',
  'salary': 2000,
  'time': 320,
  'education_required': False,
  'education_type': ''
}]


def work():
  import random
  k= random.choice(occupations)
  print(k)

work()
