
def ab(m):
    def b():
        print("this is me")
        m()
    return b

@ab
def c():
    print("this is we both")
c()