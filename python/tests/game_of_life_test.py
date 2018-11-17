from game_of_life import lives, LIVING, DEAD

# Game of Life
class TestGameOfLife(object):

    # Any live cell
    class TestAnyLiveCell(object):

        # with zero live neighbours
        class TestZeroLiveNeighbours(object):

            # dies, as if by underpopulation
            def test_dies_by_underpopulation(self):
                CELL = LIVING
                NEIGHBOURS = [ DEAD, DEAD, DEAD, DEAD ]
                assert lives(CELL, NEIGHBOURS) == False

        # with one live neighbor
        class TestOneLiveNeighbours(object):

            # dies, as if by underpopulation
            def test_dies_by_underpopulation(self):
                CELL = LIVING
                NEIGHBOURS = [ LIVING, DEAD, DEAD, DEAD ]
                assert lives(CELL, NEIGHBOURS) == False

        # with two live neighbors
        class TestTwoLiveNeighbours(object):

            # lives on to the next generation.
            def test_lives_on_to_the_next_generation(self):
                CELL = LIVING
                NEIGHBOURS = [ LIVING, LIVING, DEAD, DEAD ]
                assert lives(CELL, NEIGHBOURS) == True

        # with three live neighbors
        class TestThreeLiveNeighbours(object):

            # lives on to the next generation.
            def test_lives_on_to_the_next_generation(self):
                CELL = LIVING
                NEIGHBOURS = [ LIVING, LIVING, LIVING, DEAD ]
                assert lives(CELL, NEIGHBOURS) == True

        # with four live neighbors
        class TestFourLiveNeighbours(object):

            # dies, as if by overpopulation
            def test_dies_by_underpopulation(self):
                CELL = LIVING
                NEIGHBOURS = [ LIVING, LIVING, LIVING, LIVING ]
                assert lives(CELL, NEIGHBOURS) == False

    # Any dead cell
        # with zero live neighbors
            # remains dead
        # with one live neighbor
            # remains dead
        # with two live neighbors
            # lives on to the next generation.
        # with three live neighbors
            # lives on to the next generation.
        # with four live neighbors
            # dies, as if by overpopulation
