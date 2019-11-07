from os import chdir
chdir('N:/PATH/TO/WORKING/DIR')
n_jobs = 8

from subprocess import run
from sys import executable

run((executable, 'vox.py'))
run((executable, 'mn.py'))

from numpy import log2, array, load, save
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud

def log_var(pts):
    pca = PCA()
    pca.fit(pts)
    pca.explained_variance_[:-1] -= pca.explained_variance_[1:]
    return log2(pca.explained_variance_)

def export_pca(ply_vox, npy_knn, temp_out):
    vox = array(read_point_cloud(ply_vox).points)
    knn = load(npy_knn)
    save(temp_out, Parallel(int(n_jobs), verbose=1)(
        delayed(log_var)(vox[n]) for n in knn))
    return None

export_pca('vox1.ply', '128_1.npy', 'pca_1')
export_pca('vox2.ply', '128_2.npy', 'pca_2')
export_pca('vox4.ply', '128_4.npy', 'pca_4')

run((executable, 'concat.py'))
run((executable, 'propagate.py'))
run((executable, 'test.py'))
run((executable, 'vis.py'))
run((executable, 'treetop.py'))
