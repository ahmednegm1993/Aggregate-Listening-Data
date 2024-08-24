import pandas as pd
df=pd.read_excel(r'E:\Data_analysis_projects\Aggregate Listening Data\dataset\Aggregate Listening Data.xlsx')
df1=df.groupby('user_id').agg(
    unique_song_count=('song_id',pd.Series.nunique),
total_listen_duration=('listen_duration',lambda x: round(x.sum()/60)))

print(df1.sort_values('total_listen_duration',ascending=False))