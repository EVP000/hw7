print('========================================================================================')
print('========================================================================================')
# to call python hw6.py diabetes.data -H
# <github path - COPY PATH still not working for me ?? > 
print('> Hello, start of program hw7.py')
print('test line')
print('> ONLY USED DIABETES.DATA')
print('> import libraries')

import argparse
import os.path as op
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit

print('> define functions')
def convert_type(data_value):
    try:
        return int(data_value)
    except ValueError:
        try:
            return float(data_value)
        except ValueError:
            return data_value

print("> define GET_DELIM function")
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
    for line in lines[0:2]:
        print(line)
    print(' ')
    # Return all the contents of our file
    return lines

def plot_data(dd, debug=False):
    print('> executing plot_data')
    # dd stands for data_dictionary
    #if debug:
    ncol = len(dd)
    print('    number of columns:', ncol)
    fig = plt.figure()
    #fig.tight_layout()
    j = 0   
    for col1 in dd.keys():
        for col2 in dd.keys():
            j += 1
            # create numpy arrays  eg. vals = np.fromiter(Samples.values(), dtype=float)
            x = np.fromiter(dd[col1], dtype=float)
            y = np.fromiter(dd[col2], dtype=float)
            
            print('> creating subplot for x=', col1, ', y=', col2, ', j=', j)
            #plt.subplot(ncol, ncol, j) 
            fig.add_subplot(ncol, ncol, j)
            plt.scatter(x, y)
            xp = np.linspace(np.amin(x), np.amax(x), 100)  #only works for numpy arrays
            for degree in range(1,5):
                weights = np.polyfit(x, y, degree)
                model = np.poly1d(weights)
                plt.plot(xp, model(xp), '-', label='degree='+ str(degree))

            plt.xlabel(col1, size=6)
            plt.ylabel(col2, size=6)
            plt.title(col1 + ' x ' + col2.format(x,y), size=6)
             
            #plt.legend()  #looks even worse with the legend so removing for now
            plt.tight_layout()  # UserWarning: Tight layout not applied. cannot make axes height small enough to accommodate all axes decorations
    plt.savefig("subplots.png")
    plt.show()   # total garbage, overlapping

    print(' ')
    # Same as above but only a few, in full scale to be able to see the output
    i = 0   
    for col1 in dd.keys():
        for col2 in dd.keys():
            i += 1
            if i < 8:  # remove this IF condition to create all
                print('> creating plot for x=', col1, ', y=', col2, ', i=', i)
                # create numpy arrays  eg. vals = np.fromiter(Samples.values(), dtype=float)
                x = np.fromiter(dd[col1], dtype=float)
                y = np.fromiter(dd[col2], dtype=float)

                plt.scatter(x, y)
                xp = np.linspace(np.amin(x), np.amax(x), 100)  #only works for numpy arrays
                for degree in range(1,5):
                    weights = np.polyfit(x, y, degree)
                    model = np.poly1d(weights)
                    plt.plot(xp, model(xp), '-', label='degree='+ str(degree))
                
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.title(col1 + ' x ' + col2.format(x,y))
                plt.legend()
                plt.savefig("lgf" + str(i) + ".png")
                plt.show()

    if debug:
        print(len(dd.keys()), n)
    return 0
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", type=str,
                        help="Input CSV data file for plotting")
    #parser.add_argument("delimiter", type=str, help="the delimiter used in your file")
    parser.add_argument('-x', '--debug', action="store_true",
                        help="only prints start of file")
    parser.add_argument('-H', '--header', action="store_true",
                        help="determines if a header is present")
    
    args = parser.parse_args()
    print('    args:', args)
    dlm = get_delim(args.data_file)    
    #my_data = parse_file(args.data_file, args.delimiter, debug=args.debug)
    my_data = parse_file(args.data_file, dlm, debug=args.debug)

    data_dictionary = lines_to_dict(my_data, header=args.header)
    #print(data_dictionary)

    print(' ')
    plot_data(data_dictionary, debug=args.debug)


if __name__ == "__main__":
    main()