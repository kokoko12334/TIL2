
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:/Users/user/Desktop/data/word2vec-nlp-tutorial/'



train_data = pd.read_csv(path + "labeledTrainData.tsv", header = 0, delimiter='\t', quoting = 3)





train_data.head()



print('전체 학습 데이터의 개수:{}'.format(len(train_data)))

review_lenth = train_data['review'].apply(len)
review_lenth





