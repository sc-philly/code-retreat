# JavaScript Starter

This is the JavaScript starter.

## Prerequisites

- Install node via one of these means
  - [Homebrew](https://brew.sh/): `brew install node`
  - [Nodenv](https://github.com/nodenv/nodenv)
  - [NVM](https://github.com/creationix/nvm)
  - https://nodejs.org/en/download/

- `npm install`

## Running tests

`npm test`

## Behind the scenes

### Transpilation

[babel](https://babeljs.io/) with [@babel/preset-env](https://babeljs.io/docs/en/babel-preset-env) for the latest JS features

### Test Runner

[ava](https://github.com/avajs/ava) with [@babel/register](https://babeljs.io/docs/en/babel-register) to transpile source files that are imported by test files.

Common [Assertions](https://github.com/avajs/ava/blob/master/docs/03-assertions.md)
`t.is` for value equality
`t.deepEqual` for deep equality checking of objects and arrays
`t.truthy` / `t.falsey` for truthy / falsey tests

### Mocking library

[testdouble](https://github.com/testdouble/testdouble.js)
