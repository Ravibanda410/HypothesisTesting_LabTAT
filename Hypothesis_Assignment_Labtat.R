# Hypothesis Testing

# Load the Dataset
library(readxl)

######## LabTAT.xlsx data ##########
LabTAT <- read_excel(file.choose())
View(LabTAT)
attach(LabTAT)

#############Normality test###############    

#Ho= Data is normally distributed (no action take)
#Ha=Data is not normally distributed (action take)

shapiro.test(`Laboratory 1`)
# p-value = 0.5508 >0.05 so p high null fly => It follows normal distribution

shapiro.test(`Laboratory 2`)
# p-value = 0.8637 >0.05 so p high null fly => It follows normal distribution

shapiro.test(`Laboratory 3`)
# p-value = 0.4205 >0.05 so p high null fly => It follows normal distribution

shapiro.test(`Laboratory 4`)
# p-value = 0.6619 >0.05 so p high null fly => It follows normal distribution


#############Variance test###############
#Ho= Variance of TAT of all Labs are equal
#H1=atleast 1 Lab variance of TAT are not equal

var.test(`Laboratory 1`,`Laboratory 2`)
#H0=Variance of TAT of Lab 1 is equal to variance of TAT of Lab 2
#H1=Variance of TAT of Lab 1 is not equal to variance of TAT of Lab 2
# p-value = 0.1675 > 0.05 so p high null fly accept null hypothesis.

var.test(`Laboratory 2`,`Laboratory 3`)
# p-value = 0.2742 > 0.05 so p high null fly accept null hypothesis.

var.test(`Laboratory 3`,`Laboratory 4`)
# p-value = 0.3168 > 0.05 so p high null fly accept null hypothesis.

var.test(`Laboratory 4`,`Laboratory 1`)
# p-value = 0.1408 > 0.05 so p high null fly accept null hypothesis.

######## 1-way ANOVA test#############



?aov


#Ho= Average TAT for all the samples is same
#Ha= Averages TAT for atleast one sample is not same

Anova_results12345 <- aov(`Laboratory 1`~`Laboratory 2`+`Laboratory 3`+`Laboratory 4`,data = LabTAT)
summary(Anova_results12345)
#Laboratory2  p-value = 0.166 > 0.05 so p high null fly accept null hypothesis.
#Laboratory3  p-value = 0.277 > 0.05 so p high null fly accept null hypothesis.
#Laboratory4  p-value = 0.215 > 0.05 so p high null fly accept null hypothesis.




#there is no significant difference in the average TAT for all the laboratories.