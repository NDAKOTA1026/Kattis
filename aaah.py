from sys import stdin

def aaah() -> str:
    """
    return go or no based on whether he meets the doctor's requirement
    """
    in1 = input()
    in2 = input()
    print( "go" if len(in1) >= len(in2) else "no" )
    

if __name__ == "__main__":
    aaah()
