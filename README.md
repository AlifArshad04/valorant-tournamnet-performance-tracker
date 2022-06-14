# Valorant Tournamnet performance Tracker
A simple python project to get individual statistics from a csv file of match summaries of Valorant matches. This code has been tested using match summaries taken from tracker.gg which was manually formated as per our need. But it should work with any other tracker or other sources as long as you can generate an csv file with all the match results, IGNs and stats in them and modify the column names accordingly. Feel free to create an issuse in this github reposirtory if you face any problem using the code.

## Dependencies
Pandas and Numpy. You can install them using
```python
pip install pandas numpy
```

## How to use it
Two csv files are needed to run this code: `Team Information` and `match results`. Sample files are given and just runnig the code as is will generate a file named `individual` which will help you understang what this program does. You can oviouslty play with the code to get the stats you want to track.

## How the code works
The progrma first reads the IGNs, name and team name form `Team Information` and puts it in a dataframe. Then it parses through each line of `match results` file and if that line contains a ign, the programs searched for that ign in the previouly created dataframe. If the ign is not found, it prints the ign along with a error message in the terminal and moves on the the next line. And if the ign is found, it updates the stats in the dataframe. Once the parsing ends, the program generates new column/columns based on other columns (such as a new K/D column using kills and deaths column). And lastly, it writes the dataframe in the `individual` csv file which can be easily imported to a Excel, Google Sheet, Libre Calc or similar applications.
