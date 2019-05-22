from open3d import read_point_cloud, write_point_cloud, Vector3dVector
import joblib
from numpy import load, zeros
from scipy.special import erf

scaler = joblib.load('scaler.joblib')
svc = joblib.load('svc.joblib')
proj = joblib.load('proj.joblib')

pts = read_point_cloud('test.ply')
pcamn = load('pca_all.npy')
color = zeros((len(pcamn), 3))

pcamn = scaler.transform(pcamn)
color[:,0] = svc.decision_function(pcamn)

pcamn -= svc.coef_ * svc.coef_.dot(pcamn.T).T / (svc.coef_ ** 2).sum()
color[:,1:] = proj.transform(pcamn)

pts.colors = Vector3dVector((1.0 + erf(color / 2.0 ** 0.5)) / 2.0)
write_point_cloud('vis.ply', pts)
