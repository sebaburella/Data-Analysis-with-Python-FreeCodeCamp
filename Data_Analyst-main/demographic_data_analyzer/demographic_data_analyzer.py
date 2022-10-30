import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    avg_age_men = df["age"][df["sex"] == "Male"].mean()
    average_age_men = round(avg_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_degree = df["education"][df["education"] == "Bachelors"].count() / df["education"].count() * 100
    percentage_bachelors = bachelors_degree.round(1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df_bachelors = df["education"][df["education"] == "Bachelors"]
    bachelors_sum = df_bachelors.count()
    bachelor_50K = df_bachelors[df["salary"] == ">50K"].count()
    
    df_masters = df["education"][df["education"] == "Masters"]
    masters_sum = df_masters.count() 
    masters_50K = df_masters[df["salary"] == ">50K"].count()
    
    df_doctorate = df["education"][df["education"] == "Doctorate"] 
    doctorate_sum = df_doctorate.count()
    doctorate_50K = df_doctorate[df["salary"] == ">50K"].count()
    
    sum_higher_education = bachelors_sum + masters_sum + doctorate_sum
    higher_education = sum_higher_education
    
    df_lower_education = df[(df.education != "Bachelors") & (df.education != "Masters") & (df.education != "Doctorate")]
    lower_education = df_lower_education.education.count()
    
    higher_education_50K = bachelor_50K + masters_50K + doctorate_50K
    lower_education_50K = df_lower_education[df["salary"] == ">50K"]

    # percentage with salary >50K
    higher_education_rich = (higher_education_50K / higher_education * 100).round(1)
    
    lower_education_rich = (lower_education_50K.salary.count() / lower_education * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_time = df[df["hours-per-week"] == 1]
    sum_min_time = df_min_time["hours-per-week"].count()
    num_min_workers = sum_min_time
    
    min_time_50K = df_min_time[df["salary"] == ">50K"]
    sum_min_time_50K = min_time_50K["hours-per-week"].count()
    
    sum_min_time_50K / num_min_workers * 100

    rich_percentage = (sum_min_time_50K / num_min_workers * 100).round(1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df["native-country"][df["salary"] == ">50K"].value_counts()
    num_response = df["native-country"].value_counts()
    percentage_highest_earning = (highest_earning_country / num_response * 100).round(1)
    
    
    highest_earning_country = percentage_highest_earning.idxmax()
    highest_earning_country_percentage = percentage_highest_earning.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_50K = df[(df.salary == ">50K") & (df["native-country"] == "India")]
    occupation = india_50K["occupation"].value_counts()

    top_IN_occupation = occupation.idxmax()

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
