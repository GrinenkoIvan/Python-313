data = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

name = 'name'
salary = 'salary'

dictionary = {
    name: data.pop(name),
    salary: data.pop(salary)
}

print(data)
print(dictionary)
