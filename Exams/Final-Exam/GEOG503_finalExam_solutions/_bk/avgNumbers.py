# avgNumbers.py
# Purpose:  Practice parsing numeric tables.
# Usage: fullpath_filename output_directory
# Output: output file out.txt containing average row values of input file.
# Example input: C:/gispy/data/ch19/crop_yield.txt C:/gispy/scratch

import sys, os

try:
    ifilename = sys.argv[1]
    theDir = os.path.dirname(ifilename)
    ofilename = sys.argv[2] + '/out.txt'
except IndexError:
    print 'Warning: failed to run.'
    print 'Usage: Full path input filename'
    sys.exit(0)
try:
    with open(ifilename, 'r') as infile:
        with open(ofilename, 'w') as outfile:
            for line in infile:
                lineList = line.split()
                lineList = [float(x) for x in lineList]
                x = sum(lineList)
                avg = x/len(lineList)
                outfile.write(str(avg) + '\n')
            infile.close()
            outfile.close()
    print '{0} created.'.format(ofilename)
except IOError:
    print 'Warning: {0} could not be opened.'.format(ifilename)
