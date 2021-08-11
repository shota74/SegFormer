from .builder import DATASETS
from .custom import CustomDataset
from IPython import embed

@DATASETS.register_module()
class SIPDataset(CustomDataset):
    """Mapillary dataset.
    """
    CLASSES = ('road', 'Sidewalk', 'white_line', 'vegetation', 'car', 'person',
               'pole', 'Traffic Sign', 'Traffic Light', 'background')

    PALETTE = [[128, 64, 128],
            [244,35,232],
            [255,0,0],
            [107,142,35],
            [0,0,142],
            [220,20,60],
            [153,153,153],
            [220,220,0],
            [250,170,30],
            [255,255,255]]



    def __init__(self, **kwargs):
        super(SIPDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)