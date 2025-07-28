# File at depth 7, file 3
print('Hello from nested file at depth 7, file 3')

class NestedClass7_3:
    def __init__(self):
        self.depth = 7
        self.file_id = 3

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'