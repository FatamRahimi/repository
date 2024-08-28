from demographic_data_analyzer import demographic_data_analyzer

if __name__ == "__main__":
    results = demographic_data_analyzer()

    # نمایش نتایج
    print("Race Count:\n", results['race_count'])
    print("Average Age of Men:", results['average_age_men'])
    print("Percentage with Bachelors degrees:", results['percentage_bachelors'])
    print("Percentage with higher education that earn >50K:", results['higher_education_rich'])
    print("Percentage without higher education that earn >50K:", results['lower_education_rich'])
    print("Min work time:", results['min_work_hours'], "hours/week")
    print("Percentage of rich among those who work fewest hours:", results['rich_percentage'])
    print("Country with highest percentage of rich:", results['highest_earning_country'])
    print("Highest percentage of rich people in country:", results['highest_earning_country_percentage'])
    print("Top occupations in India:", results['top_IN_occupation'])
