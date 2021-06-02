#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # NUMPY : 
# ## NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely. NumPy stands for Numerical Python.
# 
# # PANDAS :
# ## Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.
# 
# # MATPLOTLIB :
# ## Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits.
# 
# # SEABORN :
# ## Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
# 
# # PLOTLY.EXPRESS :
# ## Plotly Express is a new high-level Python visualization library, is a wrapper for Plotly.py that exposes a simple syntax for complex charts.

# In[3]:


get_ipython().system(' pip install plotly.express')


# In[4]:


import plotly.express as px


# # STEP 2

# In[12]:


get_ipython().system(' pip install xlrd')


# In[16]:


get_ipython().system(' pip install openpyxl')


# In[17]:


df = pd.read_excel(r'C:\Users\Personal\Desktop\TASKS\TASK- II EDA ON AMCAT DATA\data.xlsx')


# In[18]:


df


# Observation :
# There are 3998 data of the people which contains the Gender, Designation, Salary, Location, Percentage of 10th, 12th and B.Tech including with College Tier -Specialization, etc things

# # STEP 3 : DATA ANALYSIS

# ## include = 'all' is provided as an option, the result will include a union of attributes of each type. The includes and excludes parameters, can be used to limit which columns in a DataFrame are analyzed for the output. The parameters are ignored when analyzing a Series & describes a numeric Series.

# In[20]:


df.describe(include='all')


# 
# Obesrvation:
# We are able to get the information of MEAN, MEDIAN, STANDARD DEVIATION, MINIMUM & MAXIMUM VALUES OF ENTIRE DATA

# # GETTING THE TOP 5 & LAST 5 DATA

# In[25]:


X=df.head()
X


# 
# OBSERVATION:
# There are 3 males & 2 females, where one of the male has highest Salary Package who is a SENIOR SOFTWARE ENGINEER.

# In[26]:


Y=df.tail()
Y


# 
# Observation:
# There are 3 females & 2 males, where one of the female has highest Salary Package who is a SENIOR SYSTEMS ENGINEER.

# # DISTPLOT: Seaborn distplot lets you show a histogram with a line on it. We use seaborn in combination with matplotlib, the Python plotting module. It plots a UNIVARIATE distribution of observations. The distplot() function combines the matplotlib hist function with the seaborn kdeplot() and rugplot() functions.
# # KDE PLOT: kernel density estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable. Kernel density estimation is a fundamental data smoothing problem where inferences about the population are made, based on a finite data sample and Show a univariate or bivariate distribution.
# # RUG PLOT: A rug plot is a plot of data for a single quantitative variable, displayed as marks along an axis. It is used to visualise the distribution of the data. As such it is analogous to a histogram with zero-width bins, or a one-dimensional scatter plot. Draws a small vertical lines to show each observation in a distribution.

# In[27]:


sns.distplot(df['Salary'])


# In[28]:


sns.distplot(df['Salary'], kde = False, rug = True)


# In[29]:


sns.distplot(df['Salary'], kde = False, rug = False)


# In[30]:


sns.distplot(df['Salary'], kde = True, rug = False)


# In[31]:


sns.distplot(df['Salary'], kde = True, rug = True)


# In[32]:



sns.distplot(df['collegeGPA'], kde = False, rug = True)


# In[33]:



sns.distplot(df['Logical'], kde = False, rug = True)


# 
# Observation:
# 1. It's a figure-level function with a similar flexibility over the kind of plot to draw.
# 
# 2. It's basically for univariant set of observations and visualizes it through a histogram i.e. only one observation and hence we choose one particular column of the dataset.
# 
# 3. The plot shows a simple distribution when it creats a random values with random.randn().

# In[34]:


sns.catplot(x = "Gender", y = "Salary", hue = "CollegeTier", kind = "point", data = df)


# In[35]:


sns.catplot(x = "Gender", y = "Salary", hue = "Degree", kind = "point", data = df)


# In[36]:


sns.catplot(x="collegeGPA", y="Salary", hue="Gender", markers=["^", "o"], linestyles=["-", "--"], kind="point", data = X)


# In[37]:


sns.catplot(x="collegeGPA", y="Salary", hue="Gender", markers=["^", "o"], linestyles=["-", "--"], kind="point", data = Y)


# In[38]:


sns.catplot(x="collegeGPA", y="Salary", hue="Gender", markers=["^", "o"], linestyles=["-", "--"], kind="point", data=df)


# In[39]:


sns.catplot(x="Degree", y="Salary", hue="Gender", markers=["^", "o"], linestyles=["-", "--"], kind="point", data = df)


# Observation:
# 1. Point plots can be more useful than bar plots for focusing comparisons between different levels of one or more categorical variables.
# 
# 2. They are particularly adept at showing interactions: how the relationship between levels of one categorical variable changes across levels of a second categorical variable. The lines that join each point from the same hue level allow interactions to be judged by differences in slope, which is easier for the eyes than comparing the heights of several groups of points or bars.
# 
# 3. It is important to keep in mind that a point plot shows only the mean (or other estimator) value, but in many cases it may be more informative to show the distribution of values at each level of the categorical variables. In that case, other approaches such as a box or violin plot may be more appropriate.
# 

# # VIOLIN PLOT :
# ## A violin plot gives a combination of boxplot and kernel density estimate, plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared.

# In[40]:


sns.violinplot(x = df.CollegeTier, y = df.collegeGPA)


# In[41]:


sns.violinplot(x = df.Degree, y = df.collegeGPA)


# In[42]:


sns.catplot(x= "Degree", y= "collegeGPA", hue= "Gender", kind= "violin", inner= "stick", split=True, palette="pastel", data= df)


# In[43]:


sns.catplot(x = "Degree", y = "collegeGPA", hue = "Gender", kind = "violin", split = True, data = df)


# In[44]:


sns.catplot(x = "collegeGPA", y = "Degree", hue = "Gender", kind = "violin", bw = .15, cut = 0, data = df)


# In[45]:


sns.catplot(x = "Degree", y = "collegeGPA", hue = "Gender", kind = "violin", data = df)


# In[46]:



sns.catplot(x = "Degree", y = "Salary", kind = "boxen", data = df.sort_values("collegeGPA"))


# In[47]:



sns.catplot(x = "Degree", y = "Salary", hue = "Gender", kind = "box", data = df)


# Observation:
# 1. The white dot represents the median, the thick gray bar in the center represents the interquartile range, the thin gray line represents the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the interquartile range.
# 
# 2. Violin plot are made vertically most of the time, If you have long labels building an horizontal version{Output[22]} like above make the labels more readable.
# 
# 3. If the variable are grouped, we can build a grouped violin as you would do for a boxplot.

# # BOXPLOT : 
# ## A Boxplot is a very basic plot - used to visualize distributions. It's very useful when you want to compare data between two groups. Sometimes a boxplot is named a box-and-whisker plot. Any box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.

# In[48]:


sns.boxplot(data = X, x='Specialization', y='Salary')


# In[49]:



sns.boxplot(data = df, x = 'Specialization', y = 'Salary')


# In[50]:



sns.boxplot(data = df, x = 'Designation', y = 'Salary')


# In[51]:



sns.boxplot(data = df, x = 'GraduationYear', y = 'Salary')


# In[52]:


sns.boxplot(data = df, x = 'CollegeTier', y = 'Salary')


# In[53]:


sns.boxplot(data = df, x = 'CollegeTier', y = 'Degree')


# In[54]:



sns.boxplot(data = X, x = 'collegeGPA', y = 'Designation')


# In[55]:



sns.boxplot(data = df, x = 'Degree', y = 'Salary')


# In[56]:



sns.boxplot(data = X, x = 'Salary', y = 'Designation', hue = 'Specialization')


# In[57]:


sns.boxplot(data = Y, x = 'Specialization', y = 'Salary', hue = 'Designation')


# In[58]:


sns.catplot(x = "English", y = "Logical", kind = "boxen", data = df.sort_values("Gender"))


# In[59]:


plt.boxplot(df['Salary'])
plt.show()


# In[60]:


plt.boxplot(df['collegeGPA'])
plt.show()


# # Observation:
# ## OUTLIERS:
# 1. An outlier is an observation that is numerically distant from the rest of the data. Box plots are useful as they show outliers within a data set. When reviewing a box plot, an outlier is defined as a data point that is located outside the whiskers of the box plot.
# 
# 2. Comparision of the medians, the interquartile ranges and whiskers of box plots.
# 
# 3. Gives the potential outliers and signs of Skewness.
# 
# # SWARM PLOT :
# # This style of plot is sometimes called a “beeswarm”. A swarm plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

# In[61]:


sns.catplot(x = "Gender", y = "Salary", order = ["m", "f"], data = df)


# In[65]:



sns.catplot(x = "English", y = "Quant", hue = "Gender", kind = "swarm", data = df)


# In[66]:



sns.catplot(x = "GraduationYear", y = "collegeGPA", data = df)
sns.swarmplot(data = df, x = 'Specialization', y = 'Salary')


# In[64]:



sns.catplot(x = "Degree", y = "Salary", hue = "Gender", kind = "swarm", data = df)


# In[67]:



sns.swarmplot(data = df, x = 'Domain', y = 'English')


# In[68]:



sns.swarmplot(data = df, x = 'Salary', y = 'Domain')


# In[69]:



sns.swarmplot(data = df, x = 'Salary', y = 'Domain')


# Observation:
# 1. It can give a better representation of the distribution of observations, although it only works well for relatively small datasets.
# 
# 2. Enlarging the plot and Separate points by hue using the argument split = True.
# 
# 3. Place the legend to the right while Adjusting the y-axis limits to end at 0.
# 
# # SCATTER PLOT : 
# ## They can plot two-dimensional graphics that can be enhanced by mapping up to three additional variables while using the semantics of hue, size, and style parameters. Using redundant semantics can be helpful for making graphics more accessible.
# # JOINT PLOT :
# ## It displays a relationship between 2 variables (bivariate) as well as 1D profiles (univariate) in the margins. This plot is a convenience class that wraps JointGrid.

# In[70]:



sns.jointplot(x = 'Salary', y = 'collegeGPA', data = df, kind = 'scatter')


# In[71]:



sns.jointplot(x = 'collegeGPA', y = 'Salary', data = df, kind = 'scatter')


# In[72]:



sns.jointplot(x = 'English', y = 'Logical', data = df, kind = 'scatter')


# In[73]:



sns.jointplot(x = 'English', y = 'collegeGPA', data = df, kind = 'scatter')


# In[74]:



sns.jointplot(x='Logical', y='Quant', data=df, kind = 'scatter')


# In[75]:



plt.scatter(df['Salary'], df['collegeGPA'])
plt.show()


# In[76]:


plt.scatter(df['Salary'], df['Specialization'])
plt.show()


# In[77]:


plt.scatter(df['Gender'], df['Salary'])
plt.show()


# In[78]:


plt.scatter(df['English'], df['Domain'])
plt.show()


# In[79]:


plt.scatter(df['Quant'], df['Logical'])
plt.show()


# In[80]:


plt.scatter(df['Degree'], df['CollegeState'])
plt.show()


# In[81]:


plt.scatter(df['Degree'], df['CollegeTier'])
plt.show()


# In[82]:



plt.scatter(df['collegeGPA'], df['Gender'])
plt.show()


# 
# ## Observation:
# 
# # SCATTER PLOT :
# 1. Pairs of numerical figures are present.
# 
# 2. Dependent variables have multiple values for each figure associated with the independent variable.
# 
# 3. Defining if there is a relationship between two variables and only show correlation.
# 
# 4. Discrete data is best at pass/ fail measurements, Continuous data lets you measure things deeply on an infinite set and is generally used in scatter analysis.
# 
# # JOINT PLOT :
# 1. From the output, you can see that a joint plot has three parts.
# 
# 2. A distribution plot at the top for the column on the x-axis, a distribution plot on the right for the column on the y-axis and a scatter plot in between that shows the mutual distribution of data for both the columns.
# 
# 3. You can see that there is no correlation observed between the x, y variables as given in the input.
# 
# 4. You can change the type of the joint plot by passing a value for the kind parameter.

# # HEXBIN PLOT : 
# ## A Hexbin plot is useful to represent the relationship of 2 numerical variables when you have a lot of data point. Instead of overlapping, the plotting window is split in several hexbins, and the number of points per hexbin is counted. The color denotes this number of points.

# In[83]:



sns.jointplot(x = 'collegeGPA', y = 'Salary', data = df, kind = 'hex', color = 'k')


# In[84]:



sns.jointplot(x = 'English', y = 'Quant', data = df, kind = 'hex', color = 'b')


# In[85]:



sns.jointplot(x = 'CollegeTier', y = 'Domain', data = X, kind = 'hex', color = 'b')


# In[86]:



sns.jointplot(x = 'Quant', y = 'Logical', data = df, kind = 'hex', color = 'b')


# In[87]:



sns.jointplot(x = 'CollegeID', y = 'Salary', data = df, kind = 'hex', color = 'b')


# Observation:
# 1. Instead of overlapping, the plotting window is split in several hexbins, and the number of points per hexbin is counted.
# 
# 2. The color denotes this number of points.
# 
# 3. The size of the hexagons changes - the scale of the color bar guide is redefined accordingly and We can change the size of the bins using the gridsize argument.
# 
# 4. We get a clear picture of density, distributions, and relative ranges, similar to a heat map.
# 
# 5. The shape of the hexagon allows us to limit the effects of edge biases found in square bins, while retaining the ability to form a continuous grid.
# 
# # PAIR PLOT :
# ## Pair Plots are a really simple (one-line-of-code simple!) way to visualize relationships between each variable. It produces a matrix of relationships between each variable in your data for an instant examination of our data. It can also be a great jumping off point for determining types of regression analysis to use.

# In[88]:



sns.pairplot(df)


# In[89]:



sns.pairplot(X)


# In[90]:



sns.pairplot(Y)


# 
# Observation:
# 1. Pairs plots are a powerful tool to quickly explore distributions and relationships in a dataset.
# 
# 2. The diagonal plots are kernel density plots where the other plots are scatter plots.
# 
# # STRIP PLOT :
# ## A strip plot is a graphical data anlysis technique for summarizing a univariate data set. The strip plot consists of: Horizontal axis = the value of the response variable. It is typically used for small data sets (histograms and density plots are typically preferred for larger data sets).

# In[91]:



sns.stripplot(data = df, x = 'Salary', y ='collegeGPA')


# In[92]:



sns.stripplot(data = df, x = 'Specialization', y = 'Logical')


# In[93]:



sns.stripplot(data = df, x = 'CollegeTier', y='Specialization')


# In[94]:



sns.stripplot(data = df, x = 'English', y='Domain')


# In[95]:



sns.stripplot(data = df, x = 'Logical', y='Quant')


# Observation:
# 1. Some things to keep an eye out for when looking at data on a numeric variable: (a) Skewness and Multimodality can be seen, but other visualizations show these more clearly. (b) Gaps and Outliers can be revealed and data outside of the expected range. (c) rounding, e.g. to integer values, or heaping, i.e. a few particular values occur very frequently. (d) impossible or suspicious values.
# 
# 2. Scalability in this form is limited due to over-plotting and can display up to 30,000 data points.
# 
# 3. With a good combination of point size choice, jittering, and alpha blending the strip plot for groups of data can scale to several hundred thousand observations and ten to twenty of groups.
# 
# 4. Storage needed for vector graphics images grows linearly with the number of observations.
# 
# # BAR PLOT :
# ## A bar chart or graph is a chart or graph that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. The bars can be plotted vertically or horizontally. A vertical bar chart is sometimes called a column chart. The size of the bar represents its numeric value & also displays the values of several levels of grouping.

# In[96]:



sns.barplot(x = 'Gender', y = 'Salary', data = df)


# In[120]:



sns.barplot(x = 'collegeGPA', y = 'Degree', data = df)


# In[98]:



sns.barplot(x = 'Salary', y = 'collegeGPA', hue = 'Degree', data = df)


# In[99]:



sns.barplot(x = 'CollegeTier', y = 'collegeGPA', hue = 'Degree', data = df)


# In[100]:



sns.barplot(x = 'English', y = 'Degree', hue = 'Gender', data = df)


# 
# Observation:
# 1. They are created to show data in multiple, highly visual waysTo interpret the length of the bars/columns determines the value as described on the y-axis.
# 
# 2. Bar graphs have an x- and y-axis and can be used to showcase one, two, or many categories of data where Single and dual bar charts are practised using them to represent data to show the total size of groups.
# 
# 3. Shows how the proportions between groups related to each other, in addition to the total of each group.
# 
# 4. The columns can contain multiple labeled variables (or just one), or they can be grouped together (or not) for comparative purposes.
# 
# # COUNT PLOT : 
# ## A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable. The basic API and options are identical to those for barplot() , so you can compare counts across nested variables.

# In[101]:



sns.countplot(x = 'Salary', data = df, palette = 'rainbow')


# In[102]:



sns.countplot(x = 'Salary', data = X, palette = 'rainbow')


# In[103]:



sns.countplot(x = 'CollegeTier', data = df, palette = 'gist_earth')


# In[104]:



sns.countplot(x = 'English', data = df, palette = 'autumn')


# In[105]:



sns.countplot(x= 'Gender', data = df, palette = 'Paired')


# In[106]:



sns.countplot(x = 'JobCity', data = Y, palette ='twilight')


# In[107]:



sns.countplot(x = 'collegeGPA', data = X, palette = 'cubehelix')


# In[108]:



sns.countplot(x = 'Degree', data = df, palette = 'Purples')


# In[109]:



sns.countplot(x = 'Designation', data = Y, palette = 'cubehelix')


# 
# Observation:
# 1. Vectors of data represented as lists, numpy arrays, or pandas Series objects passed directly to the x, y, and/or hue parameters.
# 
# 2. In most cases, it is possible to use numpy or Python objects, but pandas objects are preferable because the associated names will be used to annotate the axes. Additionally, we can use Categorical types for the grouping variables to control the order of plot elements.
# 
# 3. A "long-form" DataFrame, in which case the x, y, and hue variables will determine how the data are plotted.
# 
# 4. A “wide-form” DataFrame, such that each numeric column will be plotted.
# 
# # HISTOGRAM :
# ## A histogram is an accurate graphical representation of the distribution of numerical data. The x-axis of the histogram denotes the number of bins while the y-axis represents the frequency of a particular bin.

# In[110]:


plt.hist(df['Salary'])
plt.show()


# In[111]:


plt.hist(df['Designation'])
plt.show()


# In[112]:


plt.hist(df['Gender'])
plt.show()


# In[113]:


plt.hist(df['Specialization'])
plt.show()


# In[114]:


plt.hist(df['Degree'])
plt.show()


# Observation:
# 1. Creating a histogram provides a visual representation of data distribution.
# 
# 2. Histograms can display a large amount of data and the frequency of the data values where the median and distribution of the data can be determined. In addition, it can show any outliers or gaps in the data.
# 
# 3. To select a "neat" number of bins and "neat" mid-point values for the data. You may over-ride this selection and set your own bin specifications when prompted.

# # PIE CHART :
# ## A Pie Chart is a circular statistical plot that can display only one series of data. The area of the chart is the total percentage of the given data. The area of slices of the pie represents the percentage of the parts of the data. The slices of pie are called wedges.

# In[115]:


px.pie(df, names = 'Degree', values = 'collegeGPA')


# In[116]:



px.pie(df, names = 'GraduationYear', values = 'English')


# In[117]:



px.pie(df, names = 'Specialization', values = 'CollegeTier')


# In[118]:



px.pie(df, names = 'Gender', values = 'GraduationYear')


# 
# Observation:
# 1. When you interpret one pie chart, we get the differences in the size of the slices as per the data taken.
# 
# 2. The size of a slice shows the proportion of observations that are in that group.
# 
# 3. When you compare multiple pie charts, we get the differences in the size of slices for the same categories in all the pie charts.
# 
# # HEATMAP :
# ## A heatmap (aka heat map) depicts values for a main variable of interest across two axis variables as a grid of colored squares. The axis variables are divided into ranges like a bar chart or histogram, and each cell's color indicates the value of the main variable in the corresponding cell range.
# 
# 
# # CORRELATION OF A HEATMAP : 
# ## A correlation heatmap uses colored cells, typically in a monochromatic scale, to show a 2D correlation matrix (table) between two discrete dimensions or event types. The values of the first dimensions appear as rows of the table, while the values of the second dimension are represented by the columns of the table.
# # CORRELATION BETWEEN DIFFERENT COLUMNS

# In[119]:


corr = df.corr(method = 'kendall')
plt.figure(figsize = (15,8))
sns.heatmap(corr, annot = True)
df.columns


# 
# Observation:
# 1. Feature-expression heat maps provide insight into complex associations.
# 
# 2. It utilizes effect ordered data display on two variable sets.
# 
# 3. Its applications are found in complex biological systems.
# 
# 4. Effect size (color) and statistical significance (radius) are depicted in circles.

# In[ ]:




