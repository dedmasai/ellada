def xyz(x, y, z):
    if x<y<z:
        return y
    else:
         if x>y:
             return xyz(y, x, z)
         if y>z:
             return xyz(x, z, y)

x, y, z=map(int, input().split())
print(xyz(x, y, z))