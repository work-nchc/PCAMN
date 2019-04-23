from time import time
start = int(input('start: '))
t = time()

if start <= 0:
    print('0: vox')
    import vox
    del vox
if start <= 1:
    print('1: mn')
    import mn
    del mn

if start <= 2:
    print('2: pcamn')
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
        save(temp_out, Parallel(-1, verbose=1, temp_folder='cache')(
            delayed(log_var)(vox[n]) for n in knn))
        return None

    export_pca('vox1.ply', '128_1.npy', 'pca_1')
    export_pca('vox2.ply', '128_2.npy', 'pca_2')
    export_pca('vox4.ply', '128_4.npy', 'pca_4')

if start <= 3:
    print('3: concat')
    import concat
    del concat
if start <= 4:
    print('4: propagate')
    import propagate
    del propagate
if start <= 5:
    print('5: test')
    import test
    del test
if start <= 6:
    print('6: vis')
    import vis
    del vis
if start <= 7:
    print('7: treetop')
    import treetop
    del treetop

with open('time.txt', 'w') as w:
    w.write(str(time() - t) + ' sec\n')
