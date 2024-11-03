import json

# courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'
#
# #Loads method parse json string and it returns dictionary
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['name'])
# #get me the first language taught by trainer
# # list_language = dict_courses['languages']
# # print(type(list_language))
# # print(list_language[0])
# print(dict_courses['languages'][0])

#****** Parse content present in Json file
# "C:\Users\0G3425649\Desktop\jsonforpythonpractise.txt"
#with open('C:\\Users\\0G3425649\\Desktop\\jsonforpythonpractise.txt') as f:
with open(r'C:\Users\0G3425649\Desktop\jsonforpythonpractise.txt') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))

# Price of course "RPA"
    print(type(data['courses']))
    for course in data['courses']:
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45

with open('C:\\Users\\0G3425649\\Desktop\\jsonforpythonpractise2.txt') as fi:
    data2 = json.load(fi)
    assert data == data2