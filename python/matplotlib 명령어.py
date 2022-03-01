
# #코랩에서 한글폰트 깔기
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


#한글설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False #깨짐방지
#스타일 설정
plt.style.available
plt.style.use('seaborn-poster')


#라인플랏
#플랏 종류: 
# 
# ax.plot(x,y),plt에서 지원함, ax는 그냥 아무 변수나 지정 fig, ax = plt.subplots()로 할당 필요
# data.plot(), pandas
# plt.plot(x,y)  ,plt  에서 지원함.  plt.plot(x,y)가 상세한 설정 가능

#ax는 numpy의 array에 작동하고
#data.plot()은 pandas에 Series와 데이터프레임이 작동하고
#plt.은 둘 다 작동이 됨.

#############ax.plot############
x = np.linspace(0,10,100)
y = 4 + 2 * np.sin(2*x)

fig, ax = plt.subplots()  #plot창 여러개

ax.set( 
    xlim=(0,8),  #범위
    xticks = np.arange(1,8),   #눈금
    ylim = (0,8),
    yticks = np.arange(1,8)
)


ax.plot(x,y, linewidth = 2.0)  #x,y값표시


##################### 데이터.plot()##############

s = pd.Series(np.random.rand(10).cumsum(), index = np.arange(1,100, 10))
              
s
s.plot(figsize=(5,5))      #plot의 크기



############# plt.plot(x,y)##############
df  = pd.DataFrame(
    np.random.randn(10,4),
    index =np.arange(1,100,10),
    columns = ['A', 'B', 'C', 'D']

)
df

df.plot()
plt.figure()
plt.plot(df.index, df['A'])  #plt.plot(x,y)
plt.plot(df.index, df['B'])
plt.plot(df.index, df['C'])
plt.plot(df.index, df['D'])
plt.title('고민표')
plt.legend(df.columns) #범례




#막대 그래프


####ax.bar()######
np.random.seed(3)       #seed는 초기값
x= 0.5 +np.arange(8)
y = np.random.uniform(2,7, len(x))
fig, ax= plt.subplots()

ax.bar(x,y,width=1,edgecolor = 'white', linewidth=0.7 )
ax.set(
    xlim = (0,8), 
    xticks=np.arange(1,8),
    ylim = (0,8), 
    yticks=np.arange(1,8)
)
plt.show()

######데이터.plot()#########
s = pd.Series(
    np.random.rand(16),
    index = list('abcdefghijklmnop')
    
    )
s
s.plot(kind = 'bar') #pandas
plt.xticks(rotation = 0)

#####plt.bar ###########
plt.bar(s.index, s) #matplotlib
plt.xticks(rotation = 0)



#####이외에 가로 막대 그래프######
s.plot(kind = 'barh')
plt.barh(s.index,s)





###### 여러 독립변수의 막대그래프를 표현
data = np.random.rand(6,4)

index = ['one', 'two', 'three', 'four', 'five', 'six']
columns = pd.Index(['A','B', 'C', 'D'])


df = pd.DataFrame(
    data,
    # index = index,
    columns = columns
)
df
df.plot(kind = 'bar')

###########이렇게 하면  겹쳐서 씹히는 것이 있음
plt.bar(df.index, df['A'])
plt.bar(df.index, df['B'])
plt.bar(df.index, df['C'])
plt.bar(df.index, df['D'])

plt.xticks(df.index, index)
plt.show()

###다음과 같은 방법으로 구역을 나눔
w = 0.2
plt.bar(df.index-2*w, df['A'], width = w)
plt.bar(df.index-w, df['B'], width = w)
plt.bar(df.index, df['C'], width = w)
plt.bar(df.index+w, df['D'], width = w)
plt.xticks(df.index, index)
plt.show()
##가로 그래프

df.plot(kind = 'barh', stacked = True)

plt.barh(df.index, df['A'])
plt.barh(df.index, df['B'])
plt.barh(df.index, df['C'])
plt.barh(df.index, df['D'])
plt.show()


########히스토그램############
np.random.seed(1)
x = 4+ np.random.normal(0,1.5, 200)

fig, ax = plt.subplots()

ax.set(
    xlim=(0,8), 
    xticks = np.arange(1,8),
    ylim=(0,56), 
    yticks = np.arange(0,56,9)
    )


ax.hist(x)

plt.hist(x)
plt.show()





s = pd.Series(np.random.normal(0,1,size = 200))
s.hist(bins=50) #bins는 구간이고 디폴트는 10임 이 구간에 포함된것을 표현
s.hist()

plt.hist(s)






#산점도
#numpy, ax
np.random.seed(3)
x = 4 + np.random.normal(0,2,24)
y = 4+ np.random.normal(0,2,len(x))
sizes = np.random.uniform(15,80, len(x))
colors = np.random.uniform(15,80, len(x))

fig, ax = plt.subplots()

ax.scatter(x,y, s=sizes, c=colors, vmin=0, vmax=100 )

ax.set(
    xlim=(0,8), 
    xticks = np.arange(1,8),
    ylim=(0,8), 
    yticks = np.arange(1,8)
    )

plt.show()
#혹은 다 하고나서

fig

#plt 
x2 = np.random.normal(-2,4, size=(100,1))
x1 = np.random.normal(1,1, size=(100,1))
x =np.concatenate((x1,x2), axis=1)
df = pd.DataFrame(x, columns = ['x1','x2'])
plt.scatter(df['x1'], df['x2'])

plt.show()



# fig(도화지) , ax(그리는 부분)    numpy기능임.
fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)    #(행,렬,위치)

ax2 = fig.add_subplot(2,2,2)

ax3 = fig.add_subplot(2,2,3)


ax1.plot(np.random.randn(50).cumsum())  #ax1.그래프안에 다음을 넣는다.
ax2.hist(np.random.randn(100), bins=20)
ax3.scatter(np.arange(30), np.arange(30))
fig


### 3*3행렬 도화지 그리기
fig = plt.figure()
n = 1
for i in range(1,10):
    globals()[f'ax{i}']= fig.add_subplot(3,3,i)   
    #globals()는 딕셔너리 형태로, 인덱싱안에 변수명을 입력해서 딕셔너리와 같은 방법으로 변수 추가가능
    
    print(f'ax{i}')


##plt.subplots

fig, axes =plt.subplots(1,3, figsize = (15,5))  
#1,3행렬의 fig(종이)를 생성하고  fig, axex에는 각 부분을 할당
axes[0].plot(np.random.randn(50).cumsum())
axes[1].hist(np.random.randn(100), bins =20)
axes[2].scatter(np.arange(30), np.arange(30))
fig



###여러 기능 plt.plot
plt.figure()
plt.plot(np.random.randn(30), color = 'g', marker = 'o', linestyle = '--')

plt.figure()
plt.plot(np.random.randn(30), 'go--')         
#한번에 하는 방법 순서는 컬러, 마커, 라인스타일

##data.plot (pandas)
fig, axes = plt.subplots(2,1, figsize=(8,7))

data = pd.Series(np.random.rand(16))
index = list('abcdefghijklmnop')

data.plot(kind = 'bar', ax = axes[0], color = 'k', alpha =1)

data.plot(kind = 'barh', ax = axes[1], color = 'g', alpha =0.3)
plt.show()


fig, axes = plt.subplots(2,1, figsize = (7,5))

data = pd.Series(np.random.rand(16))
index = list('abcdefghijklmnop')

ax1 = axes[0].bar(data.index, data, color = 'k', alpha =0.1)
ax2 = axes[1].barh(data.index, data, color = 'g', alpha =1)
plt.show()


###ax.plot
fig = plt.figure(figsize = (10,5))

ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())

ax.set_xticks([0,250,500, 750,1000])  #눈금수정
ax.set_xticklabels(['하나','둘','셋','넷','다섯'], rotation = 35) #문자열로 눈금수정

ax.set_title('고민표')
ax.set_xlabel('ㅋㅋ      ' )
ax.set_ylabel('y축')
plt.show()



#한 부분에 여러 그래프 그리기
fig = plt.figure(figsize = (13,4))

ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(), 'k', label = '첫번째라인')
ax.plot(np.random.randn(1000).cumsum(), 'b--', label = '두번째 라인')
ax.plot(np.random.randn(1000).cumsum(), 'r--', label = '세번째 라인')
ax.legend(loc = 'best') #범례 loc는 범례의 위치임 기본값으로는 best로, 빈공간을 알아서 찾아감.(upper left, lower right)
plt.show()


fig, ax = plt.subplots(1,1)
ax.plot(np.random.randn(100).cumsum(), 'y', label='고민표')
ax.plot(np.random.randn(100).cumsum(), 'c--', label= '한')
ax.plot(np.random.randn(100).cumsum(), 'm.-', label= '둘')
ax.legend()
plt.show()





#####예제
data = {
    '영화':['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '어벤져스 엔드게임', '겨울왕국','베테랑','아바타', '도둑들','7번방의 선물'],
    '개봉연도': [2014, 2019, 2021, 2014, 2019,2019, 2015, 2018, 2012, 2013],
    '관객 수':[1761, 1626, 1441, 1426, 1397, 1374,1341, 1338, 1298, 1281],
    '평점':[7.8, 7.4, 7.1, 7.1, 7.9, 7.3, 8.4, 9.0, 7.9, 8.7]

}

df =pd.DataFrame(data)

#영화, 평점 막대그래프
#plt.bar
plt.figure(figsize=(10,8))
plt.bar(df['영화'], df['평점'])
plt.xticks(rotation = 45)
plt.title('역대관객순위 TOP10')
plt.xlabel('영화')
plt.ylabel('평점')
plt.show()
#ax.bar    ax는 여러개 쓰는 용도임 따라서 ax에서 plt만 바꾸면 되고 작동방식은 같음.
fig, ax =plt.subplots(1,1)
ax.bar(df['영화'], df['평점'])
plt.xticks(rotation = 90)
plt.show()
#pandas의 모듈인 데이터.plot(kind='bar')
df.plot('영화', '평점', kind = 'bar')

plt.show()




#연도별 평점 추이
df2 = df.loc[:,('개봉연도', '평점') ]  #계산을 수월하게 하기 위해서 해당 데이터만 뽑아내고
df_ko = df2.groupby('개봉연도').mean()  #groupby( unique로 구분된 요소들)로 각각 평균을 구하고
df_ko.plot()  #변수가 두개이므로 바로 .plot()으로 구하고
plt.show()

df_ko = df.groupby('개봉연도')['평점'].mean()  
#뒤에 인덱싱으로 해당 열만 선택하게 할 수 있음.



#평점 8점이상 pie plot
#방법 1
condition1 = df['평점'] >= 8

up = len(df[condition1])
down = len(df[~condition1])   #  ~는 not condition임 
up1=up/(up+down)
down1 = down/(up+down)
plt.pie([up1,down1], labels = ['8점이상', '8점이하'], autopct= '%.1f%%')
plt.legend(loc = 'upper left')
plt.show()  


#방법2
df['ratio'] = df['평점']>=8
df['ratio'][df['ratio']==True] = 1       
#열인 df['ratio']중에서  행의 값이 True인 것은 1로 바꿔라 [열][행] 임
df['ratio'][df['ratio']==False] = 0
df['ratio']

label= ['8점이상', '8점이하']

value = [df['ratio'].mean(), 1-df['ratio'].mean()]

plt.pie(value, labels= label, autopct = '%.1f%%')
plt.legend(loc = 'right')
plt.show()





