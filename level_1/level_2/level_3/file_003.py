# File at depth 3, file 3
print('Hello from nested file at depth 3, file 3')

class NestedClass3_3:
    def __init__(self):
        self.depth = 3
        self.file_id = 3

    def get_info(self):
        return f'Depth: {self.depth}, File: {self.file_id}'