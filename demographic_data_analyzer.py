import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    #acces to df column race and count values return a df with  diferent races as rows and count values of 
    #as columns
    race_count = df["race"].value_counts()

    # What is the average age of men?

    #create a mask filter dataset and convert only male dataset, access age column and calculate the mean
    #the test give me an error of diferrence for (0.03354749885268404 difference) so i decided to round the result

    average_age_men = round(df.loc[df['sex'] == "Male"]['age'].mean(),1)


    # What is the percentage of people who have a Bachelor's degree?
    
    #filter the dataframe by bachelors education and divide that rowshape by totaly rowshape
    df_bachelors = df.loc[df['education'] == "Bachelors"]
    percentage_bachelors = round((df_bachelors.shape[0] / df.shape[0])*100,1)
    
   

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education_mask = ((df["education"] == "Bachelors") | 
                            (df["education"] == "Masters") |    
                            (df['education'] == "Doctorate" ))

    lower_education_mask = ((df["education"] != "Bachelors") &
                            (df["education"] != "Masters") &  
                            (df['education'] != "Doctorate" ))

    higher_education_df = df.loc[higher_education_mask]
    lower_education_df = df.loc[lower_education_mask]
    # percentage with salary >50K
    rich_higher_porcentage = (higher_education_df['salary'].value_counts()['>50K']/higher_education_df.shape[0])*100
    rich_lower_porcentage = (lower_education_df['salary'].value_counts()['>50K']/lower_education_df.shape[0])*100

    higher_education_rich = round(rich_higher_porcentage,1)
    lower_education_rich = round(rich_lower_porcentage,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers_df = df.loc[df['hours-per-week'] == min_work_hours]
    porcentage_min_workers_rich = (min_hours_workers_df['salary'].value_counts()['>50K']/min_hours_workers_df.shape[0])*100

    rich_percentage = round(porcentage_min_workers_rich,1)

    
    people_rich_in_rich_Country = df.loc[df['salary'] == ">50K"]['native-country'].value_counts()
    people_in_rich_country = df['native-country'].value_counts() 

    align_series = people_in_rich_country.align(people_rich_in_rich_Country, join='outer')

    porcentages_series = (align_series[1]/ align_series[0])*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = porcentages_series.sort_values(ascending=False).index[0]
    

    highest_earning_country_percentage = round(porcentages_series.sort_values(ascending=False)[0], 1)

    
    indian_df = df.loc[df['native-country'] == "India"]
    rich_in_india_df = indian_df.loc[df["salary"] == ">50K"]
    
    #search indian_df, only indian country, then richs in india by salary and for the last value counts and 
    #use the index[0] for look at the most popular occupation


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = rich_in_india_df['occupation'].value_counts().index[0] 

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    #returns the country with the highest porcentage of rich people
