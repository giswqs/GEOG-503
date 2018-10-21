ifilename = "data/crop_yield.txt"
ofilename = "results/out.txt"

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
