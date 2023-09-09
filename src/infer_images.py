import glob
from tqdm import tqdm
import os
import shutil

root_folders = "/home/luantranthanh/hust/ocr/dataset/new_public_test"
output_folders = "denoised_imgs"
shutil.rmtree(output_folders, ignore_errors=True)
os.makedirs(output_folders)
image_paths = glob.glob(root_folders + "/*")
total_failed = 0
# for img_path in tqdm(image_paths):
#     img_name = img_path.split('/')[-1]
#     output_path = os.path.join(output_folders, img_name)
#     try:
#         os.system(f"./imgtxtenh {img_path} {output_path}")
#     except:
#         print(img_path)
#         total_failed += 1
#         os.system(f"scp {img_path} {output_path}")
# print(total_failed)
# write above procedure in parralel
import multiprocessing
from multiprocessing import Pool


def process_image(img_path):
    img_name = img_path.split("/")[-1]
    output_path = os.path.join(output_folders, img_name)
    try:
        os.system(f"./imgtxtenh {img_path} {output_path}")
    except:
        print(img_path)
        total_failed += 1
        os.system(f"scp {img_path} {output_path}")
    return 0


if __name__ == "__main__":
    pool = Pool(8)
    pool.map(process_image, image_paths)
    pool.close()
    pool.join()
