from open3d import read_point_cloud, write_point_cloud, voxel_down_sample
cloud = read_point_cloud('test.ply')
vox = voxel_down_sample(cloud, 0.01)
write_point_cloud('vox1.ply', vox)
vox = voxel_down_sample(cloud, 0.02)
write_point_cloud('vox2.ply', vox)
vox = voxel_down_sample(cloud, 0.04)
write_point_cloud('vox4.ply', vox)
