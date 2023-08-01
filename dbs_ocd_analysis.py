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



#%%

# --> Timeline chart of studies throughout the years ##### FOR SOME REASON THIS DOESN'T WORK LOOK INTO LATER


def extract_year(string):
    pattern = r"\b\d{4}\b"  # Regular expression pattern to match a 4-digit number
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return None

# Apply the extract_year function to the 'text' column and store the result in a new 'year' column
df['year'] = df['Study'].apply(extract_year)
df['year_end'] = df['year'].astype(int) + 1


px.timeline(df,
            x_start=df['year'].astype(int),
            x_end=df['year_end'].astype(int),
            y=df['Study']
            ).show()





# %%

# --> Study type bar chart


bar_study_type = go.Figure()

bar_study_type.add_trace(

    go.Bar(x=['Double-blind randomised crossover trial', 'Cohort', 'Case-series'],
    y=[10,18,7]
))

bar_study_type.update_layout(

    title_text='',
    xaxis_title_text='Study type',
    yaxis_title_text='Frequency',
    
)

bar_study_type.show()


#%%

## using Plotnine

data_study_type = {
    'Study type': ['Double-blind randomised crossover trial', 'Cohort', 'Case-series'],
    'Frequency': [10, 18, 7]
}

df_study_type = pd.DataFrame(data_study_type)

# Create the bar plot using Plotnine
bar_study_type = (
    ggplot(df_study_type, aes(x='Study type', y='Frequency')) +
    geom_bar(stat='identity', position='identity', fill='steelblue') +
    labs(title='', x='Study type', y='Frequency') +
    theme_minimal()
)

print(bar_study_type)



# %%

# --> Neuroimaging used


bar_neuroimaging = go.Figure()

bar_neuroimaging.add_trace(

    go.Bar(
    x=['MRI','CT','Tractography','Other'],
    y=[30,21,6,11]
))

bar_neuroimaging.update_layout(

    title_text='',
    xaxis_title_text='Neuroimaging used',
    yaxis_title_text='Frequency',
    
)

bar_neuroimaging.show()


#%%

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

# have the follow up as points on a box/biolin plot --> show the points and have the study names as the labels

df.dropna(subset=['mean_follow_up_months'], inplace=True)

px.violin(df, ['mean_follow_up_months'], points='all')

#%%

##Using plotnine

# Drop rows with missing values in the 'mean_follow_up_months' column
df.dropna(subset=['mean_follow_up_months'], inplace=True)

# Create the violin plot using Plotnine
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

bar_target = go.Figure()

bar_target.add_trace(
    go.Bar(
        x=list(df['target_location'].value_counts().index[:11]),
        y=list(df['target_location'].value_counts()[:11])
    )
)

bar_target.update_layout(
    title_text='',
    xaxis_title_text='Neuroanatomical target',
    yaxis_title_text='Frequency'
)

bar_target.show()

#%%

## Using plotnine -- doesnt work

# Get the top 11 neuroanatomical targets and their frequencies
top_targets = df['target_location'].value_counts().nlargest(11)

# Create the bar plot using Plotnine
bar_target = (
    ggplot(pd.DataFrame(top_targets.reset_index()), aes(x='factor(index)', y='target_location')) +
    geom_bar(stat='identity', fill='steelblue') +
    labs(title='', x='Neuroanatomical target', y='Frequency') +
    theme_minimal() +
    theme(axis_text_x=element_text(angle=45, hjust=1))
)

print(bar_target)





#%%

# --> Reponse definition

bar_full_response_definition = go.Figure()

bar_full_response_definition.add_trace(
    go.Bar(
        x=list(df['full_response_definition'].value_counts().index[:8]),
        y=list(df['full_response_definition'].value_counts()[:8])
    )
)

bar_full_response_definition.update_layout(
    title_text='',
    xaxis_title_text='Full response definition',
    yaxis_title_text='Frequency'
)

bar_full_response_definition.show()


#%%

# Using plotnine -- doesnt work

# Get the top 8 full response definitions and their frequencies
top_full_responses = df['full_response_definition'].value_counts()

# Create the bar plot using Plotnine
bar_full_response_definition = (
    ggplot(top_full_responses, aes(x='factor(index)', y='full_response_definition')) +
    geom_bar(stat='identity', fill='steelblue') +
    labs(title='', x='Full response definition', y='Frequency') +
    theme_minimal() +
    theme(axis_text_x=element_text(angle=45, hjust=1))
)

print(bar_full_response_definition)






#%%

# --> Number of responders vs partial vs non-resp. (Y-BOCS)










#%%


df['full_response_definition'].value_counts()

# %%
df['target_location'].value_counts()[0]
# %%
df['target_location'].value_counts().index[0]

# %%
