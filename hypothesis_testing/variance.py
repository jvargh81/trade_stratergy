import statistics as st

class variance :

    def __init__(self):
        pass


    def population(self,data):

        PopLen = len(data)
        mean = st.mean(data)
        diffMean = [(data[i] - mean)**2 for i in range(PopLen)]
        sumMean = sum(diffMean)
        variance = sumMean/PopLen
        return(variance)

    def sample(self,data):

        SampleLen = len(data)
        samplemean = st.mean(data)
        diffMean = [(data[i] - samplemean)**2 for i in range(SampleLen)]
        sumMean = sum(diffMean)
        variance = sumMean/(SampleLen - 1)
        return(variance)

    def standard_deviation_population(self,data):
        standard_deviaton = self.population(data)**(1/2) 
        print(self.population(data))
        return standard_deviaton
    
    def standard_deviation_sample(self,data):
        standard_deviaton = self.sample(data)**(1/2)
        return standard_deviaton

    def covarianceSample(self,data):
        sd = self.standard_deviation_sample(data)
        mean = st.mean(data)
        covariance = sd/mean

        return covariance

    def covariancePopulation(self,data):
        sd = self.standard_deviation_population(data)
        mean = st.mean(data)
        covariance = sd/mean

        return covariance

    def covariance_2variable_sample(self,data1,data2) :
        data1_mean = st.mean(data1)
        data2_mean = st.mean(data2)
        # expect same data length.
        value_len = len(data1)
        diff_mean = [(data1[i] - data1_mean) * (data2[i] - data2_mean) for i in range(value_len)]
        sum_diff_mean = sum(diff_mean)
        covariance = sum_diff_mean/(value_len - 1)

        return covariance

    def covariance_2variable_population(self,data1,data2) :
        data1_mean = st.mean(data1)
        data2_mean = st.mean(data2)
        # expect same data length.
        value_len = len(data1)
        diff_mean = [(data1[i] - data1_mean) * (data2[i] - data2_mean) for i in range(value_len)]
        sum_diff_mean = sum(diff_mean)
        covariance = sum_diff_mean/(value_len - 1)

        return covariance

    def correlation_coefficient_sample(self,data1,data2):
        cov = self.covariance_2variable_sample(data1,data2)
        sd1 = self.standard_deviation_sample(data1)
        sd2 = self.standard_deviation_sample(data2)
        
        cor_coef = cov/(sd1 * sd2)

        return cor_coef

    def correlation_coefficient_population(self,data1,data2):
        cov = self.covariance_2variable_population(data1,data2)
        sd1 = self.standard_deviation_population(data1)
        sd2 = self.standard_deviation_population(data2)
        
        cor_coef = cov/(sd1 * sd2)

        return cor_coef

















