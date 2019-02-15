import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
a = [1, 2, 3, 4, 5]
b = [10, 0, 10, 0, 10]
main.fmax(a,b)
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
a = [1, 2, 3, 4, 5]
b = [10, 0, 10, 0, 10]  
main.fmaxB(a,b)
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()

#spent time for my solution: 0.021624756000000002
#spent time for the best practice : 0.025832544000000013