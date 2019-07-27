#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing matplolib.pyplot
import matplotlib.pyplot as plt


# In[2]:


plt.plot([1,2,3,4])
plt.xlabel("some values")
plt.ylabel("some numbers")
plt.title("MyPlot")
plt.show()


# *You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are [0,1,2,3].*

# In[3]:


#plt.plot([x_values],[y_values])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("x")
plt.ylabel("y")
plt.title("MyPlot")
plt.show()


# *with X and y argument we can format our style with third argument that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue.*

# In[4]:


#formatting with style
plt.plot([1,2,3,4],[1,4,9,16],"x-b")
plt.xlabel("x")
plt.ylabel("y")
plt.title("MyPlot")
plt.show()


# ## A format string consists of a part for color, marker and line:
# 
# fmt = '[marker][line][color]'
# 
# **Markers**
# 
# 
# | Character | description   |
# |------|------|
# |'.'	|point marker|
# |','	|pixel marker|
# |'o'	|circle marker|
# |'v'	|triangle_down marker|
# |'^'	|triangle_up marker|
# |'<'	|triangle_left marker|
# |'>'	|triangle_right marker|
# |'1'	|tri_down marker|
# |'2'	|tri_up marker|
# |'3'	|tri_left marker|
# |'4'	|tri_right marker|
# |'s'	|square marker|
# |'p'	|pentagon marker|
# |'*'	|star marker|
# |'h'	|hexagon1 marker|
# |'H'	|hexagon2 marker|
# |'+'	|plus marker|
# |'x'	|x marker|
# |'D'	|diamond marker|
# |'d'	|thin_diamond marker|
# |'|'	|vline marker|
# |'_'	|hline marker|
# 
# **Line Styles**
# 
# | Character | description   |
# |------|------|
# |'-'	|solid line style|
# |'--'	|dashed line style|
# |'-.'	|dash-dot line style|
# |':'	|dotted line style|
# 
# **colors**
# 
# | Character | description   |
# |------|------|
# |'b'	|blue|
# |'g'	|green|
# |'r'	|red|
# |'c'	|cyan|
# |'m'	|magenta|
# |'y'	|yellow|
# |'k'	|black|
# |'w'	|white|

# In[6]:


#using grid
plt.plot([1,2,3,4],[1,4,9,16],"D-b")
plt.xlabel("x")
plt.ylabel("y")
plt.title("MyPlot")
plt.grid()
plt.show()


# In[10]:



import numpy as np
t = np.arange(0.,5.,0.2) #np.arange(starting_index,end_index,step_size)
print(t)
plt.plot(t,t**2,'b--',label='^2')
plt.plot(t,t**2.2,'rs',label='^2.2')
plt.plot(t,t**2.5,'g^',label='^2.5')
plt.legend()
plt.show()


# *There are some instances where you have data in a format that lets you access particular variables with strings. For example, with numpy.recarray or pandas.DataFrame.*
# 
# *Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.*

# In[12]:


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# # plotting with categorical values
# 
# *It is also possible to create a plot using categorical variables. Matplotlib allows you to pass categorical variables directly to many plotting functions. For example:*

# In[31]:


#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html
names = ['x', 'y']
values = [1, 10]
plt.figure(figsize=(10,5)) #Create a new figure.
plt.subplot(132) #This utility wrapper makes it convenient to create common layouts of subplots, including the enclosing figure object, in a single call.
plt.bar(names, values) #Make a bar plot.
plt.subplot(133) #A scatter plot of y vs x with varying marker size and/or color.
plt.scatter(names, values)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


# # Controlling line properties
# 
# *Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see matplotlib.lines.Line2D. There are several ways to set line properties*
# 
# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D

# In[15]:


x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,linewidth=5.0)
plt.show()


# In[18]:


lines = plt.plot(x, y)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
plt.show()


# In[21]:


x = [1,2,3,4]
y = [1,4,9,16]
z = [1,2,3,4]
w = [2,4,6,8]
lines = plt.plot(x,y,z,w)
plt.setp(lines[0],color='r',linewidth=2.0)
plt.setp(lines[1],color='g',linewidth=2.0)
plt.show()


# # Working with multiple figures and axes
# 
# *MATLAB, and pyplot, have the concept of the current figure and the current axes. All plotting commands apply to the current axes. The function gca() returns the current axes (a matplotlib.axes.Axes instance), and gcf() returns the current figure (matplotlib.figure.Figure instance). Normally, you don't have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.*
# 
# 

# In[39]:


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'b-')

plt.subplot(212) #numrows, numcols, plot_number where plot_number ranges from 1 to numrows*numcols
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


# # Working with text
# 
# *The text() command can be used to add text in an arbitrary location, and the xlabel(), ylabel() and title() are used to add text in the indicated locations (see Text in Matplotlib Plots for a more detailed example)*
# 
# https://matplotlib.org/3.1.0/tutorials/text/text_intro.html

# In[46]:


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# In[ ]:




