# temp_read_write.py
# Python 3.10.1
# Author Magnus // Feb 2022
# ------------------------------------------------------------------------------
import numpy as np

def extract_data(filename):
    '''Reads given file and returns list with temperatures as floats.'''
    with open(filename, 'r') as file:
        file.readline() # Skip header
        values = [line.split() for line in file]
   
    return [float(num) for el in values for num in el]    # Flatten list and convert elements to float


def print_results():
    '''Prints results from calulcations. Function iot clean up the program.'''
    # Header
    print('|' + '-'*27 + '|')
    print('|' + ' Year  ' + '|' + '   1945' + '  |  ' + ' 2014  ' + '|')
    print('|' + '-'*27 + '|')
    # Populate table with data
    print(f'| Mean  |  {avg_1945:5.2f}  |  {avg_2014:5.2f}  | ')
    print(f'| Max   |  {max_1945:5.2f}  |  {max_2014:5.2f}  | ')
    print(f'| Min   |  {min_1945:5.2f}  |  {min_2014:5.2f}  | ')
    #Footer
    print('|' + '-'*27 + '|')
    print('|   All values in Celsius   |')
    print('|' + '-'*27 + '|')


def write_formatting(filename, list1, list2):
    '''Writes descriptive statistics to file.'''
    width = 27 #width of table
    write_dashes = lambda : file.write('|' + '-'*(width-2) + '|\n')

    with open(filename, 'w') as file:
        # Header
        write_dashes() 
        file.write(f'| {1945:7.0f}    | {2014:7.0f}    |\n')
        write_dashes() 
        
        # Populate table with data
        for x, y in zip(list1, list2):
            file.write(f'|   {x:5.2f}    |   {y:5.2f}    |\n')
        
        #Footer
        write_dashes() 
        file.write('|  All values in Celsius  |\n')
        write_dashes() 


oct_1945 = extract_data('temp_oct_1945.txt')
oct_2014 = extract_data('temp_oct_2014.txt')

# Calculate descriptive statistics
avg_1945 = np.mean(oct_1945)
avg_2014 = np.mean(oct_2014)
max_1945 = np.max(oct_1945)
max_2014 = np.max(oct_2014)
min_1945 = np.min(oct_1945)
min_2014 = np.min(oct_2014)

print_results()
write_formatting('temp_output_file.txt', oct_1945, oct_2014)


'''
Test run:
>>>python3 temp_read_write.py
|---------------------------|
| Year  |   1945  |   2014  |
|---------------------------|
| Mean  |   6.51  |   8.85  | 
| Max   |  11.60  |  13.60  | 
| Min   |   2.10  |   2.30  | 
|---------------------------|
|   All values in Celsius   |
|---------------------------|
>>>

temp_output_file.txt
|-------------------------|
|    1945    |    2014    |
|-------------------------|
|    7.20    |    9.80    |
|    8.10    |   11.60    |
|    8.90    |   11.50    |
|   11.60    |   13.30    |
|    7.70    |   12.60    |
|    8.70    |   10.30    |
|    6.90    |    7.50    |
|    5.40    |    9.30    |
|    8.80    |   10.30    |
|    8.90    |   10.30    |
|    3.70    |    8.40    |
|    3.30    |    8.80    |
|    5.20    |    5.00    |
|    9.60    |    5.80    |
|   10.80    |    6.80    |
|    5.00    |    2.30    |
|    5.40    |    3.50    |
|    9.50    |    7.90    |
|    5.30    |   11.80    |
|    5.80    |   10.70    |
|    2.30    |    9.00    |
|    4.10    |    5.80    |
|    6.60    |    6.80    |
|    8.20    |   11.70    |
|    6.10    |   10.60    |
|    8.90    |   11.70    |
|    6.60    |   13.10    |
|    4.10    |   13.60    |
|    2.80    |    8.00    |
|    2.10    |    3.50    |
|    4.10    |    3.20    |
|-------------------------|
|  All values in Celsius  |
|-------------------------|
'''