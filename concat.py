from numpy import load, save, zeros, nan_to_num
from sklearn.neighbors import KNeighborsRegressor
from open3d import read_point_cloud

vox1 = read_point_cloud('vox1.ply')
neigh = KNeighborsRegressor(1, n_jobs=-1)

pca = nan_to_num(load('pca_1.npy'))
pca_concat = zeros((len(pca), 9))
pca_concat[:,:3] = pca

vox = read_point_cloud('vox2.ply')
pca = nan_to_num(load('pca_2.npy'))
neigh.fit(vox.points, pca)
pca_concat[:,3:6] = neigh.predict(vox1.points)

vox = read_point_cloud('vox4.ply')
pca = nan_to_num(load('pca_4.npy'))
neigh.fit(vox.points, pca)
pca_concat[:,6:] = neigh.predict(vox1.points)

save('pca', pca_concat)
