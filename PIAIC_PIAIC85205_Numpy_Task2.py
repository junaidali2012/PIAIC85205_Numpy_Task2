#!/usr/bin/env python
# coding: utf-8

# # CrunchieMunchies
# 
# You work in marketing for a food company <b>myCorps</b>, which is developing a new kind of tasty, wholesome cereal called <b>CrunchieMunchies</b>. 
# 
# You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you’ve dug up nutritional data on several different competitors.
# 
# Your task is to use <em>NumPy statistical calculations</em> to analyze this data and prove that your <b>CrunchieMunchies</b> is the healthiest choice for consumers.
# 
# 
# 
# 
# 

# # Task STEPS
# 

# 1.First, import numpy.

# In[10]:


import numpy as np # import numpy


# 2.Look over the <b><em>cereal.csv</em></b> file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as <b><em>calorie_stats.</em></b>
# 
# 

# In[11]:


import csv
from numpy import loadtxt 
calorie_stats = loadtxt ('cereal.csv', delimiter=',') # load CSV file cereal.csv
calorie_stats = np.array(calorie_stats)
calorie_stats


# 3.There are <em>60 calories per serving of CrunchieMunchies</em>. How much <b>higher</b> is the <b>average calorie count</b> of your competition?
# 
# Save the answer to the variable <b>average_calories</b> and print the variable to the terminal to see the answer.
# 

# In[12]:


average_calories = calorie_stats.mean() # averag calories count
average_calories


# 4.Does the <b>average calorie count</b> adequately reflect the distribution of the dataset? Let’s sort the data and see.
# 
# <b><em>Sort</em></b> the data and save the result to the variable <b>calorie_stats_sorted</b>. Print the sorted data to the terminal.
# 

# In[13]:


calorie_stats_sorted = np.sort(calorie_stats)# sorting the data and stored into calorie_stats_ sorted variable
calorie_stats_sorted


# 5.Do you see what I’m seeing? Looks like <b><em>the majority of the cereals are higher than the mean</em></b>. Let’s see if the <b>median</b> is a better representative of the dataset.
# 
# Calculate the median of the dataset and save your answer to <b><em >median_calories</em></b>. Print the median so you can see how it compares to the mean.

# In[14]:


median_calories = np.median(calorie_stats) # statement cal the median of the dataset
median_calories


# 6.While the median demonstrates that <b><em><q>at least half of our values are over 100 calories</q></em></b>, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.
# 
# <b>Calculate different percentiles</b> and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable <b>nth_percentile</b>.
# 

# In[15]:


print("this is 15th percentitle")
print(np.percentile(calorie_stats,15)) 
print("this is 9th percentitle")
print(np.percentile(calorie_stats,9))
print("this is 7th percentitle")
print(np.percentile(calorie_stats,7))
print("this is 5th percentitle")
print(np.percentile(calorie_stats,5))
print("this is 4th percentitle")
print(np.percentile(calorie_stats,4)) # lowest percentile greater than 60calories


# 7.While the percentile shows us that<b><em><q>the majority of the competition has a much higher calorie count</q></em></b>, it’s an awkward concept to use in marketing materials.
# 
# Instead, let’s calculate the percentage of cereals that <b><em><q>have more than 60 calories per serving</q></em></b>. Save your answer to the variable <b><em>more_calories</em></b> and print it to the terminal

# In[16]:


more_than_60 = calorie_stats[calorie_stats>60] # calcule more than 60 calories
print(more_than_60)
more_calories = np.average(more_than_60) # calculate percentage of cereals
print("calculate percentage of cereals and save into variable more_calories")
more_calories


# 8.Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, <b><em>how much variation exists in the dataset? </b></em></q>Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
# 
# Calculate the amount of variation by finding the <b><em>standard deviation</em</b> Save your answer to <b><em>calorie_std</em></b> and print to the terminal. How can we incorporate this value into our analysis?

# In[17]:


print("calcule standard deviation and save into calorie_std")
calorie_std = np.std(calorie_stats) # calcule standard deviation and save into calorie_std
calorie_std


# 9.Write a short paragraph that sums up your findings and how you think this data could be used to 
# <b>myCorp’s</b> advantage when marketing CrunchieMunchies.
# 

# # My findings regarding given dataset

# - In **Step 1** **import** numpy libarary 

# - In **Step 2** Given dataset name is **calories** and load CSV file and save into **calories_stats** variables

# - In **Step 3** i calculate **average calorie count** of your competition and save my answer into **average_calories** variable

# - In **Step 4** i **sorted** the data and check that the **average calorie count** adequately reflect the distribution of the dataset and save into **calorie_stats_sorted**

# - In **Step 5** i calculate **median** which is a better representative of the dataset and save answer into **median_calories** variable

# - In **Step 6** i find out various **percentiles** of the data and extract the **lowest percentiles** where calories is greater than 60 and save answer into median_calories variable **more_calories**

# - In **Step 7** i calculate the amount of variation by finding the **standard deviation** and save the answer into **calorie_std** variable

# ### Advantage of this analyzed data
# 
# #### I think this data would be very helpful for **myCorp's** when they compete with other player in the marketplace. further this data is also helpful while doing marketing of **CrunchieMunichies** as we applied different basic statistcs funcitons through which we come to know that our cereal is very healthiest in the market and we design our strategy to boost up the sales.

# In[ ]:




