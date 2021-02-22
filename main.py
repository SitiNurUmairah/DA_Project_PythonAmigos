#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse top 3 countries in the region over a span of 10 years
#Name: Umairah
#Group Name: PYTHON_AMIGOS
#Class: PN2004L
#Date: 11/2/2021
#Version: 
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd 
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################
def sortCountry(df):

  #display sorted dataframe based on given year range of region (1998-2008)
  print("The countries in Asia Pacific region are shown below.")
  print("Given year range: 1998-2008" + "\n")

  #columns & rows for Asia Pacific Region
  AsiaPacificRegion = df.iloc[240:372, 9:14]
  df1 = df.iloc[240:372,0:2]
  result = df1.join(AsiaPacificRegion)
  
  #print Asia Pacific Region (1998-2008)
  print(result)

  #display the top 3 countries in the region that visited Singapore over the span of 10 years
  print("\n" + "The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years:")
  print(df.iloc[240:372, 9:14].sum(axis=0).sort_values(ascending=False).nlargest(3))

   
  #print the top 5 countries
  print("\n" + "The Top 5 countries of visitors to Singapore from the selected region over the span of 10 years:")
  print(df.iloc[240:372, 9:14].sum(axis=0).sort_values(ascending=False).nlargest(5))  

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################

#pie chart to display the top 3 countries
import matplotlib.pyplot as pit
activities = ['China', 'Japan', 'Korea, Republic Of','Hong Kong', 'Taiwan']
slices = [7804293,7494724,3754517,3044686,2546998]
colors = ['r', 'g', 'm', 'p', 'y']
pit.pie(slices,
          labels=activities,
          startangle=90,
          shadow=True,
          explode=(0.2, 0, 0, 0, 0),
          autopct='%1.2f%%')

pit.legend()

pit.show()








#sry idk how