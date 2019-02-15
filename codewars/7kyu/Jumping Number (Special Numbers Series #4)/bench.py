import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.jumping_number(7)
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.jumping_numberB(7)
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()

#spent time for my solution: 0.005605549000000001
#spent time for the best practice : 0.020394675