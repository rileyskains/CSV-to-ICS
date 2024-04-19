# Import required libraries
from ics import Calendar, Event
import pandas as pd
import arrow

# Function to convert CSV to ICS
def convert_csv_to_ics(csv_file_path, output_folder):
    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate through rows
    for index, row in df.iterrows():
        # Extract data from the row
        event_title = row['EventTitle']
        start_datetime_str = row['StartDateTime']
        end_datetime_str = row['EndDateTime']
        location = row['Location']
        event_description = row['Description']
        company = row['Company']

        # Convert date and time strings to arrow objects
        start_datetime = arrow.get(start_datetime_str)
        end_datetime = arrow.get(end_datetime_str)

        # Create an event
        event = Event()
        event.name = event_title
        event.begin = start_datetime
        event.end = end_datetime
        event.location = location
        event.description = event_description

        # Create a calendar and add the event
        cal = Calendar()
        cal.events.add(event)

        # Save the ICS file. Update filename to include fields and custom string if needed.
        ics_filename = f'{output_folder}/{company}-CUSTOMSTRING.ics'
        with open(ics_filename, 'w') as f:
            f.write(str(cal))
        print(f'ICS file "{ics_filename}" created successfully.')

# Main execution
if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the path to your CSV file
    csv_file_path = 'input-file.csv'

    # Replace 'output_folder' with the folder where you want to save the ICS files. Files will be dumped into this folder.
    output_folder = 'C:\\Users\\YOURPATHHERE'

    # Create ICS files
    convert_csv_to_ics(csv_file_path, output_folder)

    # put this in your terminal to run: python csv_to_ics_converter.py