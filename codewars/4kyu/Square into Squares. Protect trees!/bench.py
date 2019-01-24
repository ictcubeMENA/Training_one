import timeit

def benchmarksquareintosquares():
    setup_code = '''
import main'''
    test_code =  '''
main.decompose(5)'''

    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spended time for my solution: {}'.format(min(times)))


def benchmarksquareintosquaresB():
    setup_code = '''
import main'''
    test_code = '''
main.decomposeB(5)'''


    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spended time for the best practice : {}'.format(min(times)))


if __name__ == '__main__':
    benchmarksquareintosquares()
    benchmarksquareintosquaresB()

#spended time for my solution: 0.016454407000000004
#spended time for the best practice : 0.028180066000000004
