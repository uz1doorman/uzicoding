# Binary Node Implementation with AVL Balancing
def height(A):
    if A: return A.height
    else: return -1

class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A):
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):
        return height(A.right) - height(A.left)

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left: return A.left.subtree_first()
        else: return A

    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else: return A

    def successor(A):
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            A.parent.maintain()
        return A

    def subtree_rotate_right(D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        D.item, B.item = B.item, D.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def rebalance(A):
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    def maintain(A):
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()
