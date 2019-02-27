import skewness
import variance

skew = skewness.skewness()
var = variance.variance()
data1 = [1,1,1,1,1,1,2,3,4,5,6,7,8]
data2 = [1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8]
data3 = [1,2,3,4,5,6,7,8,9]
print("data1 : " + skew.skew_ness(data1))
print("data2 : " + skew.skew_ness(data2))
print("data3 : " + skew.skew_ness(data3))
print("Variance for data1 : " + str(var.population(data1)))
print("standard deviation for data1 : " + str(var.standard_deviation_population(data1)))
print("Covariance for data1 : " + str(var.covariancePopulation(data1)))

size = [650,785,1200,720,975]
price = [772000,998000,1200000,800000,895000]

print("Covariance for data1 and data2 : " + str(var.covariance_2variable_sample(size,price)))
print("Correltion coeffient for data1 and data2 : " + str(var.correlation_coefficient_sample(size,price)))



























