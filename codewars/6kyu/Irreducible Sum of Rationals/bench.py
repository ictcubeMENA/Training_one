import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.sum_fracts([[1, 2], [1, 3], [1, 4]])
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.sum_fractsB([[1, 2], [1, 3], [1, 4]])
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()

#spent time for my solution: 0.2413910359999999
#spent time for the best practice : 0.23428874
