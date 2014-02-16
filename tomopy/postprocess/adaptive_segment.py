# -*- coding: utf-8 -*-
import numpy as np
from skimage.filter import threshold_otsu, threshold_adaptive
from tomopy.tools.multiprocess import worker


@worker
def adaptive_segment(args):
    """
    Adaptive thresholding based segmentation.
    """
    data, args, ind_start, ind_end = args
    block_size, offset = args
    
    for m in range(ind_end-ind_start):
        img = data[m, :, :]
        global_thresh = threshold_otsu(img)
        binary_global = img > global_thresh

        img = threshold_adaptive(img, block_size=block_size, offset=offset)
        data[m, :, :] = img
    return ind_start, ind_end, data