# File at depth 7, file 2
print('Hello from nested file at depth 7, file 2')

class NestedClass7_2:
    def __init__(self):
        self.depth = 7
        self.file_id = 2

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'