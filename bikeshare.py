import pandas as pd
import datetime
import time

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\n1.Select the CITY to filter, the options are:\n \nChicago\n \nNew York City\n \nWashington\n \n1. Please enter the name of the City: ').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('\n........Please enter the name of the City correctly........')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('\n2.Select the MONTH to filter, the options are:\n \nJanuary\n \nFebruary\n \nMarch\n \nApril\n \nMay\n \nJune\n \nall (for no time filter)\n \n2. Please enter the name of the Month: ').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('\n........Enter correctly the name of the Month you want to filter........')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\n3.Select the DAY to filter, the options are:\n \nMonday\n \nTuesday\n \nWednesday\n \nThursday\n \nFriday\n \nSaturday\n \nSunday\n \nall (for no time filter)\n \n3. Please enter the name of the Day: ').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'saturday', 'all'):
            print('\n........Enter correctly the name of the Day you need to filter........')
            continue
        else:
            break

    print('-'*40 + ' 1. Data entered correctly')
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
    #Load csv City
    df = pd.read_csv((city.replace(' ', '_') + '.csv').lower())

    #Change column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')

    #Create month column
    df['month'] = df['Start Time'].dt.month

    #Create day of week column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter month
    if month!= 'all':
        #Filter index
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #Filter month index
        df = df[df['month'] == month]

    #Filter day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print('-'*40 + ' 2. Dataframe load correctly')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month: ', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day: ', common_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nMost Commonly used Start Station: ', start_station)
    
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nMost Commonly used End station:', end_station)

    # display most frequent combination of start station and end station trip
    concat_station = '-From- ' + df['Start Station'] + ' -To- ' + df['End Station']
    concat_station = str(concat_station.value_counts().idxmax())
    print('\nMost frequent combination of Station and End Station trip are:\n', concat_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    total_travel_time = datetime.timedelta(seconds = total_travel_time)
    print('Total travel time: ' + str(total_travel_time))

    # display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    mean_travel_time = datetime.timedelta(seconds = mean_travel_time)
    print('Mean travel time: ' + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The total per user type are:\n' + str(user_types))

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nThe total by gender is: \n' + count_gender.to_string())

    print('-'*40)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.keys():
        print('\nEarliest birth year: ' + str(df['Birth Year'].min()))
        print('Most recent birth year: ' + str(df['Birth Year'].max()))
        print('Most common birth year: ' + str(df['Birth Year'].mode()[0]))
    else:
        print('Birth year not found')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def five_lines_data(df, city):
    count = 0
    five_data = input('\nWould you like to see more information about: {}? Enter yes or no.\n'.format(city.title()))
    while five_data.lower() == 'yes':
        df_five = df.iloc[count: count + 5]
        print(df_five)
        count += 5
        five_data = input('\nWould you like to see more information about: {}? Enter yes or no.\n'.format(city.title()))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        five_lines_data(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
