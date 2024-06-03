## Sensor Fusion: Camera, Lidar and Bus Data

The Sensor Fusion subset contains three recorded sequences in three
locations in Germany:

Gaimersheim
Munich
Ingolstadt

Each sequence has data from camera, LiDAR, and the vehicle bus. In total
there are 392,556 frames. This data is not annotated.

Each frame contains the following items:

- RGB image
- registration info file
- 3D point cloud

Frames are grouped in three different scenes, with each scene in a
separate directory. Scene directory names denote the time and date of
the recording in 'YYYYMMDD_hhmmss' format. Each scene is further divided
into two subdirectories:

- 'camera': images and json info files
- 'lidar': 3D point clouds

Each of these directories contains further subdirectories for each
camera. There are six cameras available in the vehicle, corresponding
to the following subdirectories:

- 'cam_front_center'
- 'cam_front_left'
- 'cam_front_right'
- 'cam_side_left'
- 'cam_side_right'
- 'cam_rear_center'

These are the filename formats for the items of a single sample:

- RGB image         : YYMMDDDDhhmmss_camera_[frontcenter|frontleft|frontright|sideleft|sideright|rearcenter]_[ID].png
- registration info : YYMMDDDDhhmmss_camera_[frontcenter|frontleft|frontright|sideleft|sideright|rearcenter]_[ID].json
- LiDAR point cloud : YYMMDDDDhhmmss_lidar_[frontcenter|frontleft|frontright|sideleft|sideright|rearcenter]_[ID].npz

For example a sample with ID 1617 from a scene recorded on 2018-08-07
14:50:28 from the front center camera would have the following items in
these locations:

- input RGB image   : 20180807_145028/camera/cam_front_center/20180807145028_camera_frontcenter_000001617.png
- input info        : 20180807_145028/camera/cam_front_center/20180807145028_camera_frontcenter_000001617.json
- LiDAR point cloud : 20180807_145028/lidar/cam_front_center/20180807145028_lidar_frontcenter_000001617.npz

For further explanations regarding the format of each of these items,
please refer to the tutorial on the A2D2 web page.
