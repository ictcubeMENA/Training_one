import timeit
def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.array_diff([1,2],[1])
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.array_diffB([1,2],[1])
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()


#spent time for my solution: 0.008481709999999996
#spent time for the best practice : 0.008359682999999993
