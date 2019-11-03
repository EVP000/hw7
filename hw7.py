# program name: hw7.py
# required arguments: data_file (eg. diabetes.data)
# optional arguments: --plot/-p + 2 column names (eg. -p bmi sex)
#                     --debug/-x
#                     --header/-H to determine if a line of headers is present
#                     --summary/-s + 1 column name (eg. -s glu)
#                     --interpolate/-i + 2 columns + 1 x value (eg. -i y glu 300)
# 
# <github path - COPY PATH still not working for me ?? 
# From the navigation line: https://github.com/EVP000/hw7/blob/master/hw7.py> 
# https://travis-ci.org/EVP000/hw7

print('========================================================================================')
print('========================================================================================')

print('> start of program hw7.py')
print('> ONLY USES DIABETES.DATA ')
print('> import libraries')

import argparse
import os.path as op
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit

print('> define convert_type function')
def convert_type(data_value):
    try:
        return int(data_value)
    except ValueError:
        try:
            return float(data_value)
        except ValueError:
            return data_value

print("> define get_delim function")
def get_delim(sourcefile1):
    print('> executing get_delim function')
    data = open(sourcefile1, 'r') 
    my_read_data = data.read()
    if my_read_data.find(',') > 0:
        print('    delimiter: comma')
        return ','
    else:
        print('    delimiter: space')
        return ' '      
    print(' ')

def lines_to_dict(lines, header=False):
    print('> executing lines_to_dict')
    if header:
        column_titles = lines[0]
        lines = lines[1:]
    else:
        column_titles = list(range(1, len(lines[0])+1))
    
    data_dict = {}
    for idx, column in enumerate(column_titles):
        data_dict[column] = []
        for row in lines:
            data_dict[column] += [row[idx]]
    return data_dict

def parse_file(data_file, dlm, debug=False):   # took delimiter out
    print('> executing parse_file')
    # Verify the file exists
    assert(op.isfile(data_file))

    # open it as a csv 
    with open(data_file, 'r') as fhandle:
        csv_reader = csv.reader(fhandle, delimiter=dlm)
        # Add each line in the file to a list
        lines = []
        if debug:
            count = 0
        for line in csv_reader:
            if debug:
                if count > 2:
                    break
                count += 1
            newline = []
            for value in line:
                newline += [convert_type(value)]
            if len(newline) > 0:
                lines += [newline]

    print('> view a few lines')
    print(' ')
    for line in lines[0:2]:
        print(line)
    print(' ')
    # Return all the contents of our file
    return lines

print('> define key_exist function')
def key_exist(dd, chkkey):
    print('> does ', chkkey, 'exist?')
    if chkkey in dd:
        print("    Yes")
    else:
        print("    No, quitting")    
        exit()

def plot_data(dd, col1, col2, debug=False):
    print('> executing plot_data function')
    
    # dd stands for data_dictionary
    #if debug:
    # ncol = len(dd)
    # print('    number of columns:', ncol)
    # fig = plt.figure()
    #fig.tight_layout()
    # j = 0   
    # for col1 in dd.keys():
    #     for col2 in dd.keys():
    #         j += 1
    #         # create numpy arrays  eg. vals = np.fromiter(Samples.values(), dtype=float)
    #         x = np.fromiter(dd[col1], dtype=float)
    #         y = np.fromiter(dd[col2], dtype=float)
            
    #         print('> creating subplot for x=', col1, ', y=', col2, ', j=', j)
    #         #plt.subplot(ncol, ncol, j) 
    #         fig.add_subplot(ncol, ncol, j)
    #         plt.scatter(x, y)
    #         xp = np.linspace(np.amin(x), np.amax(x), 100)  #only works for numpy arrays
    #         for degree in range(1,5):
    #             weights = np.polyfit(x, y, degree)
    #             model = np.poly1d(weights)
    #             plt.plot(xp, model(xp), '-', label='degree='+ str(degree))

    #         plt.xlabel(col1, size=6)
    #         plt.ylabel(col2, size=6)
    #         plt.title(col1 + ' x ' + col2.format(x,y), size=6)
             
    #         plt.legend()  #looks even worse with the legend so removing for now
    #         plt.tight_layout()  # UserWarning: Tight layout not applied. cannot make axes height small enough to accommodate all axes decorations
    # plt.savefig("subplots.png")
    # plt.show()   # total garbage, overlapping


    # Same as above but only a few, in full scale to be able to see the output
    
    print('> plotting ', col1, 'x', col2)
    key_exist(dd, col1)
    key_exist(dd, col2)
    
    x = np.fromiter(dd[col1], dtype=float)
    y = np.fromiter(dd[col2], dtype=float)
    plt.scatter(x, y)
    xp = np.linspace(np.amin(x), np.amax(x), 100)  #only works for numpy arrays
    for degree in range(1,4):
        weights = np.polyfit(x, y, degree)
        model = np.poly1d(weights)
        plt.plot(xp, model(xp), '-', label='degree='+ str(degree))
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(col1 + ' x ' + col2.format(x,y))
    plt.legend()
    plt.savefig("plot_" + col1 + '_' + col2 + ".png")
    plt.show()

    # i = 0   
    # for col1 in dd.keys():
    #     for col2 in dd.keys():
    #         i += 1
    #         if i < 8:  # remove this IF condition to create all
    #             print('> creating plot for x=', col1, ', y=', col2, ', i=', i)
    #             # create numpy arrays  eg. vals = np.fromiter(Samples.values(), dtype=float)
    #             x = np.fromiter(dd[col1], dtype=float)
    #             y = np.fromiter(dd[col2], dtype=float)

    #             plt.scatter(x, y)
    #             xp = np.linspace(np.amin(x), np.amax(x), 100)  #only works for numpy arrays
    #             for degree in range(1,5):
    #                 weights = np.polyfit(x, y, degree)
    #                 model = np.poly1d(weights)
    #                 plt.plot(xp, model(xp), '-', label='degree='+ str(degree))
                
    #             plt.xlabel(col1)
    #             plt.ylabel(col2)
    #             plt.title(col1 + ' x ' + col2.format(x,y))
    #             plt.legend()
    #             plt.savefig("lgf" + str(i) + ".png")
    #             plt.show()

    # if debug:
    #     print(len(dd.keys()), n)
    # return 0
    
print('> define get_type function')
def get_type(df, col, debug=False):
    print('> executing get_type')
    if isinstance(df[col], str):
        type = 'string'
    else:
        nuval = df[col].nunique()  # number of unique values 
        nvals = df[col].count()    # total number of values
        pct = nuval/nvals * 100
        print('    number of unique values: ' , nuval)
        print('    number of non-null values: ', nvals)
        print('    percent of unique values/total values: ', pct)
        if pct < 20:
            type = 'categorical'
        else:
            type = 'continuous'    
    print('    type: ', type)
    return type
    

print('> define sumstats function')
def sumstats(dd, col, debug=False):
    print('> generating summary statistics for ', col)
    key_exist(dd, col)  
    df = pd.DataFrame(dd, columns = [col])    
    type = get_type(df, col)
    if type == 'string':
        print('    quitting')
        exit()
    # create numpy arrays  eg. vals = np.fromiter(Samples.values(), dtype=float)
    # x = np.fromiter(dd[col], dtype=float)
    # create dataframe
    else:
        print('> summary statistics ')
        print('    mean: ', df[col].mean() )
        print('    min: ', df[col].min() )
        print('    max: ', df[col].max() )
        print('    std: ', df[col].std() )
  

print('> define interp function')
def interp(dd, col1, col2, xvalue, debug=False):
    print('> executing interp function')
    key_exist(dd, col1)
    key_exist(dd, col2)
    df = pd.DataFrame(dd, columns = [col1]) 
    min_value = df[col1].min()
    max_value = df[col1].max()
    xvalue = float(xvalue)
    if xvalue >= min_value and xvalue <= max_value:
        print('    value provided is within the range of values')
        type = get_type(df, col1)
        if type != 'continuous':
            print('    does not make sense to interpolate with this type of data')
        else:
            x = np.fromiter(dd[col1], dtype=float)
            y = np.fromiter(dd[col2], dtype=float)
            print(' ')
            print('    for', col1, '=', xvalue,':')
            for degree in range(1,4):
                weights = np.polyfit(x, y, degree)
                model = np.poly1d(weights)
                # print(' model: ', model)
                yint = model(xvalue)
                print('    degree =', degree, ' interpolated', col2, 'value: ', yint)
    else:
        print('    value provided (', xvalue, ') is not within the range of', col1, 'values')
        sumstats(dd, col1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file",      type=str,            
        help="Input CSV data file for plotting")
    parser.add_argument('-p', '--plot',   type=str, nargs = 2,
        help='2 columns to plot')
    parser.add_argument('-x', '--debug',  action="store_true", 
        help="only prints start of file")
    parser.add_argument('-H', '--header', action="store_true", 
        help="determines if a header is present")
    parser.add_argument('-s', '--summary', type=str, 
        help='column for summary statistics')
    parser.add_argument('-i', '--interpolate', type=str, nargs = 3,     
        help='two column names and a value for the first column')

    args = parser.parse_args()
    print(' ')
    print('    args:', args)
    print(' ')

    dlm = get_delim(args.data_file)    
    my_data = parse_file(args.data_file, dlm, debug=args.debug)

    data_dictionary = lines_to_dict(my_data, header=args.header)
    #print(data_dictionary)

    #print('args.plot:',args.plot)
    if args.plot != None: 
        plot_data(data_dictionary, col1= args.plot[0], col2= args.plot[1], debug=args.debug)
    else:
        print('> plot argument missing, not plotting')


    # guess as to whether or not the data in that column is continuous or categorical/discrete.
    #print('args.summary:', args.summary)
    if args.summary != None:
        sumstats(data_dictionary, args.summary, debug=args.debug)
    else:
        print('> summary arguments missing, not producing summary statistics')   

    if args.interpolate != None:
        interp(data_dictionary, col1 = args.interpolate[0], col2 = args.interpolate[1], xvalue = args.interpolate[2], debug = args.debug)
    else:
        print('> interpolate arguments missing, not performing interpolation') 

if __name__ == "__main__":
    main()
