# FS<sup>2</sup>D: Fully Sparse Few-Shot 3D Object Detection
 This is the official implementation of FS2D

This code is built upon [`OpenPCDet`](https://github.com/open-mmlab/OpenPCDet) and [`VoxelNeXt`](https://github.com/dvlab-research/VoxelNeXt/tree/master).
You can refer to the [`Install`](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/INSTALL.md) and [`Getting Started`](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/GETTING_STARTED.md) to prepare the training environment.

* Please download the official [NuScenes 3D object detection dataset](https://www.nuscenes.org/download) and 
organize the downloaded files as follows: 
```
FS2D
├── data
│   ├── nuscenes
│   │   │── v1.0-trainval 
│   │   │   │── samples
│   │   │   │── sweeps
│   │   │   │── maps
│   │   │   │── v1.0-trainval  
├── pcdet
├── tools
```

* Install the `nuscenes-devkit` with version `1.0.5` by running the following command: 
```shell script
pip install nuscenes-devkit==1.0.5
```

* Generate the data infos by running the following command (it may take several hours): 
```python 
# for lidar-only setting
python -m pcdet.datasets.nuscenes.nuscenes_dataset --func create_nuscenes_infos \
    --cfg_file tools/cfgs/dataset_configs/nuscenes_dataset.yaml \
    --version v1.0-trainval
```

## Getting Started
1. Training.

    ```
    cd FS2D/tools
    python train_meta.py --cfg_file cfgs/nuscenes_models/fs2d.yaml
    ```

2. Evaluation.

    ```
    cd SGF3D/tools
    python test.py --cfg_file cfgs/nuscenes_models/fs2d.yaml --ckpt checkpoint_epoch_XX.pth
    ```

3. Visualization.

   You can refer to [3D-Detection-Tracking-Viewer](https://github.com/hailanyi/3D-Detection-Tracking-Viewer) or [3d-object-vis](https://github.com/DeclK/3d-object-vis) for visualization. Both of these visualization tools are based on [vedo](https://github.com/marcomusy/vedo).
You can also use Open3D or mayavi for visualization.