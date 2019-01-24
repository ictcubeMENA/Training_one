import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.movie(500, 15, 0.9)
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.movieB(500, 15, 0.9)
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()
#spent time for my solution: 0.44245010900000004
#spent time for the best practice : 0.4160948980000003
