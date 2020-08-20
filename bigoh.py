# https://github.com/gergelykalman/bigOH - This code will not terminate in your lifetime.
MAX = 1000000
magic = 0x1fffffffffffffff
ret = [i*magic for i in range(MAX)]
set(ret)
print("Your Python is not vulnerable")
