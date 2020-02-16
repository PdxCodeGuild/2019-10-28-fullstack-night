class ListNode:
    def __init__(self):
        self.val = None
        self.next = None

    def append(self, in_val):
        if self.val is None:
            self.val = in_val
        else:
            if self.next is None:
                self.next = ListNode()
            self.next.append(in_val)

    def __repr__(self):
        if self.next is None:
            return str(self.val) + ', '
        return str(self.val) + ', ' + str(self.next)

    def __len__(self):
        if self.next is None:
            return 1
        return 1 + len(self.next)

    def __getitem__(self, in_num):
        if in_num == 0:
            return self.val
        return self.next[in_num-1]

class RootNode:
    def __init__(self):
        self.base = None

    def append(self, in_val):
        if self.base is None:
            self.base = ListNode()
        self.base.append(in_val)

    def __repr__(self):
        if self.base is None:
            return '[]'
        return f'[{self.base}]'

    def __len__(self):
        if self.base is None:
            return 0
        return len(self.base)

    def __getitem__(self, in_num):
        if self.base is None:
            raise IndexError
        return self.base[in_num]