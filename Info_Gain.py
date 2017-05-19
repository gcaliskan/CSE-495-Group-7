import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

DataUrl = "C:/HR_Data.xlsx"
data = pd.read_excel(DataUrl)


# Calculates the entropy of the given data set for the target attribute.
def entropy(target_attr):
    val_freq = {}
    data_entropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for record in data:
        if (val_freq.has_key(record[target_attr])):
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0

    # Calculate the entropy of the data for the target attribute
    for freq in val_freq.values():
        data_entropy += (-freq / len(data)) * Math.log(freq / len(data), 2)

    return data_entropy


def entropy(data, target_attr):
    val_freq = {}
    data_entropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for record in data:
        if (record[target_attr] in val_freq):
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0

    # Calculate the entropy of the data for the target attribute
    for freq in val_freq.values():
        data_entropy += (-freq / len(data)) * np.math.log(freq / len(data), 2)

    return data_entropy


# Calculates the information gain (reduction in entropy) that would result by splitting the data on the chosen attribute (attr).
# def gain(data, attr, target_attr):
def gain(attr, target_attr):
    val_freq = {}
    subset_entropy = 0.0

    # Calculate the frequency of each of the values in the target attribute
    for record in data:
        #if (val_freq.has_key(record[attr])):
        if (record[attr] in val_freq):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    # Calculate the sum of the entropy for each subset of records weighted by their probability of occuring in the training set.
    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)

    # Subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute (and return it)
    # return (entropy(data, target_attr) - subset_entropy)
    return (entropy(target_attr) - subset_entropy)


result = entropy(data,0)

print(result)
