# PCAMN
Principal Component Analysis of Multiscale Neighbourhood

Tested in Python 3.6

---
```
PATH/TO/python.exe pcamn.py
```

Enter the numbers of [begin], [end], and [n_jobs] (default = 8).  Lidar cloud should be named as test.ply.  Photogrammetry cloud used for colour correction should be named as photo_test.ply.  time.txt records the execution time.

Execution steps:

0: vox  
output: vox1.ply, vox2.ply, vox4.ply

1: mn  
output: 128_1.npy, 128_2.npy, 128_4.npy

2: pcamn  
output: pca_1.npy, pca_2.npy, pca_4.npy

3: concat  
output: pca.npy

4: propagate  
output: pca_all.npy

5: test  
output: tree.ply

6: vis  
output: vis.ply

7: treetop  
output: corr.ply

---
2019-05-08 by 1803031@narlabs.org.tw
