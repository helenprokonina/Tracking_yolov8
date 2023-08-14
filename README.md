# Tracking_yolov8

First **make_video_from_frames.py** creates videos from images in the MOT20-04 (any of them) directory.

```
python make_video_from_frames.py --sequence_dir MOT20/test/MOT20-04
```

Then in **main.py** DeepSORT algorithm with YOLOv8 for detections is performed. 

```
python main.py --video_path MOT20-04.mp4
```

The result video with tracking will be saved as outs/MOT20-04.mp4 file.

Resulting videos are available via link: https://drive.google.com/drive/folders/1-tio25jy6FH8ZH5Qeeks7YPiX2tqjI-E?usp=sharing
