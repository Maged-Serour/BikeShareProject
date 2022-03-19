import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ["all", "january", "february", "march", "april", "may", "june"]

WEEK_DATA = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Defining the city variable globally to use in the "user_stats" function
    #global city

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        city = input("\nPlease specify the city you want to analyze the data for (Chicago / New York City / Washington):\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("\nYou entered an invalid city name. Please try again\n")

    # TO DO: get user input for month (all, january, february, ... , june)

    month = ''
    while month not in MONTH_DATA:
        month = input("\nPlease specify the month you want to see the data for\nYou can select from January to June\nOr type 'All' to see all data\n").lower()
        if month in MONTH_DATA:
            break
        else:
            print("\nYou entered an invalid input. Please try again.\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    while day not in WEEK_DATA:
        day = input("\nPlease select the day of the week to see its data\nYou can type 'All' to see all data\n").lower()
        if day in WEEK_DATA:
            break
        else:
            print("\nYou entered an invalid input. Please try again.\n")



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df['day_of_week'] = day


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[common_month].title())


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day.title())


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common starting hour is: {}:00".format(common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common starting station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is :" + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " and " + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print("The most frequent trip is between {} stations".format(common_trip))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is {}.".format(time.strftime('%H:%M:%S', time.gmtime(total_travel_time))))


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average time taken for trips is {}.".format(time.strftime('%H:%M:%S', time.gmtime(average_travel_time))))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The filtered data contains:\n" + str(user_type))

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    #if city == "new york city" or city == "chicago":
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print("The filtered data contains:\n" + str(user_gender))
        oldest_user = df['Birth Year'].min()
        youngest_user = df['Birth Year'].max()
        most_common_birth_year = int(df['Birth Year'].mode())
        print("The oldest user is {} years old.".format(2021 - int(oldest_user)))
        print("The youngest user is {} years old.".format(2021 - int(youngest_user)))
        print("The most common year of birth is " + str(most_common_birth_year) + ".")
    else:
        print("\nThat's all the user stats available for the selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    valid_responses = ["yes" , "no"]


    while view_data not in valid_responses:
        print("You entered an invalid response.")
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()

    while view_data == "yes":
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to display 5 more rows?: ").lower()
        while view_data not in valid_responses:
            print("You entered an invalid response.")
            view_data = input("Do you wish to display 5 more rows?: ").lower()
        else:
            if view_data == "no":
                print("Have a nice day.")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
