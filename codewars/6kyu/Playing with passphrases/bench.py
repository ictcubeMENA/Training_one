import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.play_pass("I LOVE YOU!!!", 1)
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.play_passB("I LOVE YOU!!!", 1)
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()
#spent time for my solution: 0.10097540299999996
#spent time for the best practice : 0.138099686