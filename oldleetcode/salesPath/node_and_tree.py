class Node:
    def __init__(self, value : int, children : list = []):
        self.value = value
        self.children = children

    def __repr__(self):
        return f'[Node (value = {self.value})]'

class Tree:

    def __init__(self, headVal : int = None):
        self.head = Node(headVal)

    def add_child(self, node)

        



def main():
    x = Node(5)
    print(x)
    t = Tree()
    t.add_child(5)
    t.add_child(6)


if __name__ == '__main__':
    main()

