https://numpy.org/devdocs/reference/generated/numpy.quantile.html

# Median

The median is the middle value of a sorted array, in case the array is even, the median value is the average of the two middle values.
Example:

n = 10 (tellen van 1)

Median = (n5 + n6) / 2

# Average

# Mean


# IQR (Interquartile Range)

IQR:

The Interquartile Range (IQR) is a measure of statistical dispersion, which represents the range within which the middle 50% of the data lies. It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1):

IQR = Q3 - Q1

Q1 (First Quartile): The value below which 25% of the data falls.
Q3 (Third Quartile): The value below which 75% of the data falls.
The IQR is useful because it is not affected by extreme values (outliers) and provides a robust measure of variability in the dataset.

Steps to Calculate IQR:
Arrange the data in ascending order.
Find Q1 (25th percentile) and Q3 (75th percentile).
Subtract Q1 from Q3 to get the IQR.