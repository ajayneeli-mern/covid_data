#!/usr/bin/env python
# coding: utf-8

# ### imports

# In[10]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import os


# ### Read csv

# In[12]:


df = pd.read_csv("Latest Covid-19 India Status.csv")
df.head()


# In[18]:


df.shape
df.columns


# In[19]:


df.info()


# In[21]:


df.describe()


# In[24]:


#df.isnull() -> shws booleen values 
#df.isnull().sum() -> keep add count of null of that row
df.isnull().sum()


# In[30]:


df['State/UTs'].unique()#states

df['State/UTs'].nunique()#count


# In[29]:


states=df["State/UTs"].tolist()


# ### min & max number of deaths

# In[ ]:


df['Deaths'].max()

df['Deaths'].min()

df[df['Deaths']==148419]


# ### state with hightest death & lowest deaths

# In[50]:


df[['State/UTs','Deaths']].sort_values(by="Deaths",ascending=False)[:5]


# In[52]:


df.sort_values(by="Deaths",ascending=False)[:5]['Population']


# In[53]:


df.sort_values(by="Deaths",ascending=False)[:5]


# ### plot states vs no of death

# In[105]:


x=df[['State/UTs','Deaths']].sort_values(by="Deaths",ascending=False)['State/UTs'][:10].values
y=df[['State/UTs','Deaths']].sort_values(by="Deaths",ascending=False)['Deaths'][:10].values

df1=pd.DataFrame({'State/UTs':x,'Deaths':y})
fig=px.bar(df1,
          x='State/UTs',
          y='Deaths',
          color='State/UTs',
          title='states vs No.of deaths')

fig.show()


# In[67]:


df['Active']#.tolist()]
df['Active'].values#.tolist()]


# In[64]:


df[['Active']].values


# ### TOP 10 STATES WITH HIGHEST NUMBER OF ACTIVE CASES

# In[80]:


x=df[['State/UTs','Active']].sort_values(by = 'Active',ascending=False)[:10]['State/UTs'].values

y=df[['State/UTs','Active']].sort_values(by = 'Active',ascending=False)[:10]['Active'].values

df1 = pd.DataFrame({'State/UTs':x,
                  'Active Cases':y })
fig = px.pie(df1, 
             names='State/UTs', 
             values='Active Cases',
             color='State/UTs',
             title='State/UTs Vs No. of Active Cases',
             hole=0.3,
             height = 800,
             width = 800
            )
fig.update_traces(textposition='outside', textinfo='value+label',
            pull=[0,0.1,0.2,0.3,0.4,0.1,0.2,0.1,0.1,0.3] )
fig.show()


# In[83]:


x = df[['State/UTs','Active']].sort_values(by = 'Active',ascending=False)[:10]['State/UTs'].values
y = df[['State/UTs','Active']].sort_values(by = 'Active',ascending=False)[:10]['Active'].values

df1 = pd.DataFrame({'State/UTs':x,
                  'Active Cases':y })

fig = px.scatter(df1, 
             x='State/UTs', 
             y='Active Cases',
             color='State/UTs',
             title='State/UTs Vs No. of Active Cases',
                 size='Active Cases'
            )
fig.show()


# ### Top 10 States with Highest Number of Discharged Patients

# In[89]:


x = df[['State/UTs','Discharged']].sort_values(by = 'Discharged',ascending=False)[:10]['State/UTs'].values
y = df[['State/UTs','Discharged']].sort_values(by = 'Discharged',ascending=False)[:10]['Discharged'].values

df1 = pd.DataFrame({'State/UTs':x,
                  'Discharged':y })
fig = px.pie(df1, 
             names='State/UTs', 
             values='Discharged',
             color='State/UTs',
             title='State/UTs Vs No. of Discharged',
             hole=0.3,
             height = 800,
             width = 800
            )
fig.update_traces(textposition='outside', textinfo='value+label',
            pull=[0,0.1,0.2,0.3,0.4,0.1,0.2,0.1,0.1,0.3] )
fig.show()


# ### **Active Cases is comparatively very less than Total cases or discharged

# In[90]:


x = df['State/UTs'].values
y1 = df['Total Cases'].values
y2 = df['Active'].values


fig= go.Figure()

fig.add_trace(go.Scatter(x=x, y=y1, name= "Total"))
fig.add_trace(go.Scatter(x=x, y=y2, name= "Active"))

fig.show()


# In[92]:


covidI= df
x = covidI['State/UTs'].values
y1 = covidI[['State/UTs','Total Cases']]['Total Cases'].values
y2 = covidI[['State/UTs','Deaths']]['Deaths'].values
y3 = covidI[['State/UTs','Discharged']]['Discharged'].values

fig= go.Figure()

fig.add_trace(go.Bar(x=x, y=y1, name= "Total"))
fig.add_trace(go.Bar(x=x, y=y2, name= "Deaths"))
fig.add_trace(go.Bar(x=x, y=y3, name= "Discharged"))

fig.update_layout(
    height = 900,
    margin=dict(l=0, r=0, t=0, b=0)
    #paper_bgcolor="lightgrey",
)
fig.show()


# In[96]:


fig = px.line(covidI, x=covidI['State/UTs'].values, y=covidI.columns[3:5], height = 800,width=1000)
fig.show()


# In[97]:


px.histogram(covidI['Death Ratio'])


# In[98]:


x= covidI['State/UTs'].values

plt.subplots(figsize = (8,8))

wordcloud = WordCloud (
                    background_color = 'white',
                    width = 712,
                    height = 384,
                    colormap = 'prism'    ).generate(' '.join(x))
plt.imshow(wordcloud) # image show
plt.axis('off') # to off the axis of x and y
plt.savefig('Plotly-World_Cloud.png')
plt.show()


# In[101]:


# Horizontal Bar graph States versus Death Ratio (using plotly)
x = covidI['State/UTs'].values
y = covidI['Death Ratio'].values

df = pd.DataFrame({'State/UTs':x,
                  'Death Ratio':y })

fig = px.bar(df, 
             x='Death Ratio', 
             y='State/UTs',
             color='State/UTs', #color represents State/UTs
             title='State/UTs versus Death Ratio',
             orientation='h',
             height = 1000
            )
fig.show()


# In[ ]:




