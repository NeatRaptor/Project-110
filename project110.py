import statistics
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")

data = df["claps"].to_list()

population_mean = statistics.mean(data)
print("Mean of population: "+str(population_mean))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    sample_mean = statistics.mean(mean_list)
    print("Sampling mean: " +str(sample_mean))
    show_fig(mean_list)


def show_fig(mean_list):
    dafr = mean_list
    fig = ff.create_distplot([dafr], ["Average number of claps"], show_hist=False)
    fig.show()


setup()
