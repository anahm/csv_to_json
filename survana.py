#!/usr/bin/python
# Basic python script to convert csv format into json object

import sys

if (len(sys.argv) != 3):
    print "python survana.py <filename> <row_num>"
    sys.exit()

filename = sys.argv[1]
row_num = int(sys.argv[2])
col_num = 0

print filename
print row_num

# open csv
input = open(filename, 'rU')
output = open('json_output.txt', 'w');

# find out number of rows and columns
# row_num = int(input.readline().split()[0])

# store the column names (aka json id's)
col_names = []
for temp_col_name in input.readline().split(','):
    col_names.append(temp_col_name)
    col_num += 1

print 'width: ' + str(col_num) + ' height: ' + str(row_num)

# strip off new line character of the last
col_names[col_num - 1] = col_names[col_num - 1][:-1]

for counter in range(row_num):
    output.write('{\n')
    i = 0
    num_items = 0

    # print out validate option since it's there every time?
    output.write('\t"s-validate": {\n')
    output.write('\t\t"required": true,\n\t\t"skip":true\n\t')
    output.write('},\n')

    for temp in input.readline().split(','):
        print temp

        if len(temp) == 0 or temp == 'blargl' or i > col_num:
            i += 1
            print "hello"
            continue

        if temp[-1] == '\n':
            temp = temp[:-1]

        # strip stupid quotation marks
        if (temp[0] == '"'):
            temp = temp[2:-2]

        # dealing with inner code
        if (col_names[i] == 's-items'):
            output.write('\t"s-items": [\n\t\t{\n')
            num_items = int(temp)
        elif (num_items > 0):
            output.write('\t\t\t" ' + temp + ' ": ' + col_names[i])
            num_items -= 1

            if (num_items == 0):
                output.write('\n\t\t}\n\t]')
        else:
            output.write('\t"' + col_names[i] + '": ' + temp)

        if (col_names[i] != 's-items' and i < col_num - 1):
            output.write(',\n')

        i += 1
    output.write('\n}')
    if counter != row_num - 1:
        output.write(',\n')

# all done!
input.close()
output.close()
print 'all done! (:'
