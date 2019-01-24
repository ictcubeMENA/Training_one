import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB")
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.composeB("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB")
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()