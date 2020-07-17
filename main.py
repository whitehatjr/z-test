import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
# fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
# fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
# print("mean of popultion:- ",mean)
# print("Standard deviation of popultion:- ",std_deviation)



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



# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
# mean = statistics.mean(mean_list)
# print("mean of sampling distribution:- ",mean)
# print("Standard deviation of sampling distribution:- ", std_deviation)

# #plotting the mean of the sampling
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
# fig.show()
# print("Standard deviation of sampling distribution:- ", std_deviation)


## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)

## plotting the graph with traces
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
# fig.show()


# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
# df = pd.read_csv("data1.csv")
# data = df["Math_score"].tolist()
# mean_of_sample1 = statistics.mean(data)
# print("Mean of sample1:- ",mean_of_sample1)
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.show()



# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
# df = pd.read_csv("data2.csv")
# data = df["Math_score"].tolist()
# mean_of_sample2 = statistics.mean(data)
# print("mean of sample 2:- ",mean_of_sample2)
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.show()


# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
