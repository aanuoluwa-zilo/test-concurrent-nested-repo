# File at depth 10, file 3
print('Hello from nested file at depth 10, file 3')

class NestedClass10_3:
    def __init__(self):
        self.depth = 10
        self.file_id = 3

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'