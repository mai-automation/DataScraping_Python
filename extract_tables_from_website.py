# Import the pandas library after installing it by running 'pip install pandas' in your terminal
import pandas as pd

# Extract all tables from a webpage, storing them in a list of DataFrames
# *Note: This works only if the webpage's HTML source code contains <table> tags
tb_list = pd.read_html('website_url')

# Display the total number of tables extracted from the webpage
print(len(tb_list))
