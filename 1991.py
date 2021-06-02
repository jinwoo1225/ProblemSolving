class Node:
    """
    Overly built isn't?
    should use dictionary to solve this problem
    """

    def __init__(self, data: str, left=None, right=None):
        self.data: str = data
        self.left: Node = left
        self.right: Node = right

    def search(self, query):
        if self.data == query:
            return self

        if self.left is not None:
            left_query = self.left.search(query)
            if left_query is not None:
                return left_query

        if self.right is not None:
            right_query = self.right.search(query)
            if right_query is not None:
                return right_query

        return None

    def preorder(self) -> str:
        ret = self.data
        if self.left is not None:
            ret += self.left.preorder()
        if self.right is not None:
            ret += self.right.preorder()
        return ret

    def inorder(self):
        ret = ""
        if self.left is not None:
            ret += self.left.inorder()
        ret += self.data
        if self.right is not None:
            ret += self.right.inorder()
        return ret

    def postorder(self):
        ret = ""
        if self.left is not None:
            ret += self.left.postorder()
        if self.right is not None:
            ret += self.right.postorder()
        ret += self.data
        return ret


N = int(input())
root = Node('A')
temp = []

for _ in range(N):
    head, left, right = input().split()

    if head == 'A':
        root.left = Node(left) if not left == '.' else None
        root.right = Node(right) if not right == '.' else None
    else:
        target = root.search(head)
        if target is None:
            left_node = Node(left) if not left == '.' else None
            right_node = Node(right) if not right == '.' else None
            temp.append(Node(head, left_node, right_node))
        else:
            target.left = Node(left) if not left == '.' else None
            target.right = Node(right) if not right == '.' else None

while temp:
    for n in temp:
        target = root.search(n.data)
        if target is None:
            continue
        target.left = n.left
        target.right = n.right
        temp.remove(n)

print(root.preorder())
print(root.inorder())
print(root.postorder())
