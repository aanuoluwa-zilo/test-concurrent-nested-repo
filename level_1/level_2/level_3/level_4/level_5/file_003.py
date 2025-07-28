# File at depth 5, file 3
print('Hello from nested file at depth 5, file 3')

class NestedClass5_3:
    def __init__(self):
        self.depth = 5
        self.file_id = 3

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'