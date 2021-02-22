import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease choose City Name between Chicago , New york City and Washington to explore: \n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Wrong input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich Month or all months? \n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("\nWrong Input . Enter a valid month ")
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich Day of the week or all days? \n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("\nWrong day . Enter a Valid day of the week")
            

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month is :" , df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("\n Most common day of the week is :" , df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    if hour == 12:
        str_hr = '12 PM'
    elif hour == 0:
        str_hr = '12 AM'
    else:
        str_hr = '{} AM'.format(hour) if hour < 12 else '{} PM'.format(hour - 12)
    print("\n Most common hour is :" , str_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\n Most commonly used start station is :" , df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("\n Most commonly used end station is :" , df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_trip'] = df['Start Station'].astype(str) + ' ' + df['End Station'].astype(str)
    print("\n Most combination trip from start and end station week is :" , df['combination_trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total trip duration is", df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("Total trip mean is", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print("User type counts :",user_types)
    


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_cnt = df.groupby(['Gender'])['Gender'].count()
        print("Gender Counts :",gender_cnt)
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_yob = int(df['Birth Year'].min())
        recent_yob = int(df['Birth Year'].max())
        com_yob = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth : ', int(df['Birth Year'].min()))
        print('Most Recent year of birth : ', int(df['Birth Year'].max()))
        print('Most Common year of birth : ', int(df['Birth Year'].mode()))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df,city):
    """Displays raw data (5 rows) in interactive fasion based on users input 
    until they say stop."""
    
    x_rows = 5
    x_start = 0
    x_end = x_rows - 1
    
    print("\nWould you like to see raw data of {} ?".format(city))
    
    while True:
        raw_data = input("\nEnter yes or no :\n")
        if raw_data.lower() == 'yes':
            print("\n",df.iloc[x_start : x_end + 1])
            x_start = x_start + x_rows
            x_end = x_end + x_rows
            
            print('\nWould you like to see the next {} rows?'.format(x_rows))
            continue
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df,city)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
