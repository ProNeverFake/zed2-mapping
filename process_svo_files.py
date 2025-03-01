from zed_mapping.mapping import process_video_file
import os
from pathlib import Path
import time
import argparse

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Process ZED SVO files, ")
    # parser.add_argument('--data_path', help='Path to directory containing multiple .svo files to process')
    # args = parser.parse_args()
    # directory = Path(args.data_path)
    directory = os.path.dirname(os.path.realpath(__file__))
    # directory = os.path.join(current_dir, "svo_file.svo2")
    for fname in os.listdir(directory):
        p = Path(fname)
        if not p.suffix == '.svo':
            print("Skipping non-svo file %s" % p)
            continue

        print("Processing %s" % p)
        svo_file = directory / p

        # trim the HD720_SN... part from the filename, for the output directory
        if fname.startswith("HD720"):
            output_name = p.stem.split('_')[-1]
        else:
            output_name = p.stem
        output_directory = os.path.join(directory, output_name)
        start_time = time.time()
        process_video_file(svo_file, output_directory, verbose=True)
        print("Finished, runtime was %.2f" % (time.time() - start_time))