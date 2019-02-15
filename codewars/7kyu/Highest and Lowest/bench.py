import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.high_and_lowB("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()

#spent time for my solution: 0.12444421300000003
#spent time for the best practice : 0.06959448299999993