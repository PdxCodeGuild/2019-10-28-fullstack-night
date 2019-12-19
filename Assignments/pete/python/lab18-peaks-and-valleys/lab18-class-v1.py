data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Complete Peaks and Valleys using the Column class.
class Column:
    def __init__(self, height, index):
        self.height = height
        self.index = index
        self.p = None # Boolean, True if the column is a peak
        self.v = None # Boolean, True if the column is a valley
        self.left = None # Points at the column to the left, if it exists
        self.right = None # Points at the column to the right, if it exists
    def __len__(self):
        return self.height
    def __repr__(self):
        return str(self.index)
    def __bool__(self):
        return True
for i, datum in enumerate(data):
    column_class_test = Column(datum, i)
    print(f"__len__{column_class_test.__len__()}  __repr__{column_class_test.__repr__()}")
    print(f"")