import { lives } from './gameOfLife'

describe('Game of life', () => {
  const living = () => ({ isLiving: true })
  const dead = () => ({ isLiving: false })

  describe('Any live cell', () => {
    const cell = living()

    describe('with zero live neighbors', () => {
      const neighbors = [ dead(), dead(), dead(), dead() ]

      it('dies, as if by underpopulation', () => {
        expect(lives(cell, neighbors)).toEqual(false)
      })
    })
    describe('with one live neighbor', () => {
      const neighbors = [ living(), dead(), dead(), dead() ]

      xit('dies, as if by underpopulation', () => {
        expect(lives(cell, neighbors)).toEqual(false)
      })
    })
    describe('with two live neighbors', () => {
      const neighbors = [ living(), living(), dead(), dead() ]

      xit('lives on to the next generation.', () => {
        expect(lives(cell, neighbors)).toEqual(true)
      })
    })
    describe('with three live neighbors', () => {
      xit('lives on to the next generation.', () => {
      })
    })
    describe('with four live neighbors', () => {
      xit('dies, as if by overpopulation', () => {
      })
    })
  })

  describe('Any dead cell', () => {
    describe('with zero live neighbors', () => {
      xit('remains dead', () => {
      })
    })
    describe('with one live neighbor', () => {
      xit('remains dead', () => {
      })
    })
    describe('with two live neighbors', () => {
      xit('lives on to the next generation.', () => {
      })
    })
    describe('with three live neighbors', () => {
      xit('lives on to the next generation.', () => {
      })
    })
    describe('with four live neighbors', () => {
      xit('dies, as if by overpopulation', () => {
      })
    })
  })
})
