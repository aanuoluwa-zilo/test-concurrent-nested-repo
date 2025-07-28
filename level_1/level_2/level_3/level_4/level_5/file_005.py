# File at depth 5, file 5
print('Hello from nested file at depth 5, file 5')

class NestedClass5_5:
    def __init__(self):
        self.depth = 5
        self.file_id = 5

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'