class A(object):
    def __init__(self):
        print "a"

class B(A):
    def __init__(self):
        print "b"

class C(B):
    def __init__(self):
        print "c"

if __name__ == "__main__":
    o = B()
    print isinstance(o, A)
    print isinstance(o, B)
    print isinstance(o, C)
