
d = {
  'INTERNATIONAL':{
    'xxs' : 'xxs',
    'xs':'xs',
    's' :'s',
    "m":'m',
    "l" :'l',
    "xl":'xl',
    'xxl':'xxl',
    'xxxl' :'xxxl'},
  'DE':{
    'xxs' : '36',
    'xs':'38',
    's' :'40',
    "m":'42',
    "l" :'44',
    "xl":'46',
    'xxl':'48',
    'xxxl' :'50'},
  'USD':{
    'xxs' : '8',
    'xs':'10',
    's' :'12',
    "m":'14',
    "l" :'16',
    "xl":'18',
    'xxl':'20',
    'xxxl' :'22'},
  'FR':{
    'xxs' : '38',
    'xs':'40',
    's' :'42',
    "m":'44',
    "l" :'46',
    "xl":'48',
    'xxl':'50',
    'xxxl' :'52'},
  'GB':{
    'xxs' :'24',
    'xs':'26',
    's' :'28',
    "m":'30',
    "l" :'32',
    "xl":'34',
    'xxl':'36',
    'xxxl' :'38'},
}
size = d.get('GB').get('xxl')
print(size)

