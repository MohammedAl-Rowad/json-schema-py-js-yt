from jsonschema import Draft7Validator
from json import load

with open('schema.json') as f:
    schema = load(f)

list_ = [
    {'name': 'rowadz', 'age': -1, 'salary': 100},
    {'name': 'fasdkjfkasld;jfkfasdfasdfasdfasdasld;jfas;dlkfjkasld', 'age': 24},
    {'name': 'sarah', 'age': 35}
]

validator = Draft7Validator(schema)


print(list(validator.iter_errors(list_)))