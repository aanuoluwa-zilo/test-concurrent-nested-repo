# File at depth 7, file 1
print('Hello from nested file at depth 7, file 1')

class NestedClass7_1:
    def __init__(self):
        self.depth = 7
        self.file_id = 1

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'