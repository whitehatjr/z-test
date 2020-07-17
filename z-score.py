import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#Change the School data here
df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()


##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


# Function to get the mean of 100 data sets
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)



## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)




# # finding the mean of THE STUDENTS WHO GAVE EXTRA TIME TO MATH LAB and plotting on graph
df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()




# #finding the mean of the STUDENTS WHO USED MATH PRACTISE APP and plotting it on the plot.
df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


# finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plotting it on the plot.
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


#finding the z score using the formula
z_score = (mean - mean_of_sample2)/std_deviation
print("The z score is = ",z_score)