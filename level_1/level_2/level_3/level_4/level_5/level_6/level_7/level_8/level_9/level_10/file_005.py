# File at depth 10, file 5
print('Hello from nested file at depth 10, file 5')

class NestedClass10_5:
    def __init__(self):
        self.depth = 10
        self.file_id = 5

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'