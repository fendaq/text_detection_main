from lib.utils.cython_nms import nms as cython_nms
def nms(dets, thresh):
    if dets.shape[0] == 0:
        return []
    #if cfg.USE_GPU_NMS:
    #   return gpu_nms(dets, thresh, device_id=cfg.GPU_ID)
    else:
        return cython_nms(dets, thresh)
