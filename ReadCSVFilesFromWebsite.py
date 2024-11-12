# Import the pandas library, typically used for data manipulation and analysis
import pandas as pd

# Read a CSV file from a URL, which contains football data, and load it into a DataFrame
# The DataFrame 'csv_dataframe' will contain the structured data from the CSV file
csv_dataframe = pd.read_csv('csv_file_name')

# Print the entire DataFrame to display the contents of the CSV file
print(csv_dataframe)

# Rename specific columns in the DataFrame to more descriptive names for clarity
# Updating the DataFrame directly by setting inplace=True.
csv_dataframe.rename(columns={'culumn_name_to_replace1': 'replaced_name1', 'culumn_name_to_replace2': 'replaced_name2'}, inplace=True)

