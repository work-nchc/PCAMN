from time import time
begin = int(input('begin: '))
end = int(input('end: '))
n_jobs = input('n_jobs: ')
if not n_jobs:
    n_jobs = 8
t = time()

if begin <= 0 <= end:
    print('0: vox')
    import vox
    del vox
if begin <= 1 <= end:
    print('1: mn')
    import mn
    del mn

if begin <= 2 <= end:
    print('2: pcamn')
    from numpy import log2, array, load, save
    from sklearn.decomposition import PCA
    from joblib import Parallel, delayed
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

if begin <= 3 <= end:
    print('3: concat')
    import concat
    del concat
if begin <= 4 <= end:
    print('4: propagate')
    import propagate
    del propagate
if begin <= 5 <= end:
    print('5: test')
    import test
    del test
if begin <= 6 <= end:
    print('6: vis')
    import vis
    del vis
if begin <= 7 <= end:
    print('7: treetop')
    import treetop
    del treetop

with open('time.txt', 'w') as w:
    w.write(str(time() - t) + ' sec\n')
