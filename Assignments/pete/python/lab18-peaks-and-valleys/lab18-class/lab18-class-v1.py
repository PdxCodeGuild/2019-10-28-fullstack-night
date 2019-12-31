# peaks and valleys with classes
class Column:
    def __init__(self, i, datum):
        self.i = i
        self.datum = datum
        self.left_column = None
        self.right_column = None
        self.peak = None
        self.valley = None

    def __len__(self):
        return self.datum
    
    def __repr__(self):
        return f"Column(i={self.i}, datum={self.datum})"
    
    def __bool__(self):
        return True

    def set_peak(self):
        if self.left_column and self.right_column:
            if len(self.left_column) < self.datum and len(self.right_column) < self.datum:
                self.peak = True
            else:
                self.peak = False
    
    def set_valley(self):
        if self.left_column and self.right_column:
            print(self.i)
            if len(self.left_column) > self.datum and len(self.right_column) > self.datum:
                self.valley = True
            else:
                self.valley = False


data = [1, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
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
[print(len(column) * 'x') for column in column_list]
print(bool(column_list[0]))