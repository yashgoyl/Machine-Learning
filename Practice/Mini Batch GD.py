import numpy as np
import matplotlib.pyplot as plt

mean = np.array([5.0, 6.0])
cov = np.array([[1.0, 0.95], [0.95, 1.2]])
data = np.random.multivariate_normal(mean, cov, 8000)

plt.scatter(data[:500, 0], data[:500, 1], marker='.')
plt.show()

data = np.hstack((np.ones((data.shape[0], 1)), data))

split_factor = 0.95
split = int(split_factor * data.shape[0])

X_train = data[:split, :-1]
y_train = data[:split, -1].reshape((-1,1))
X_test = data[split:, :-1]
y_test = data[split:, -1].reshape((-1,1))

print("Number of examples in training set = % d"%(X_train.shape[0])) 
print("Number of examples in testing set = % d"%(X_test.shape[0])) 