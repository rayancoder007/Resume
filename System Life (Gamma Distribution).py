# Code Developed by
# Rayan Chowdhury
# Nimit Singhal
# Saptarshi Roy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

N = int(input("Enter the number of iterations (N): "))
n = int(input("Enter the value of n: "))

t_array = []
t_array_without = []
t_array_renew = []

for i in range(1, N+1):
    X1 = np.random.gamma(shape=5, size=n)
    X2 = np.random.gamma(shape=5, size=n)
    X3 = np.random.gamma(shape=5, size=n)
    
    # with standby
    cold_standby = np.random.gamma(shape=5, size=n)
    first_fail = np.minimum(X1, X2, X3)
    
    if np.array_equal(X1, first_fail):
        t = np.minimum(cold_standby, np.maximum(X2-X1, X3-X1)) + X1
    elif np.array_equal(X2, first_fail):
        second_fail = np.minimum(X1, X3)
        if np.array_equal(second_fail, X1):
            t = np.minimum(cold_standby, X3-X1) + X1
        else:
            t = np.minimum(cold_standby, X1-X3) + X3
    else:
        second_fail = np.minimum(X1, X2)
        if np.array_equal(second_fail, X1):
            t = np.minimum(cold_standby, X2-X1) + X1
        else:
            t = np.minimum(cold_standby, X1-X2) + X2
    
    t_array.append(t)
    
    # without standby
    t2 = np.minimum(X1, np.maximum(X2, X3))
    t_array_without.append(t2)
    
    # renewal
    cold_standby_2 = np.random.gamma(shape=5, size=n)
    
    if np.array_equal(X1, first_fail):
        t = np.minimum(cold_standby, np.maximum(X2-X1, X3-X1)) + X1
    elif np.array_equal(X2, first_fail):
        second_fail = np.minimum(X1, X3)
        if np.array_equal(second_fail, X1):
            t = (np.minimum(cold_standby, np.maximum(cold_standby_2, X3-X1)) + X1) + np.minimum(cold_standby_2, cold_standby)
        else:
            t = np.minimum(X1-X3, np.maximum(cold_standby, cold_standby_2)) + X3
    else:
        second_fail = np.minimum(X1, X2)
        if np.array_equal(second_fail, X1):
            t = (np.minimum(cold_standby, np.maximum(cold_standby_2, X2-X1)) + X1) + np.minimum(cold_standby_2, cold_standby)
        else:
            t = np.minimum(X1-X2, np.maximum(cold_standby, cold_standby_2)) + X2
    
    t_array_renew.append(t)

without_mean = np.mean(t_array_without)
with_mean = np.mean(t_array)
renewal_mean = np.mean(t_array_renew)

without_cost = 300
with_cost = 400
renewal_cost = 500

cost_without_sb = without_cost / without_mean
cost_with_sb = with_cost / with_mean
cost_with_renewal = renewal_cost / renewal_mean

combined_df = pd.DataFrame({
    "lifetime": np.concatenate([np.ravel(t_array), np.ravel(t_array_without), np.ravel(t_array_renew)]),
    "id": np.repeat(["with standby", "without standby", "with renewal"], N*n)
})

combined_df["id"] = combined_df["id"].astype("category")  # Convert 'id' column to categorical

plt.figure(figsize=(10, 6))
sns.ecdfplot(data=combined_df, x="lifetime", hue="id")
plt.title("ECDF of Lifetime")
plt.ylabel("Percent")
plt.show()
