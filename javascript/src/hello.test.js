import test from 'ava'
import hello from './hello'

const kenya = { name: 'Kenya' }

test('says hello', (t) => {
  t.is(hello(kenya), 'Hello, Kenya!')
})
