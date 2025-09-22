import math

print("Tính chu vi và diện tích hình tròn")
r = float(input("Nhập bán kính r: "))

cv = 2 * math.pi * r
dt = math.pi * r * r

print("Chu vi = 2πr = %.2f" % cv)
print("Diện tích = πr^2 = %.2f" % dt)
