

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# read data
def read_data_from_csv(name):
    '''
    this function read data and return in the required form
    '''
    # read data
    df = pd.read_csv(name,skiprows=4)
    
    original_data=df.drop(['Country Code', 'Indicator Code'],axis=1)
    
    countries_data=df.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis=1)
    
    year_data= df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',],axis=1).T
    
    year_data.index.name='Years'
    

    
    # return data transpose and original data with year as column and country as column
    return countries_data,year_data,original_data

    # plot a lie graph
def graph_line_plot(data,indicator,indicator_name,sli):
    '''
    this function plot graph line plot of specific country 
    '''
    # create a dataframe
    factor_data=data[data["Indicator Name"]==indicator]
    
    jap_data=factor_data[factor_data["Country Name"]=="Japan"].drop(['Country Name','Indicator Name'],axis=1)

    oman_data=factor_data[factor_data["Country Name"]=="Oman"].drop(['Country Name','Indicator Name'],axis=1)
    
    south_data=factor_data[factor_data["Country Name"]=="South Africa"].drop(['Country Name','Indicator Name'],axis=1)
    
    italy_data=factor_data[factor_data["Country Name"]=="Italy"].drop(['Country Name','Indicator Name'],axis=1)
  
    # get year data from data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:sli].to_numpy()),jap_data.iloc[0].dropna().to_numpy() , label = "Japan",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:sli].to_numpy()),oman_data.iloc[0].dropna().to_numpy() , label = "Oman",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:sli].to_numpy()),south_data.iloc[0].dropna().to_numpy() , label = "South Africa",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:sli].to_numpy()),italy_data.iloc[0].dropna().to_numpy() , label = "Italy",linestyle="-.")
    
      
    # naming the x axis
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # giving a title to my graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()
    
   
    
 # plot a bar graoh  
def graph_bar_plot(data,indicator,indicator_name):
    '''
    this function draw bar plot graph for the 4 countries year 1995 to 2020
    '''
    #  creating a data frame
    factor_data=data[data["Indicator Name"]==indicator]
    
    jap_data=factor_data[factor_data["Country Name"]=="Japan"].drop(['Country Name','Indicator Name'],axis=1)

    oman_data=factor_data[factor_data["Country Name"]=="Oman"]
    
    south_data=factor_data[factor_data["Country Name"]=="South Africa"]
    
    italy_data=factor_data[factor_data["Country Name"]=="Italy"]
    
    index = ['1995', '2000', '2005',
          '2010', '2015', '2020']
    
    df = pd.DataFrame({'Italy':  [italy_data['1995'].iloc[0],italy_data['2000'].iloc[0],italy_data['2005'].iloc[0],italy_data['2010'].iloc[0],italy_data['2015'].iloc[0],italy_data['2020'].iloc[0],],
                       'Oman': [oman_data['1995'].iloc[0],oman_data['2000'].iloc[0],oman_data['2005'].iloc[0],oman_data['2010'].iloc[0],oman_data['2015'].iloc[0],oman_data['2020'].iloc[0],],
                    'Japan':  [jap_data['1995'].iloc[0],jap_data['2000'].iloc[0],jap_data['2005'].iloc[0],jap_data['2010'].iloc[0],jap_data['2015'].iloc[0],jap_data['2020'].iloc[0],],
                    'South Africa':  [south_data['1995'].iloc[0],south_data['2000'].iloc[0],south_data['2005'].iloc[0],south_data['2010'].iloc[0],south_data['2015'].iloc[0],south_data['2020'].iloc[0],],
                    
                    }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()

# plot a heatmap with annotation
def correlation_heatmap_us(data,name):
    '''
    this function show heatmap and thier correaltion between indicators for better understanding
    '''
    country_data,year_data,data=read_data_from_csv("data.csv")
    #condition for countries specific data
   
    # create data frame
    factor_data=pd.DataFrame()
    
    # getting indicator data
    jap_pov=data[data["Indicator Name"]=="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]
    
    # get united states data 
    jap_pov=jap_pov[jap_pov['Country Name']=="Japan"].drop(['Country Name','Indicator Name'],axis=1).T
    
    # drop nan values
    jap_pov=jap_pov.dropna().T
    
    # get urban population data
    factor_data["Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]=jap_pov.iloc[0]
    
    #  get arable data
    jap_mortality=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
    
    
    jap_mortality=jap_mortality[jap_mortality['Country Name']=="Japan"].drop(['Country Name','Indicator Name'],axis=1).T
    
    jap_mortality=jap_mortality.dropna().T
    
    factor_data['Mortality rate, under-5 (per 1,000 live births)']=jap_mortality.iloc[0]
        
    #  get cereal data
    jap_population=data[data["Indicator Name"]=='Population, total']
        
    jap_population=jap_population[jap_population['Country Name']=="Japan"].drop(['Country Name','Indicator Name'],axis=1).T
        
    jap_population=jap_population.dropna().T
        
    factor_data['Population, total']=jap_population.iloc[0]
        
    jap_Agricultural=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    jap_Agricultural= jap_Agricultural[ jap_Agricultural['Country Name']=="Japan"].drop(['Country Name','Indicator Name'],axis=1).T
        
    jap_Agricultural=jap_Agricultural.dropna().T
        
    factor_data['Agricultural land (sq. km)']= jap_Agricultural.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # plot heatmap
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
                             
            annot=True,ax=ax
                
                )
    # add title
    ax.set_title('Japan')
        
    plt.show()
    
    country_data,year_data,data=read_data_from_csv("data.csv")
    #condition for countries specific data
   
    # create data frame
    factor_data=pd.DataFrame()
    
    # getting indicator data
    italy_pov=data[data["Indicator Name"]=="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]
    
    # get united states data 
    italy_pov=italy_pov[italy_pov['Country Name']=="Italy"].drop(['Country Name','Indicator Name'],axis=1).T
    
    # drop nan values
    italy_pov=italy_pov.dropna().T
    
    # get urban population data
    factor_data["Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]=italy_pov.iloc[0]
    
    #  get arable data
    italy_mortality=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
    
    
    italy_mortality=italy_mortality[italy_mortality['Country Name']=="Italy"].drop(['Country Name','Indicator Name'],axis=1).T
    
    italy_mortality=italy_mortality.dropna().T
    
    factor_data['Mortality rate, under-5 (per 1,000 live births)']=italy_mortality.iloc[0]
        
    #  get cereal data
    italy_population=data[data["Indicator Name"]=='Population, total']
        
    italy_population=italy_population[italy_population['Country Name']=="Italy"].drop(['Country Name','Indicator Name'],axis=1).T
        
    italy_population=italy_population.dropna().T
        
    factor_data['Population, total']=italy_population.iloc[0]
        
    italy_Agricultural=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    italy_Agricultural= italy_Agricultural[ italy_Agricultural['Country Name']=="Italy"].drop(['Country Name','Indicator Name'],axis=1).T
        
    italy_Agricultural=italy_Agricultural.dropna().T
        
    factor_data['Agricultural land (sq. km)']= italy_Agricultural.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # plot heatmap
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
                             
            annot=True,ax=ax
                
                )
    # add title
    ax.set_title('Italy')
        
    plt.show()
    
    country_data,year_data,data=read_data_from_csv("data.csv")
    #condition for countries specific data
   
    # create data frame
    factor_data=pd.DataFrame()
    
    # getting indicator data
    oman_pov=data[data["Indicator Name"]=="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]
    
    # get united states data 
    oman_pov=oman_pov[oman_pov['Country Name']=="Oman"].drop(['Country Name','Indicator Name'],axis=1).T
    
    # drop nan values
    oman_pov=oman_pov.dropna().T
    
    # get urban population data
    factor_data["Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]=oman_pov.iloc[0]
    
    #  get arable data
    oman_mortality=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
    
    
    oman_mortality=oman_mortality[oman_mortality['Country Name']=="Oman"].drop(['Country Name','Indicator Name'],axis=1).T
    
    oman_mortality=oman_mortality.dropna().T
    
    factor_data['Mortality rate, under-5 (per 1,000 live births)']=oman_mortality.iloc[0]
        
    #  get cereal data
    oman_population=data[data["Indicator Name"]=='Population, total']
        
    oman_population=oman_population[oman_population['Country Name']=="Oman"].drop(['Country Name','Indicator Name'],axis=1).T
        
    oman_population=oman_population.dropna().T
        
    factor_data['Population, total']=oman_population.iloc[0]
        
    oman_Agricultural=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    oman_Agricultural= oman_Agricultural[ oman_Agricultural['Country Name']=="Oman"].drop(['Country Name','Indicator Name'],axis=1).T
        
    oman_Agricultural=oman_Agricultural.dropna().T
        
    factor_data['Agricultural land (sq. km)']= oman_Agricultural.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # plot heatmap
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
                             
            annot=True,ax=ax
                
                )
    # add title
    ax.set_title('Oman')
        
    plt.show()
    
    country_data,year_data,data=read_data_from_csv("data.csv")
    #condition for countries specific data
   
    # create data frame
    factor_data=pd.DataFrame()
    
    # getting indicator data
    south_pov=data[data["Indicator Name"]=="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]
    
    # get united states data 
    south_pov=south_pov[south_pov['Country Name']=="South Africa"].drop(['Country Name','Indicator Name'],axis=1).T
    
    # drop nan values
    south_pov=south_pov.dropna().T
    
    # get urban population data
    factor_data["Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]=south_pov.iloc[0]
    
    #  get arable data
    south_mortality=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
    
    
    south_mortality=south_mortality[south_mortality['Country Name']=="South Africa"].drop(['Country Name','Indicator Name'],axis=1).T
    
    south_mortality=south_mortality.dropna().T
    
    factor_data['Mortality rate, under-5 (per 1,000 live births)']=south_mortality.iloc[0]
        
    #  get cereal data
    south_population=data[data["Indicator Name"]=='Population, total']
        
    south_population=south_population[south_population['Country Name']=="South Africa"].drop(['Country Name','Indicator Name'],axis=1).T
        
    south_population=south_population.dropna().T
        
    factor_data['Population, total']=oman_population.iloc[0]
        
    south_Agricultural=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    south_Agricultural= south_Agricultural[ south_Agricultural['Country Name']=="South Africa"].drop(['Country Name','Indicator Name'],axis=1).T
        
    south_Agricultural=south_Agricultural.dropna().T
        
    factor_data['Agricultural land (sq. km)']= south_Agricultural.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # plot heatmap
    heatmap = sns.heatmap(factor_data.corr(), cmap="tab10",
                             
            annot=True,ax=ax
                
                )
    # add title
    ax.set_title('South Africa')
        
    plt.show()
   
    
    
    
    
    
    # main function
if __name__ == "__main__":
    
    country_data,year_data,original_data=read_data_from_csv("data.csv")
    
    graph_bar_plot(original_data,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)','Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)')
    
    graph_bar_plot(original_data,'Mortality rate, under-5 (per 1,000 live births)','Mortality rate, under-5 (per 1,000 live births)')
    
    graph_line_plot(original_data, 'Population, total','Population, total',62)
    
    graph_line_plot(original_data, 'Agricultural land (sq. km)','Agricultural land (sq. km)',60)
    
    correlation_heatmap_us(original_data,"us")
    
