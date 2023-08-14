import cv2
import glob
import argparse

def parse_args():
    """ Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Deep SORT")
    parser.add_argument(
        "--sequence_dir", help="Path to MOTChallenge sequence directory",
        default=None, required=True)

    return parser.parse_args()

args = parse_args()


for filename in glob.glob(f"{args.sequence_dir}/img1/*.jpg"):
    img = cv2.imread(filename)
    frameSize = (img.shape[1], img.shape[0])
    break


#use 15 fps rate

filename = args.sequence_dir.split("/")[-1]

output_file = f"videos/{filename}.mp4"

out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'MP4V'), 24, frameSize)

for filename in glob.glob(f"{args.sequence_dir}/img1/*.jpg"):
    img = cv2.imread(filename)
    out.write(img)

out.release()