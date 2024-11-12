# You can import pandas after installing it by running 'pip install pandas' in terminal
import pandas as pd
# Extract all tables from a website *Note: this works only if the web source code contains <table>tags.
tbs = pd.read_html('URL')
# Check how many tables have been extracted
len(tbs)
