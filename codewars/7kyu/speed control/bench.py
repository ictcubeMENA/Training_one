import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
s = 20
main.gps(s, x)
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
s = 20
main.gpsB(s, x)
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()
#spent time for my solution: 0.07015981699999999
#spent time for the best practice : 0.032372067000000004