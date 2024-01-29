import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Series
s = pd.Series([3,5,7,9])
s
#인덱스 지정
s2 = pd.Series([3,5,7,9], index = ['a','b','c','d'])
s2
type(s2)
s2['a']
s2[0]

#함수
s.index
s.values


#딕셔너리 시리즈
pop_dict = {
    '서울': 9543,
    '도쿄': 37340,
    '토론토': 6255,
    '뉴욕': 18823,
    '파리': 11079,
    '베를린': 3567,
    '런던': 9426
}

population = pd.Series(pop_dict)
population
population['서울']
population[0]    #딕셔너리랑 다르게 인덱싱이 가능
population *1000

population.index
population.values

##DataFrame

#리스트
data = [
    ['대한민국', '서울', 9543],
    ['일본', '도쿄', 37340],
    ['캐나다', '토론토', 6255],
    ['미국', '뉴욕', 18823], 
    ['프랑스', '파리', 11079],
    ['독일', '베를린', 3567],
    ['영국', '런던', 9426]
]

df = pd.DataFrame(data)
df

#열이름 정하기
df = pd.DataFrame(data, columns = ['Country', 'City', 'Population'])
df #리스트를 열이름을 일일이 정하는 번거러움이 있을 수 있음.


#딕셔러니
data2 = {
     'Country':['대한민국', '일본', '캐나다','미국', '프랑스', '독일', '영국'],
     'City':['서울','도쿄','토론토','뉴욕','파리','베를린','런던'],
     'Population':[9543., 37340, 6255, 18823, 11079, 3567, 9426]
 }
df2 = pd.DataFrame(data2)
df2
#행이름 정하기
df2 = pd.DataFrame(data2, index=['a','b','c','d','e','f','g'])
df2

type(df2)
type(df2['Country'])  #시리즈가 모여서 데이터프레임 생성('열(세로)'씩 모임)

df.info()


##행렬 조작
df
df_index = df.set_index('Country')
df_index        #Country  열을 열 이름으로 정하기

df_index2 = df.set_index(['Country', 'City'])
df_index2  #두개로 줄 수도 있음.



#######인덱싱

#df.loc[행][열]   -> 행 혹은 특정성분인 행렬 값
#df[열][행]  -> 열 추출 혹은 특정성분인 행렬 값 추출  정확히는 딕셔너리라서 키 값을 적어야 함. 그 키값이 열에 있음.
#df_index2 에서 country, city는 행의 이름 임
df_index2
df_index2.loc[('대한민국', '서울')]
df_index2.loc['대한민국'] #행이름 둘 중 하나만 써도 혹은 두개 써도됨
df_index2.loc[0]   #행의 이름이 안맞아서 오류남 

df_index2.iloc[0]  #이때는 iloc를 씀 즉 loc는 그 이름을 직접, iloc는 인덱스를 씀
df_index2.iloc[0,0]

df_index2['대한민국']  #대한민국은 행이름이므로 오류남
df_index2['Population'] #모든 열 출력 그냥 [] 인덱싱 쓰는 것은 열 출력임.


#예제
# #대한민국 인구가 다른나라에 비해 몇배인지 구하기
df_index_with_country=df_index
df_index_with_country
a=df_index_with_country['Population']   #해당열
b=df_index_with_country.loc['대한민국']['Population']  #특정 행렬 성분
a/b




#연산 등등
s = pd.Series([3,5,7,9], index = ['a','b','c','d'])
s

s1 = s[['a','b']]
s1

s2 = s[['b','c']]
s2

s1+s2  #b만 연산되어서 10이나오고 a,c는  NaN로 처리




###################################################
#자료 export, import

#자료 내보내기
jason_data = df.to_json()
jason_data
#자료  import 하기
pd.read_json(jason_data)

#!wget은 코랩에서만 됨.
#csv 확장자로 저장하기
# !wget -O 'iris_sample.csv' https://raw.githubusercontent.com/duc-ke/edu_jupyter_pandas/master/dataset/iris_sample.csv

#tsv로 다음 파일을 다운받기(저장) tsv는 탭으로 구분됨
#!wget -O 'iris_sample.tsv' https://gist.githubusercontent.com/mbostock/3305937/raw/a5be7c5fd55c4fa0ca8a400cb68d658a40989966/data.tsv

#파일 불러오기
import pandas as pd
df_iris  = pd.read_csv('iris_sample.txt')  #.csv로 저장햇다면 csv로 함
df_iris

#tsv는 읽을 때 sep를 \t로 해야함.
pd.read_csv('iris_sample.tsv' , sep="\t")

#export(csv)
df_iris.to_csv('iris_sample2.csv')  #csv는 자동으로 엑셀로 됨(확장자 안정해주면)  
df_iris.to_csv('iris_sample2.txt')  #메모장으로 저장 

#import(csv)
pd.read_csv('iris_sample2.csv')
#왼쪽이 열이 하나 더 생김 


#열하나 생기는거 방지하는 법
df_iris.to_csv('iris_sample2.csv', index = False)  #export 할때 index false를 함.
pd.read_csv('iris_sample2.csv')

# 엑셀사용하기

#!pip install xlsxwriter
#비쥬얼 코드에서는 ! 빼고 터미널에서 실행하면 됨.
df_iris.to_excel('iris_sample.xlsx', index = False, sheet_name='iris1')

pd.read_excel('iris_sample.xlsx', sheet_name = 0) #혹은 시트 네임그대로 써도 됨
pd.read_excel('iris_sample.xlsx', sheet_name = 'iris1')


#데이터베이스 사용하기
import pandas as pd
# !pip install mysql_connector-python
import sqlalchemy
user = 'anonymous'
host = 'ensembldb.ensembl.org'
port = '3337'
database = 'ailuropoda_melanoleuca_core_79_1'
url = f'mysql+mysqlconnector://{user}@{host}:{port}/{database}'
# url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{databas}'
connection = sqlalchemy.create_engine(url)
connection
pd.read_sql('select * from analysis limit 10', connection)
###############################################################




# 슬라이싱
df2['a':'d']  #행이름이 문자열 슬라이싱이라면 'd'까지

df
df[1:5]
df.iloc[0:1, 0:2]
df.loc[0:1, 'Country':'City']  #name 으로 해서 행도 끝자리 들어감.
df.loc[0:0, 'Country':'City'] 


#불리언 인덱싱

condition  = df['Population'] > 10000
condition = df.loc[:,'Population'] >10000
condition  = df.iloc[:, 2] >10000
condition

df[condition]  #해당 조건식을 인덱스 해주면 됨.



data ={
    'country': ['Belgium', 'France', 'Germany', 'Netherland', 'United Kingdom'], 
    'population': [11.3, 64.3, 81.3, 16.9, 64.9], 
    'area': [30510, 671308, 357050, 41526, 244820], 
    'capital': ['Brussels', 'Paris', 'Berlin', 'Amsterdam', 'London'],
}

countries = pd.DataFrame(data)
countries = countries.set_index('country')

countries
###예제 (열추가)
popul = countries.loc[:,'population']*1000000
area = countries.loc[:, 'area']
density = popul/area 
countries['density'] = density
countries


countries.drop('density', axis = 1)  #이므로 열삭제, 반환값임.


###density 300이상 구하기
condition = countries['density'] > 300
condition
countries.loc[condition, ['capital', 'population']]   
#loc안에 조건에 맞는 행을 condition을 쓸수 있음
countries[condition][['capital', 'population']]
#인덱싱도 바로 condition 쑬 수 있음

countries.loc[condition]
countries[condition]       #결과는 같음

#하나하나 보면
countries[condition]
#위에서 []하며 열의 이름을 출력 이때 개수가 2개이상이니까 리스트로 묶어줌.
countries[condition][['capital', 'population']]

#행렬성분 변환
countries.loc['United Kingdom','capital'] = 'Manchester'
countries['capital']['United Kingdom'] = 'London'

#다중 조건식

condition = (countries['density'] >= 100) & (countries['density'] < 300) 
 #다중 조건식은 |, &를 써야 하고 괄호를 따로 각각 써야한다.
condition


############인덱싱 loc 다시 정리##########
countries['capital']['France']
countries.loc['France', 'capital']
countries.loc['France']['capital']




### .str .contains
countries['capital'].str.len()  
#.str은 오브젝트 객체에서만 가능하고 여기서는 .len()해야함 .str은 그 안의 요소가 접근하겠다는 것임.

condition = countries['capital'].str.len() >=7
countries[condition]


condition = countries['capital'].str.contains('Lo')

countries[condition]




#없애기
df
df.drop(1) #반환값임. 원본 건드리지 않음. #행을 없애는 것이 기준 axis=0이고 디폴트값
df.drop([2,3])


#열삭제
df.drop('City', axis = 1)# 기본값이 axis=0(행기준)이므로 열이름, axis = 1로 하면됨
df.drop(['Country','City'], axis = 1)  #inplace = True를 주면 원본이 바뀜.



#여러함수
df
df.describe()
df.sort_values('Population')
df.sort_values('Population', ascending =False)
df.count()
df.sum()
df.max()
df.min()
df.mean()
df.median()


#결측치
df.isnull()
df.isnull().any() #어느 하나라도 True가 없다 기본값은 axis=0
df.isnull().any(axis=1)
df.isnull().any().any() #전체


df2 = df.copy()
df2.loc[0,'Population'] = None
df2
df2.isnull().any()
df2.isnull().any(axis=1)
df2.isnull().any().any()







########apply 함수
df

df.loc[:, 'Population':'Population'] #차원유지를 위해서 슬라이싱


df.loc[:, 'Population':'Population'].apply(lambda x: x*1000)  #apply안에 함수를 넣어주면됨

def mul(a):
  return a*1000

df.loc[:, 'Population':'Population'].apply(mul)




#######groupby
#split->apply(sum)->combine(각 요소들의 결과값 모으기)



df2 = pd.DataFrame({
    '과목':['국','수','영','국','수','영', '국','수','영'],
    '점수':[100,80,80,95,85,75,70,60,50]

})
df2

 #열의 모든 성분 값들을 표시(중복제외)
df2['과목'].unique()
df2['점수'].unique()





korean = df2['과목']=='국' 
df2[korean]#split
df2[korean].mean() #apply


df2.groupby('과목').mean()#str중에서 unique로 구분된 요소들(국,수,영)의 각각에 대한 정보를 나타냄.





#####타이타닉 예제
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df


#성별에 따른 평균나이
df['Sex'].unique()  #성별열의 요소들 확인하기

df.groupby('Sex')   #성별로 추출하고


df.groupby('Sex').mean()  #그에 해당하는 모든열 출력

df.groupby('Sex').mean()['Age']  #그 중에서 Age열만 출력



df.groupby('Sex')['Age']  #Age만 뽑아내고
df.groupby('Sex')['Age'].mean() #여기서 평균구하기 위보다는 빠름.


#25세이상의 생존률
condition = df['Age'] <=25

df[condition]
df[condition]['Survived'].mean()







