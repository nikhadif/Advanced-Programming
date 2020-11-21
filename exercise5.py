import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]



plt.bar(x, y, label="First Line")
plt.bar(x2,y2, label="Second Line")
plt.xlabel("Plot Number")
plt.ylabel("sample Value")
plt.title(" Sample Data\n 0 - 100")
plt.legend()
plt.show()
