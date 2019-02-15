import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.count_animals("I see 3 zebras, 5 lions and 6 giraffes.")
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.count_animalsB("I see 3 zebras, 5 lions and 6 giraffes.")
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()
#spent time for my solution: 0.03591169500000002
#spent time for the best practice : 0.06533677399999993