dict_values1=dict(name="Ram",age=21)
print(type(dict_values1))
print(dict_values1)

dict_values={"place":"Madurai"}
dict_values["name"]="mekha"
print(type(dict_values))
print(dict_values)

values={
    "fruits-1":"Apple",
    "fruits-2":"orange",
    "fruits-3":"Grapes",
    "fruits-4":"kiwi",
    "fruits-5":"jack",
    }
print(list(values.items()))
print(list(values.keys()))
print(list(values.values()))

for k,v in values.items():
    print(k,v)
for fruitId in values.keys():
    print(fruitId)
for fruitvalues in values.values():
    print(fruitvalues)

squareNum={i:i*i for i in range(1,6)}
print(squareNum)
evensquares=[i**2 for i in range(1,1) if i%2==0]
print(evensquares)
evensquares=[i**2 if i%2==1 else 0 for i in range(1,11)]
print(evensquares)

