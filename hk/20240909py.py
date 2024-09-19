import pandas as pd

df = pd.read_csv("data_1955_20240920.csv", index_col=False)

summ = len(df)
go  = len(df[df['등락률'] >= 1])

go/summ


