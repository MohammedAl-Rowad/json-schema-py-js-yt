const Ajv = require('ajv')
const schema = require('./schema.json')

const ajv = new Ajv({ allErrors: true })

const array = [
  { name: 'rowadz', age: -1, salary: 100 },
  { name: 'fasdkjfkasld;jfkfasdfasdfasdfasdasld;jfas;dlkfjkasld', age: 24 },
  { name: 'sarah', age: 35 },
]

const validate = ajv.compile(schema)

validate(array)

console.log(validate.errors)
