# Ruby Starter

This is the Ruby starter.

## Prerequisites

- Install node via one of these means
  - [Homebrew](https://brew.sh/): `brew install ruby`
  - [Rbenv](https://github.com/rbenv/rbenv)
  - [RVM](https://rvm.io/)
  - https://www.ruby-lang.org/en/documentation/installation/

- `bundle install`

## Running tests

`bundle exec rspec`

## Behind the scenes

### Test Runner

[RSpec](http://rspec.info/)

#### Common [Expectations](https://relishapp.com/rspec/rspec-expectations/v/3-8/docs/built-in-matchers)
- `expect(actual).to be(expected)` for object equivalence (same instance)
- `expect(actual).to eql(expected)` for object value equivalence

### Mocking library

[RSpec mocks](https://relishapp.com/rspec/rspec-mocks/docs)
