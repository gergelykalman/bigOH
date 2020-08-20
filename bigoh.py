# this hangs Python
set([i*0x1fffffffffffffff for i in range(1000000)])
print("Your Python is not vulnerable")
