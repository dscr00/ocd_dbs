#%%
# imports

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import re
from plotnine import *


#%%

# data processing

df = pd.read_csv('OCD DBS Tables.csv')



#%%

### Things to do
# --> World map chart of origin of publications --> will require extraction from SR team

# used online resource


# %%

# --> Study type bar chart

## using Plotnine

data_study_type = {
    'Study type': ['Double-blind randomised crossover trial', 'Cohort', 'Case-series'],
    'Frequency': [10, 18, 7]
}

df_study_type = pd.DataFrame(data_study_type)


bar_study_type = (
    ggplot(df_study_type, aes(x='Study type', y='Frequency')) +
    geom_bar(stat='identity', position='identity', fill='steelblue') +
    labs(title='', x='Study type', y='Frequency') +
    theme_minimal()
)

print(bar_study_type)



# %%

# --> Neuroimaging used

# using plotnine

data_neuroimaging = {
    'Neuroimaging used': ['MRI', 'CT', 'Tractography', 'Other'],
    'Frequency': [30, 21, 6, 11]
}

df_neuroimaging = pd.DataFrame(data_neuroimaging)

# Create the bar plot using Plotnine
bar_neuroimaging = (
    ggplot(df_neuroimaging, aes(x='Neuroimaging used', y='Frequency')) +
    geom_bar(stat='identity', position='identity', fill='steelblue') +
    labs(title='', x='Neuroimaging used', y='Frequency') +
    theme_minimal()
)

print(bar_neuroimaging)

#%%

# --> Follow-up time period

# have the follow up as points on a box/biolin plot --> show the points and have the study names as the labels?

##Using plotnine

# Drop rows with missing values in the 'mean_follow_up_months' column
df.dropna(subset=['mean_follow_up_months'], inplace=True)


violin_plot = (
    ggplot(df, aes(x='factor(1)', y='mean_follow_up_months')) +
    geom_violin(fill='steelblue', alpha=0.5) +
    geom_jitter(aes(color='factor(1)'), width=0.2, size=2.5) +
    labs(title='', x='mean_follow_up_months', y='') +
    theme_minimal() +
    theme(legend_title=element_blank())
)

print(violin_plot)


# %%

# --> Target of choice

## Using plotnine

# Get the top 11 neuroanatomical targets and their frequencies
top_targets = df['target_location'].value_counts().reset_index()
top_targets

target_plot = (

    ggplot(top_targets)+
    aes(x='index', y="target_location")+
    geom_bar(stat='identity', position='identity', fill='steelblue') +
    theme_minimal()+
    coord_flip()
)

print(target_plot)


#%%

# --> Reponse definition

# Using plotnine -- doesnt work

response_definition = df['full_response_definition'].value_counts().reset_index()

response_plot = (

    ggplot(response_definition)+
    aes(x='index', y="full_response_definition")+
    geom_bar(stat='identity', position='identity', fill='steelblue') +
    theme_minimal()+
    coord_flip()
)

print(response_plot)


#%%

# --> Number of responders vs partial vs non-resp. (Y-BOCS) --> for some reason doesn't work --> had the same bug for previous graphs and cannot remember how I solved it...

df_responders = df[['Study','full_responders','partial_responders']].copy()

df_responders.dropna(inplace=True)

df_responders_melted = df_responders.melt(id_vars='Study',var_name='Response Type')

df_responders_melted_1 = df_responders_melted[df_responders_melted['value']!=0].reset_index()

df_responders_melted_1



bar_plot = (
    ggplot(df_responders_melted_1, aes(x='Study', y='value'))+
    geom_bar(
        aes(fill='Response Type'),
        stat='identity', position='fill'))



print(bar_plot)
