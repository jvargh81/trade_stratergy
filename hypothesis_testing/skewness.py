import statistics
class skewness :
    def __init__(self):
        pass

    def skew_ness(self,data):
        total_number_of_instances = len(data)
        mean = statistics.mean(data)
        xmean3 = [ (data[i] - mean)**3  for i in range(total_number_of_instances)]
        xmean2 = [ (data[i] - mean)**2  for i in range(total_number_of_instances)]
        sumxmean3 = sum(xmean3)
        sumxmean2 = sum(xmean2)

        skew = (((sumxmean3))/total_number_of_instances)/((((sumxmean2))/(total_number_of_instances-1))**(1/3))
        
        if (skew>0):
            return "Right Skewed"
        elif (skew==0):
            return "No Skewed"
        elif (skew<0):
            return "Left Skewed"
        else :
            return "Data Error."






























