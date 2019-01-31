from challenge_decompress_a_string import solve

def test_solve_first_example():
    assert(solve('3[abc]4[ab]c') == 'abcabcabcababababc')

def test_solve_recursion_example():
    assert(solve('2[3[a]b]') == 'aaabaaab')