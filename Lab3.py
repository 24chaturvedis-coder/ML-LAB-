import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("enjoy - enjoy.csv")

df.head()
df.info()
df.isnull().sum()
df.describe()

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

def find_s(X, y):
    hypothesis = None
    print("Initial Hypothesis:", hypothesis)

    for i in range(len(X)):
        if str(y[i]).strip().lower() == "yes":
            if hypothesis is None:
                hypothesis = X[i].copy()
            else:
                for j in range(len(hypothesis)):
                    if hypothesis[j] != X[i][j]:
                        hypothesis[j] = "?"

            print(f"\nAfter Training Example {i+1}")
            print(hypothesis)

    return hypothesis


final_hypothesis = find_s(X, y)

print("\nFinal Hypothesis:")
print(final_hypothesis)

import copy

def candidate_elimination(concept, target):
    specific = concept[0].copy()
    general = [["?" for i in range(len(specific))]]

    print("\nInitial S:", specific)
    print("Initial G:", general)

    for i, h in enumerate(concept):
        if target[i] == "Yes":
            for x in range(len(specific)):
                if h[x] != specific[x]:
                    specific[x] = "?"
        else:
            for x in range(len(specific)):
                if h[x] != specific[x]:
                    general.append(
                        ["?" if j != x else specific[x]
                         for j in range(len(specific))]
                    )

        print("\nExample", i + 1)
        print("S =", specific)
        print("G =", general)

    return specific, general


S, G = candidate_elimination(X, y)

print("\nFinal Specific Boundary")
print(S)

print("\nFinal General Boundary")
print(G)
