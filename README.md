# FS2D
 This is the official implementation of FS2D

This code is built upon [`OpenPCDet`](https://github.com/open-mmlab/OpenPCDet) and [`VoxelNeXt`](https://github.com/dvlab-research/VoxelNeXt/tree/master).
You can refer to the [`Install`](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/INSTALL.md) and [`Getting Started`](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/GETTING_STARTED.md) to prepare the training environment.

## Getting Started
1. Training.

    ```
    cd FS2D/tools
    python train.py --cfg_file cfgs/kitti_models/sgf.yaml
    ```

2. Evaluation.

    ```
    cd SGF3D/tools
    python test.py --cfg_file cfgs/kitti_models/sgf.yaml --ckpt checkpoint_epoch_66.pth
    ```

3. Visualization.

   You can refer to [3D-Detection-Tracking-Viewer](https://github.com/hailanyi/3D-Detection-Tracking-Viewer) or [3d-object-vis](https://github.com/DeclK/3d-object-vis) for visualization. Both of these visualization tools are based on [vedo](https://github.com/marcomusy/vedo).
You can also use Open3D or mayavi for visualization.