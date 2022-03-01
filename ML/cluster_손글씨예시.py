
# K-Means Clustering 연습
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 시험용 데이터 세트를 구성한다
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)

print(X[:10, :])

# 시험용 데이터를 2차원 좌표에 표시한다
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], marker='o', s=100, alpha=0.5)
plt.grid()
plt.show()

# K-means 알고리즘으로 시험용 데이터를 3 그룹으로 분류한다 (k = 3)
# n_init = 10 (default) : Local min에 빠지는 것을 완화함.
# 초기 중심을 다르게 설정하여 (100번) error가 작은 값을 최종 학습 결과로 선택한다.
#클러스트 갯수, 클러스터 랜덤, 클러스터 지정랜덤 시행횟수, k-means과정 실행횟수, 새로운 오차간의 차이 제한,       
#local optimization을 좀더 방지하기 위해서 init = 'k-means++'로 초기중점을 좀더 멀리떨어지게 한다.
#k-means++가 default값임.
km = KMeans(n_clusters=3, init='random', n_init=100, max_iter=300, tol=1e-04, random_state=0)
km = km.fit(X)
y_km = km.predict(X)

# 분류 결과를 표시한다
plt.figure(figsize=(8, 6))
plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1], s=100, c='green', marker='s', alpha=0.5, label='cluster 1')
plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1], s=100,  c='orange', marker='o', alpha=0.5, label='cluster 2')
plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1], s=100, c='blue', marker='v', alpha=0.5, label='cluster 3')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s=250, marker='+', c='red', label='centroids')
plt.legend()
plt.grid()
plt.show()


# K-Means Clustering : Elbow에 의한 최적 cluster 개수
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 시험용 데이터 세트를 구성한다
X, y = make_blobs(n_samples=300, n_features=2, centers=5, cluster_std=1.4, shuffle=True, random_state=10)

# 시험용 데이터를 2차원 좌표에 표시한다
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], marker='o', s=100, alpha=0.5)
plt.grid()
plt.show()

# 엘보우 (elbow) 방법으로 최적 cluster 개수를 찾아본다.
distortions = []
for i in range(2, 11):
    km = KMeans(n_clusters=i, init='random', n_init=100, max_iter=300,tol=1e-04)
    km = km.fit(X)
    
    # Cluster내의 SSE를 계산한다.
    # 관성 (inertia), 혹은 왜곡 (distortion)이라고도 한다.
    distortions.append(km.inertia_)
    
plt.plot(range(2, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()



# K-Means Clustering : Silrouette 계수 확인(클스록 좋은것)
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

# 시험용 데이터 세트를 구성한다
X, y = make_blobs(n_samples=300, n_features=2, centers=5, cluster_std=1.4, shuffle=True, random_state=10)

# 시험용 데이터를 2차원 좌표에 표시한다
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], marker='o', s=100, alpha=0.5)
plt.grid()
plt.show()

silhouette_list = []
for n in range(2, 10):
    # K-means 알고리즘으로 시험용 데이터를 3 그룹으로 분류한다 (k = 3)
    km = KMeans(n_clusters=n, init='random', n_init=100, max_iter=300, tol=1e-04, random_state=0)
    km = km.fit(X)
    y_km = km.predict(X)

    vals = silhouette_samples(X, y_km, metric='euclidean')
    mean_vals = silhouette_score(X, y_km, metric='euclidean')     # np.mean(vals)
    silhouette_list.append(mean_vals)
    print('n_cluster = {}, 실루엣 스코어 = {:.3f}'.format(n, mean_vals))

plt.plot(range(2, 10), silhouette_list, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('silhouette_score')
plt.show()




#H-clustering(hierarchical Agglomerative cluster)
#그룹을 나눈후에 cluster 결정  앞에서는 cluster수를 정하고 나누었음. 
#자르는 기준은 앞에서 실루엣 평가모형을 기준으로 하면 될듯.
#모든 자료의 거리를 구하고 제일 가까운 거리를 묶고 그 묶은 클러스터의 평균을 구하고
#그 평균에서 다시(자료의 개수를 줄어듬) 모든 자료의 거리구하고 가까운거 묶고.. 반복
# H-Clustering 연습
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import numpy as np

# 시험용 데이터 세트를 구성한다
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)

# 시험용 데이터를 2차원 좌표에 표시한다
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], marker='o', s=100, alpha=0.5)
plt.grid()
plt.show()

# linkage를 계산한다.
mergings = linkage(X, method='complete')

# Dendrogram을 그린다.
plt.figure(figsize=(8,6))
dendrogram(mergings)
plt.show()

# 분류 결과를 표시한다
y_clust = fcluster(Z=mergings, t=3, criterion='distance')

# 중점의 좌표를 계산한다.
c1 = np.mean(X[y_clust == 1], axis=0)
c2 = np.mean(X[y_clust == 2], axis=0)
c3 = np.mean(X[y_clust == 3], axis=0)
centroid = np.vstack([c1, c2, c3])

plt.figure(figsize=(8, 6))
plt.scatter(X[y_clust == 1, 0], X[y_clust == 1, 1], s=100, c='green', marker='s', alpha=0.5, label='cluster 1')
plt.scatter(X[y_clust == 2, 0], X[y_clust == 2, 1], s=100, c='orange', marker='o', alpha=0.5, label='cluster 2')
plt.scatter(X[y_clust == 3, 0], X[y_clust == 3, 1], s=100, c='blue', marker='v', alpha=0.5, label='cluster 3')
plt.scatter(centroid[:,0], centroid[:,1], s=250, marker='+', c='red', label='centroids')
plt.legend()
plt.grid()
plt.show()


#위 두개의 군집분석은 거리 기반이기 때문에 서로 옹졸하게 모인 형태에서만 성능을 발휘함.


#DBSCAN
#하나의 자료를 가지고 원 반경의 min-points(3이라고 가정)이상이면 
# 그 것을 core point(핵심샘플)라고 한다.
#그 core points를 다 모아서 연결하면 그 집합이 하나의 클러스터가 된다.
#파라미터는 원반경, min-points



# DBSCAN을 사용하여 밀집도가 높은 지역 찾기
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
print(X[:10, :])

plt.scatter(X[:, 0], X[:, 1])
plt.tight_layout()
plt.show()

# K-Means
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))

km = KMeans(n_clusters=2, random_state=0)
y_km = km.fit_predict(X)
ax1.scatter(X[y_km == 0, 0], X[y_km == 0, 1],
            edgecolor='black',
            c='lightblue', marker='o', s=40, label='cluster 1')
ax1.scatter(X[y_km == 1, 0], X[y_km == 1, 1],
            edgecolor='black',
            c='red', marker='s', s=40, label='cluster 2')
ax1.set_title('K-means clustering')

# 계층 군집
ac = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='complete')
y_ac = ac.fit_predict(X)

ax2.scatter(X[y_ac == 0, 0], X[y_ac == 0, 1], c='lightblue', edgecolor='black', marker='o', s=40, label='cluster 1')
ax2.scatter(X[y_ac == 1, 0], X[y_ac == 1, 1], c='red', edgecolor='black', marker='s', s=40, label='cluster 2')
ax2.set_title('Agglomerative clustering')

plt.legend()
plt.tight_layout()
plt.show()

# DBSCAN
db = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
y_db = db.fit_predict(X)

plt.scatter(X[y_db == 0, 0], X[y_db == 0, 1], c='lightblue', marker='o', s=40, edgecolor='black', label='cluster 1')
plt.scatter(X[y_db == 1, 0], X[y_db == 1, 1], c='red', marker='s', s=40, edgecolor='black', label='cluster 2')
plt.legend()
plt.tight_layout()
plt.show()




#mean_shift 
#자료의 최빈값을 클러스터 중심으로 정하는 것

# 코드 출처 : 파이썬 머신러닝 완벽 가이드 (위키북스, 2020)
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
from sklearn.cluster import estimate_bandwidth
import matplotlib.pyplot as plt

# 클러스터링 테스트를 위한 임의 데이터를 생성한다.
X, y = make_blobs(n_samples=200, n_features=2, centers=3, cluster_std=0.8, random_state=0)

# 데이터 시각화
plt.scatter(X[:, 0], X[:, 1])
plt.show()

clusterDF = pd.DataFrame(data=X, columns=['ftr1', 'ftr2'])
clusterDF['target'] = y

# estimate_bandwidth()로 최적의 bandwidth 계산
best_bandwidth = estimate_bandwidth(X, quantile=0.2)

# Mean Shift Clustering
meanshift= MeanShift(bandwidth=1)
cluster_labels = meanshift.fit_predict(X)
print('cluster labels 유형:', np.unique(cluster_labels))

clusterDF['meanshift_label']  = cluster_labels
centers = meanshift.cluster_centers_
unique_labels = np.unique(cluster_labels)
markers=['o', 's', '^', 'x', '*']

for label in unique_labels:
    label_cluster = clusterDF[clusterDF['meanshift_label']==label]
    center_x_y = centers[label]

    # 군집별로 다른 marker로 scatter plot 적용
    plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], marker=markers[label] )
    
    # 군집별 중심 시각화
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=200, color='white', edgecolor='k', alpha=0.9, marker=markers[label])
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k', marker='$%d$' % label)
    
plt.show()

best_bandwidth




##GMM(Gaussian Mixture Model)
#비모수적으로 분포를 추정(이때 분포는 빈도수를 가지고 파악하는 KDE방법)



from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# make_blobs() 로 300개의 데이터 셋, 3개의 cluster 셋, cluster_std=0.5 을 만듬. 
X, y = make_blobs(n_samples=300, n_features=2, centers=3, cluster_std=0.5, random_state=0)

# 길게 늘어난 타원형의 데이터 셋을 생성하기 위해 변환함. 
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)

# feature 데이터 셋과 make_blobs( ) 의 y 결과 값을 DataFrame으로 저장
clusterDF = pd.DataFrame(data=X_aniso, columns=['ftr1', 'ftr2'])
clusterDF['target'] = y

# 데이터 시각화
plt.scatter(clusterDF['ftr1'], clusterDF['ftr2'])
plt.show()

# 클러스터 결과를 담은 DataFrame과 사이킷런의 Cluster 객체등을 인자로 받아 클러스터링 결과를 시각화하는 함수  
def visualize_cluster_plot(clusterobj, dataframe, label_name, iscenter=True):
    if iscenter :
        centers = clusterobj.cluster_centers_
        
    unique_labels = np.unique(dataframe[label_name].values)
    markers=['o', 's', '^', 'x', '*']

    for label in unique_labels:
        label_cluster = dataframe[dataframe[label_name]==label]
        cluster_legend = 'Cluster ' + str(label)
        
        plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], s=70, marker=markers[label], label=cluster_legend)
        
        if iscenter:
            center_x_y = centers[label]
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=250, color='white', alpha=0.9, edgecolor='k', marker=markers[label])
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k', marker='$%d$' % label)
    
    legend_loc='upper right'
    plt.legend(loc=legend_loc)
    plt.show()

# KMeans clustering
kmeans = KMeans(3, random_state=0)
kmeans_label = kmeans.fit_predict(X_aniso)
clusterDF['kmeans_label'] = kmeans_label

visualize_cluster_plot(kmeans, clusterDF, 'kmeans_label',iscenter=True)

# GMM clustering
gmm = GaussianMixture(n_components=3, random_state=0).fit(X_aniso)
gmm_cluster_labels = gmm.predict(X_aniso)
clusterDF['gmm_cluster'] = gmm_cluster_labels

visualize_cluster_plot(None, clusterDF, 'target', iscenter=False)

p = gmm.predict_proba(X_aniso)
cluster = np.argmax(p, axis=1)
(gmm_cluster_labels != cluster).sum()


##위의 알고리즘들은 빈도수를 기반으로 추정하므로 주변의 빈도수에
#영향을 받을 자료에 성능이 나올 듯.



import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt

DATA_PATH = 'C:/Users/user/Desktop/git/TIL/ML/'
#구글드라이버에 상세한 설명있음(다운로드방법)
# 저장된 mnist 데이터를 읽어온다.
with open(DATA_PATH + 'mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)

print(mnist.keys())

type(mnist['data'])

# 데이터가 많아 시간이 오래걸리므로, 앞 부분 10000개만 분석한다.
x_feat = np.array(mnist['data'][:1000])
y_target = np.array(mnist['target'][:1000])

# n-번째 손글씨 이미지를 확인해 본다.
n = 0
img = x_feat[n].reshape(28,28)
print('\nclass =', y_target[n])
plt.imshow(img)
plt.show()
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size = 0.2)
#######DBSCAN
from sklearn.cluster import DBSCAN

# DBSCAN
db = DBSCAN(eps=0.4, min_samples=4, metric='euclidean')
y_pred=db.fit_predict(x_train)
y_pred
n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(12,4))
for i, miss in enumerate(miss_sam):
    # x = x_test[miss] * 255  # 표준화 단계에서 255로 나누었으므로, 여기서는 곱해준다.
    x = x.reshape(28, 28)   # 이미지 확인을 위해 (28 x 28) 형태로 변환한다.
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_train[miss]) + ' / ' + str(y_pred[miss]))

