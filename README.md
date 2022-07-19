# bct_analysis

WCS data was clustered based on color chip responses. This script presents some
simple analysis to guide further investigations.

## Usage
In a directory with `speaker.xlsx`,


`python bct_analysis.py`

outputs a series of csv files with contingency table data.

Specifically, the difference between the real `cluster_id`/column table and
the expected one if the features were independent.
