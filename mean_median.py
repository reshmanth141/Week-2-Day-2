import numpy as np
data = np.array([12, 15, 18, 20, 25], dtype=float)
numpy_mean = np.mean(data)
numpy_median = np.median(data)
numpy_std = np.std(data)  
manual_mean = sum(data) / len(data)
sorted_data = sorted(data)
middle = len(sorted_data) // 2
if len(sorted_data) % 2:
	manual_median = sorted_data[middle]
else:
	manual_median = (sorted_data[middle - 1] + sorted_data[middle]) / 2

manual_std = (
	sum((value - manual_mean) ** 2 for value in data) / len(data)
) ** 0.5

print(f"Data: {data}")
print(f"Mean: NumPy = {numpy_mean:.2f}, Manual = {manual_mean:.2f}")
print(f"Median: NumPy = {numpy_median:.2f}, Manual = {manual_median:.2f}")
print(f"Standard deviation: NumPy = {numpy_std:.2f}, Manual = {manual_std:.2f}")

assert np.isclose(numpy_mean, manual_mean)
assert np.isclose(numpy_median, manual_median)
assert np.isclose(numpy_std, manual_std)
