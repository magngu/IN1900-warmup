# primes.py
# Python 3.10.1
# Author Magnus // Feb 2022
# ------------------------------------------------------------------------------


def read_file(file='primes_data.txt'):
    """Takes file_path of excercise file and return two sorted tuples, n and pi_n."""
    with open(file, 'r') as file:
        n = file.readline().split()[1:]
        pi_n = file.readline().split()[1:]

    # Convert to integers and sort zipped lists
    n = [eval(el) for el in n]
    pi_n = [int(el) for el in pi_n]
    t1, t2 = zip(*sorted(zip(n, pi_n)))  # Maps the lists to anoher, then sort, then unpack to t1, t2

    return t1, t2


def write_table(n, pi_n, file='primes_table.txt'):
    """Outputs table of n & pi(n) to a file."""
    with open(file, 'w') as file:
        # Header
        file.write('----------------------------------\n')
        file.write('|' + ' '*4 + 'n' + ' '*4 + '|' +  ' '*9 + 'pi(n)' + ' '*8 + '| \n' )
        file.write('----------------------------------\n')

        # Fill table with data
        for x, y in zip(n, pi_n):
            file.write(f'|  {x:5.0E}  | {y:20.0f} |\n')

        # Footer
        file.write('----------------------------------')


def test_read_file():
    """Test function for test_read_file. Generates file to test with."""
    from math import log

    # Generate test data
    n    = ['10**20', '10**4', '10**2', '10**1', '10**12', '10**4', '10**6', '10**15']
    pi_n = ['2220819602560918840', '1229', '25', '4', '37607912018', '168', '78498', '29844570422669']

    # Write data to file
    with open('test_read_file.txt', 'w') as file:
        file.write ('n: ')
        for el in n:
            file.write(el)
            file.write(' ')
        file.write('\n')

        file.write('pi_n: ')
        for el in pi_n:
            file.write(el)
            file.write(' ')

    # Call function to be tested
    t1, t2 = read_file(file='test_read_file.txt')

    # Compare results
    exp1 = (10, 100, 10000, 10000, 1000000, 1000000000000, 1000000000000000, 100000000000000000000)
    exp2 = (4, 25, 168, 1229, 78498, 37607912018, 29844570422669, 2220819602560918840)
    success = exp1 == t1 and exp2 == t2
    assert success, f'{exp1, exp2} was expected, but {t1, t2} was calcualted.'

# Code to generate output for test run
n, pi_n = read_file()
write_table(n, pi_n)

'''
Test run:
>>>python3 primes.py
>>>

Output file 'primes_table.txt':
----------------------------------
|    n    |         pi(n)        | 
----------------------------------
|  1E+01  |                    4 |
|  1E+02  |                   25 |
|  1E+04  |                  168 |
|  1E+04  |                 1229 |
|  1E+06  |                78498 |
|  1E+12  |          37607912018 |
|  1E+15  |       29844570422669 |
|  1E+20  |  2220819602560918784 |
----------------------------------
'''