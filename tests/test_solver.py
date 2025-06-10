from src.nonogram_solver import calculate_fitness, random_initial_state, validate_constraints

def test_random_initial_state():
    state = random_initial_state(5, 5)
    assert len(state) == 5
    assert all(len(row) == 5 for row in state)
    assert all(cell in [0, 1] for row in state for cell in row)

def test_calculate_fitness_perfect():
    state = [[1, 1], [1, 1]]
    row_constraints = [[2], [2]]
    col_constraints = [[2], [2]]
    assert calculate_fitness(state, row_constraints, col_constraints) == 4

def test_validate_constraints_pass():
    rows = 5
    cols = 5
    row_constraints = [[2], [1,1], [1], [3], [1]]
    col_constraints = [[1], [3], [1], [2], [1]]
    valid, message = validate_constraints(rows, cols, row_constraints, col_constraints)
    assert valid

def test_validate_constraints_fail_length():
    row_constraints = [[6]]
    col_constraints = [[1]]
    valid, message = validate_constraints(1, 5, row_constraints, col_constraints)
    assert not valid
