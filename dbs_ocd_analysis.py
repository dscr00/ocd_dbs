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



#%%

## Year of publication

def extract_year(string):
    pattern = r"\b\d{4}\b"  # Regular expression pattern to match a 4-digit number
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return None

# Apply the extract_year function to the 'text' column and store the result in a new 'year' column
df['Year'] = df['Study'].apply(extract_year)

year_df=df['Year'].value_counts().reset_index()
year_df

#%%
data = {
    'Year': [2021, 2019,2022,2020,2016,2010,2018,2014,2005,2006,2015,2017,2012,2011],
    'count': [8,5,4,3,3,2,2,2,1,1,1,1,1,1,]
}


year_df = pd.DataFrame(data)

# Create the line plot
year_line_plot = (
    ggplot(year_df, aes(x='Year', y='count')) +
    geom_line() +
    geom_point()+
    labs(title='', x='Year of Publication', y='Number of Studies') +
    theme_classic()
)

# Show the plot
print(year_line_plot)


# %%

# --> Study type bar chart

## using Plotnine

data_study_type = {
    'Study type': ['Double-blind randomised crossover trial', 'Cohort', 'Case-series'],
    'Frequency': [10, 18, 7]
}

df_study_type = pd.DataFrame(data_study_type)


bar_study_type = (
    ggplot(df_study_type, aes(x='Study type', y='Frequency', fill='Study type')) +
    geom_bar(stat='identity', position='identity',show_legend=False) +
    scale_fill_manual(values=['black','gray','silver'])+
    labs(title='', x='Study type', y='Frequency')+
    theme_classic()

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
    ggplot(df_neuroimaging, aes(x='Neuroimaging used', y='Frequency', fill='Neuroimaging used')) +
    geom_bar(stat='identity', position='identity', show_legend=False) +
    labs(title='', x='Neuroimaging used', y='Frequency') +
    scale_fill_manual(values=['black','gray','silver','lightgrey'])+
    theme_classic()
    )

print(bar_neuroimaging)

#%%

# --> Follow-up time period

# have the follow up as points on a box/biolin plot --> show the points and have the study names as the labels?

##Using plotnine

# Drop rows with missing values in the 'mean_follow_up_months' column
df.dropna(subset=['mean_follow_up_months'], inplace=True)


violin_plot = (
    ggplot(df, aes(x=1, y='mean_follow_up_months')) +
    geom_violin(fill='black', alpha=0.5) +
    labs(title='', x='Mean follow up (months)', y='') +
    theme_classic() +
    theme(legend_title=element_blank())+
    geom_jitter(width=0.1, alpha=0.7)+
    theme(axis_text_x=element_blank())
    )

print(violin_plot)


# %%

# --> Target of choice

## Using plotnine

# Get the top 11 neuroanatomical targets and their frequencies
top_targets = df['target_location'].value_counts().reset_index()

target_plot = (

    ggplot(top_targets)+
    aes(x='target_location', y="count", fill='target_location')+
    geom_bar(stat='identity', position='identity', show_legend=False) +
    labs(title='',x='Target location',y='Frequency')+
    scale_fill_manual(values=['black','gray','silver','lightgrey','rosybrown','firebrick','red','darksalmon','bisque','tan','moccasin'])+
    theme_classic()+
    coord_flip()
)

print(target_plot)


#%%

# --> Reponse definition

# Using plotnine --> works

response_definition = df['full_response_definition'].value_counts().reset_index()

response_plot = (

    ggplot(response_definition)+
    aes(x='full_response_definition', y="count", fill='full_response_definition')+
    geom_bar(stat='identity', position='identity', show_legend=False) +
    labs(title='',x='Full response definition',y='Frequency')+
    scale_fill_manual(values=['black','gray','silver','lightgrey','rosybrown','firebrick','red'])+
    theme_classic()+
    coord_flip()
)

print(response_plot)


#%%

# --> Number of responders vs partial vs non-resp. (Y-BOCS) --> works

df_responders = df[['Study','Full responders','Partial responders','Non responders']].copy()

df_responders.dropna(inplace=True)

df_responders_melted = df_responders.melt(id_vars='Study',var_name='Response Type')

df_responders_melted_1 = df_responders_melted[df_responders_melted['value']!=0].reset_index()

df_responders_melted_1

#%%

bar_plot = ((ggplot(df_responders_melted_1,
    aes(x='Study', y='value', fill='Response Type'))+
    geom_col())+
    coord_flip()+
    labs(title='',x='Study',y='Number of participants')+
    scale_color_identity(labels=['Full responders','Partial responders','Non responders'])+
    theme_classic()
)

print(bar_plot)

# %%
