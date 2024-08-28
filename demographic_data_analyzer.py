import pandas as pd

def demographic_data_analyzer():
    # خواندن داده‌ها از فایل CSV
    df = pd.read_csv('adult.data.csv')

    # پاسخ به سوالات مختلف
    race_count = df['race'].value_counts()
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100

    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (no_advanced_education[no_advanced_education['salary'] == '>50K'].shape[0] / no_advanced_education.shape[0]) * 100

    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100

    country_income = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    highest_earning_country = (country_income / country_count * 100).idxmax()
    highest_earning_country_percentage = (country_income / country_count * 100).max()

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # بازگرداندن نتایج
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
