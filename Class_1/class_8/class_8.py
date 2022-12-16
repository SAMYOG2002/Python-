# More about Dictionary 

dict = {'a':'home','b':'school','C':'college'}
dict["new"] = 3
print (dict)
net = dict.items()
print(net)
print(dict['a']=='home')
print(dict.pop('a'))
print(len(dict))
print(dict.popitem())
print(dict.update({'d': None}))
print(dict.get('b'))
dict["new_dict"] = {1: 'one', 2:'two'}
print(dict)

## Nested Dictionaries

sagarmatha = {
    "Department":{
        "Computer Engineering":{
            "HOD":"Bharat Bhatta", 
            "NO of teachers":20
        },
        "Civil Engineering":{
            "HOD":"Sudip Lamsal",
            "NO of teachers":20
        },
        "Exam Department":{
            "HOD":"Chaturbhuj Nepali",
            "NO of teachers":10
        }
    }    
}
print(sagarmatha)

