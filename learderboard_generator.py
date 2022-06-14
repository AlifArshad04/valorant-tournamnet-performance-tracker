from cmath import nan
import pandas as pd
import numpy as np

# getting igns #
col_toGet = ['Team Name', 'Team Captain\'s Name', 'Team Captain\'s Valorant IGN', '2nd Player\'s Name', '2nd Player\'s Valorant IGN', '3rd Player\'s Valorant IGN', '3rd Player\'s Name',
             '4th Player\'s Valorant IGN', '4th Player\'s Name', '5th Player\'s Valorant IGN', '5th Player\'s Name', '6th Player\'s Valorant IGN', '6th Player\'s Name', '7th Player\'s Valorant IGN', '7th Player\'s Name']
df_info = pd.read_csv('Team Information.csv', usecols=col_toGet)
# df_info.replace(np.nan, '', regex=True, inplace=True)


# copying players to leaderboard dataframe #

df_ldb = pd.DataFrame(columns=['Name', 'IGN', 'Team'])

df_temp = df_info[['Team Captain\'s Name',
                  'Team Captain\'s Valorant IGN', 'Team Name']]
df_temp.columns = ['Name', 'IGN', 'Team']
df_ldb = pd.concat([df_ldb, df_temp], ignore_index=True)

pos = ['2nd', '3rd', '4th', '5th', '6th', '7th']
for i in pos:
    df_temp = df_info[['{} Player\'s Name'.format(i),
                       '{} Player\'s Valorant IGN'.format(i), 'Team Name']]
    df_temp = df_temp[df_temp['{} Player\'s Valorant IGN'.format(i)].notna()]
    df_temp.columns = ['Name', 'IGN', 'Team']
    df_ldb = pd.concat([df_ldb, df_temp], ignore_index=True)


# adding stat columns #
df_ldb['Played'] = 0
df_ldb['avg ACS'] = np.nan
df_ldb['K'] = 0
df_ldb['D'] = 0
df_ldb['A'] = 0
df_ldb['K/D'] = 0.0
df_ldb['HS%'] = np.nan
df_ldb['Ace'] = 0


# loading match data from result.txt file #
result = pd.read_csv('match results.csv')
result.replace(np.nan, '', regex=True, inplace=True)


# inserting data in leaderboaord dataframe #
valid_igns = df_ldb['IGN'].tolist()
# print(len(valid_igns))

for index, row in result.iterrows():
    ign = row['ign']
    if (ign.find('#') != -1):
        if ign in valid_igns:
            filt = (df_ldb['IGN'] == ign)

            df_ldb.loc[filt, 'Played'] += 1

            if pd.isnull(df_ldb.loc[filt, 'avg ACS']).values.any():
                df_ldb.loc[filt, 'avg ACS'] = float(row['ACS'])
            else:
                df_ldb.loc[filt, 'avg ACS'] = (
                    df_ldb.loc[filt, 'avg ACS'] + float(row['ACS'])) / 2

            df_ldb.loc[filt, 'K'] += int(row['K'])
            df_ldb.loc[filt, 'D'] += int(row['D'])
            df_ldb.loc[filt, 'A'] += int(row['A'])

            if pd.isnull(df_ldb.loc[filt, 'HS%']).values.any():
                df_ldb.loc[filt, 'HS%'] = float(row['HS%'])
            else:
                df_ldb.loc[filt, 'HS%'] = (
                    df_ldb.loc[filt, 'HS%'] + float(row['HS%'])) / 2

            df_ldb.loc[filt, 'Ace'] += int(row['Ace'])

        else:
            print("NOT FOUND", ign)

df_ldb['K/D'] = df_ldb.K / df_ldb.D


# saving dataframe to a csv file #
df_ldb.to_csv("individual.csv", index=False)
