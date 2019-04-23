from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
from numpy import array, concatenate

cloud = read_point_cloud('tree.ply')
calibrate = read_point_cloud('photo_test.ply')

neigh0 = KNeighborsRegressor(4, 'distance', n_jobs=-1)
neigh0.fit(calibrate.points, calibrate.colors)

arr_points = array(cloud.points)
arr_colors = array(cloud.colors)
arr_filter = array(cloud.normals)[:,0] * (arr_colors[:,2] > 0.5)
points_other = arr_points.compress(True - arr_filter, 0)
colors_other = arr_colors.compress(True - arr_filter, 0)

neigh1 = KNeighborsRegressor(1, n_jobs=-1)
neigh1.fit(points_other, colors_other)

points_abn = arr_points.compress(arr_filter, 0)
colors_abn = (neigh0.predict(points_abn) + neigh1.predict(points_abn)) / 2
cloud.points = Vector3dVector(concatenate((points_other, points_abn)))
cloud.colors = Vector3dVector(concatenate((colors_other, colors_abn)))
cloud.normals = Vector3dVector()
write_point_cloud('corr.ply', cloud)
