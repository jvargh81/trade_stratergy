## Null hypothesis denoted by H0.
## one too be tested.
## accept - if sample mean is close to the true mean.
## reject - if sample mean is far from the true mean.
## Always aiming to reject the null hypothesis.
##
##Example :
##H0 = mu0 = $130000

## Alternative hypothesis denoted by H1.
## Alternative hypothesis is fact checking null hypothesis.

## Significance level : denoted by alpha
## it is the probablity of rejecting the null hypothesis, if it is true.
## Typical Value for alpha are 0.01,0.05 and  0.1. Value selected based on the certanity.
## pick low significance level if you need high precision.

## example : dean proposes mean grade is 70%
	Null hypothesis H0: it is 70%
	Alternative hypothesis H1: it is not 70%

### Note : Assumption is that the data is normaly distributed.
### Tested using Z_test
## Formula : z_test = (samle mean - population mean)/standard error
## standard error = s/squaredroot(n) s : standard deviation n :  sample size.
## How big should the z be to reject the null hypothesis.
## two case scenario:  
##	1. Two tailed test: 
##		- if its in the middle then we have to accept null hypothesis.
##		- if it falls in the shaded region then we reject it.
## 		for example : if alpha = 0.05 then the alpha/2 is the rejection region.
## 			 How does hypothesis testing work?
##  				- calculate a statistic eg : sample mean.
##  				- scale it eg : z_test
##  				- check if z is in the rejection region. 
## 	2. One tailed test : 
##         	- In this case there is only one side of alternative hypothesis. example: null pass if >= $250000
## 		- if the test statistics is bigger than the cut off 3 score, we would
## 		   reject the null, otherwise we wouldn't.
##
## Types of error 
## 1. Type I error : 
## 	- Reject a true null hypothesis.
##      - False positive.
##	- probability of making this error is alpha.
## 2. Type II error : 
##	- Accept a false null hypothesis.
##	- False negative.
##	- denoted by Beta and depends on sample size and variance.
## 	- probablity of making this error is 1 - B
## Table : 
##			H0 is true		H0 is False
##Accept		correct			False Negative	
##						(Type II error)	
##Reject 		False Positive		correct
##			(Type I error)
##
## P-Value
## p-value is the smallest level of significance at which we can still reject the null hypothesis, given the observed sample statistics.
## p-value = 1 - number from the table. (one sided test)
## p-value = (1 - number from the table) * 2
## Rule : 
##	- Reject the null hypothesis if p-value < alpha.
## P-value works with all distribution. 





