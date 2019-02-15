import timeit
def benchmarkvalidsolution():
    setup_code ='''
import main'''
    test_code =  '''
main.validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]) 
    '''
    
    times = timeit.repeat(setup = setup_code,stmt = test_code,
                          repeat = 3, 
                          number = 10000)
    
    print('validate solution time for my solution: {}'.format(min(times)))


def benchmarkvalidsolutionB():
    setup_code = '''
import main'''
    test_code = '''
main.validSolutionB([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]) 
    '''

    times = timeit.repeat(setup=setup_code, stmt=test_code,
                          repeat=3,
                          number=10000)

    print('validate solution time for the best practice : {}'.format(min(times)))
if __name__ == '__main__':
    benchmarkvalidsolution()
    benchmarkvalidsolutionB()


#validate solution time: 0.6132896480000001
#validate solution time for the best practice : 0.06698157500000024
