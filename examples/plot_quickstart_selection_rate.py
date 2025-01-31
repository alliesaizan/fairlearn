# Copyright (c) Microsoft Corporation and Fairlearn contributors.
# Licensed under the MIT License.

"""
=================================
Selection rates in census dataset
=================================
"""
from fairlearn.datasets import fetch_diabetes_hospital
import matplotlib.pyplot as plt


# %%
fig, ax = plt.subplots()

data = fetch_diabetes_hospital(as_frame=True)
X = data.data
X.drop(columns=["readmitted", "readmit_binary"], inplace=True)
y_true = data.target
race = X['race']

df = race.value_counts().reset_index()

ax.bar(df["race"], df["count"])
ax.set_title('Counts by race')
ax.tick_params(axis='x', labelrotation=45)

plt.show()
