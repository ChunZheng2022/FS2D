import torch

from .vfe_template import VFETemplate


class MeanVFEMeta(VFETemplate):
    def __init__(self, model_cfg, num_point_features, **kwargs):
        super().__init__(model_cfg=model_cfg)
        self.num_point_features = num_point_features
        if self.training:
            self.meta_n = self.model_cfg.META_N
            self.meta_k = self.model_cfg.META_K

    def get_output_feature_dim(self):
        return self.num_point_features

    def forward(self, batch_dict, **kwargs):
        """
        Args:
            batch_dict:
                voxels: (num_voxels, max_points_per_voxel, C)
                voxel_num_points: optional (num_voxels)
            **kwargs:

        Returns:
            vfe_features: (num_voxels, C)
        """
        voxel_features, voxel_num_points = batch_dict['voxels'], batch_dict['voxel_num_points']
        points_mean = voxel_features[:, :, :].sum(dim=1, keepdim=False)
        normalizer = torch.clamp_min(voxel_num_points.view(-1, 1), min=1.0).type_as(voxel_features)
        points_mean = points_mean / normalizer
        batch_dict['voxel_features'] = points_mean.contiguous()

        if self.training:
            for i in range(self.meta_n):
                for j in range(self.meta_k):
                    num_cls = str(i)
                    num_shot = str(j)
                    voxel_features, voxel_num_points = (
                        batch_dict['voxels_meta'+num_cls+num_shot], batch_dict['voxel_num_points_meta'+num_cls+num_shot])
                    points_mean = voxel_features[:, :, :].sum(dim=1, keepdim=False)
                    normalizer = torch.clamp_min(voxel_num_points.view(-1, 1), min=1.0).type_as(voxel_features)
                    points_mean = points_mean / normalizer
                    batch_dict['voxel_features_meta'+num_cls+num_shot] = points_mean.contiguous()

        return batch_dict
