# File at depth 3, file 4
print('Hello from nested file at depth 3, file 4')

class NestedClass3_4:
    def __init__(self):
        self.depth = 3
        self.file_id = 4

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'