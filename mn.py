from numpy import save
from sklearn.neighbors import NearestNeighbors
from open3d import read_point_cloud

k = 128
neigh = NearestNeighbors(k, n_jobs=-1)

vox = read_point_cloud('vox1.ply')
neigh.fit(vox.points)
knn = neigh.kneighbors(return_distance=False)
save('{}_1'.format(k), knn)

vox = read_point_cloud('vox2.ply')
neigh.fit(vox.points)
knn = neigh.kneighbors(return_distance=False)
save('{}_2'.format(k), knn)

vox = read_point_cloud('vox4.ply')
neigh.fit(vox.points)
knn = neigh.kneighbors(return_distance=False)
save('{}_4'.format(k), knn)
