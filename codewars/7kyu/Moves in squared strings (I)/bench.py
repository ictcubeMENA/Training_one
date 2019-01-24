import timeit

def benchmarkarraydiff():
    setup_code ='''
import main'''
    test_code =  '''
main.vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu")
main.hor_mirror("lVHt\nJVhv\nCSbg\nyeCt")
    '''
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('spent time for my solution: {}'.format(min(times)))


def benchmarkarraydiffB():
    setup_code = '''
import main'''
    test_code = '''
main.vert_mirrorB("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu")
main.hor_mirrorB("lVHt\nJVhv\nCSbg\nyeCt")
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('spent time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkarraydiff()
    benchmarkarraydiffB()