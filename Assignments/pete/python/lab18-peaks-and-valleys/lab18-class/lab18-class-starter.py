# peaks and valleys with classes
class Column:
    '''Take in an index, and a height
    has __len__
    has attributes left_column, right_column, that start as null
    has attributes peak and valley, which start as null
    has methods set_peak and set_valley, which change peak and valley
    attributes to true or false after checking if they are peaks or valleys
    or neither
    '''
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
column_list = []
for i, datum in enumerate(data):
    column_list.append(Column(i, datum))
# print(column_list)
for i, column in enumerate(column_list):
    if i >= 1:
        column.left_column = column_list[i-1]
    if i < len(column_list)-1:
        column.right_column = column_list[i+1]
for column in column_list:
    column.set_peak()
    column.set_valley()
peak_list = [x for x in column_list if x.peak]
print(peak_list)
valley_list = [x for x in column_list if x.valley]
print(valley_list)
print([len(column) * 'x' for column in column_list])