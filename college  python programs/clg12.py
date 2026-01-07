
import matplotlib.pyplot as plt
lsx = [1,2]
lsy = [4,5]
plt.bar(lsx,lsy)
for i in range(len(lsx)):
    plt.annotate(xy=[lsx(i),lsy(i)], text = lsy(i))
