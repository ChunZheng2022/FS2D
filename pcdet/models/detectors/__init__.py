from .detector3d_template import Detector3DTemplate
from .voxelnext import VoxelNeXt
from .fs2d import FS2D

__all__ = {
    'Detector3DTemplate': Detector3DTemplate,
    'VoxelNeXt': VoxelNeXt,
    'FS2D': FS2D,
}


def build_detector(model_cfg, num_class, dataset):
    model = __all__[model_cfg.NAME](
        model_cfg=model_cfg, num_class=num_class, dataset=dataset
    )

    return model
