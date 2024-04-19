
# CSV to ICS Generator

Download this python script and run it on your computer to generate .ics calendar files from a .csv file.


## Intended Use

- Generating custom "Add to Calendar" files for marketing emails## Usage/Examples

## How to Use

1. To use the script, download `csv_to_ics_converter.py` and `sample.csv` to your computer.

2. Modify `sample.csv` or make a copy and fill in your own information. Each row will create a new .ics calendar file.
    - Your datetime format should be ISO 8601.
      - If you are having trouble converting in Excel, ChatGPT can actually convert in bulk with the correct timezone as long as you are specific.

3. Open `csv_to_ics_converter.py` in a code editor and modify line 46 to update your input CSV file (ideally in the same directory as your script).
```python
csv_file_path = 'input-file.csv'
```

4. Additionally, modify line 49 to state your output folder. 
```python
output_folder = 'C:\\Users\\YOURPATHHERE'
```

5. For the final modification, update line 38 with your .ics filename structure. Use the row titles declared on lines 14-19 to customize the name and add your own unique string if desired.

6. To run the script, open the directory that contains the script in your terminal and run this command:
```python
python csv_to_ics_converter.py
```
