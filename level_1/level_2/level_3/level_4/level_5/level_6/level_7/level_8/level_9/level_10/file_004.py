# File at depth 10, file 4
print('Hello from nested file at depth 10, file 4')

class NestedClass10_4:
    def __init__(self):
        self.depth = 10
        self.file_id = 4

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'