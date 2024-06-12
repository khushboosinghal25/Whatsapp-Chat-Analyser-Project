import re
import pandas as pd


def preprocess(data):
    # Pattern to match the date and time format
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[APap][mM]\s-\s'

    # Splitting the data into messages and dates
    messages = re.split(pattern, data)[1:]  # The first element is discarded as it's before the first match
    dates = re.findall(pattern, data)

    # Creating the DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Converting message_date to datetime according to the given pattern
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')

    # Renaming the column
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Separate users and messages
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'(^[\w\W]+?):\s', message, maxsplit=1)  # Splitting based on the delimiter
        if len(entry) > 2:  # Check if splitting was successful
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    # Adding new columns to the DataFrame
    df['user'] = users
    df['message'] = messages

    # Dropping the old column
    df.drop(columns=['user_message'], inplace=True)

    # Adding new columns for date and time details
    df['only_date'] = df['date'].dt.date
    df['only_time'] = df['date'].dt.time
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name' , 'hour']]['hour']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df
