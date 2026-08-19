def counting_sort(A):
    '''
    This part serves for the radix_sort
    '''

    if len(A) <= 1:
        return
    
    u = 1 + max(x.key for x in A)

    D = [[] for _ in range(u)]

    for x in A:
        key = x.key
        D[key].append(x)

    i = 0

    for Chain in D:
        for x in Chain:
            A[i] = x
            i += 1

def radix_sort(A):
    n = len(A)

    if n <= 1:
        return

    u = 1 + max(A)

    c = 0
    power = 1
    while power < u:
        power *= n
        c += 1

    class Obj : pass

    D = []

    for x in A:
        obj = Obj()
        obj.item = x
        obj.digits = []
        high = x

        for _ in range(c):
            high, low = divmod(high, n)
            obj.digits.append(low)

        D.append(obj)

    for digits_index in range(c):
        for obj in D:
            obj.key = obj.digits[digits_index]

        counting_sort(D)

    for i in range(n):
        A[i] = D[i].item
