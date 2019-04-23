from open3d import read_point_cloud
from sklearn.neighbors import KNeighborsRegressor
from numpy import load, save

origin = read_point_cloud('test.ply')
vox = read_point_cloud('vox1.ply')
pca = load('pca.npy')

neigh = KNeighborsRegressor(1, n_jobs=-1)
neigh.fit(vox.points, pca)
pca_all = neigh.predict(origin.points)

save('pca_all', pca_all)
