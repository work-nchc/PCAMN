from numpy import load, zeros
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.externals import joblib

scaler = joblib.load('scaler.joblib')
svc = joblib.load('svc.joblib')

pca = load('pca_all.npy')
norms = zeros((len(pca), 3))
norms[:,0] = svc.predict(scaler.transform(pca))
cloud = read_point_cloud('test.ply')
cloud.normals = Vector3dVector(norms)
write_point_cloud('tree.ply', cloud)
