import hello from './hello'

const kenya = { name: 'Kenya' }

describe('hello', () => {
  it('says hello', () => {
    expect(hello(kenya)).toEqual('Hello, Kenya!')
  })
})
