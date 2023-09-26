import json
from PIL import Image
import glob
import random

def load_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def laod_images(file):
    image_list = []
    for filename in glob.glob(f'{file}*.jpg'):
        im = Image.open(filename)
        image_list.append(im)

    return image_list


def get_data():
    captions = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/captions_val2017.json')
    instances = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/instances_val2017.json')
    person_keypoints = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/person_keypoints_val2017.json')
    images = laod_images('../../../groups/course.cap6411/Dataset/coco/val2017/*.jpg')

    return captions, instances, person_keypoints, images


captions, instances, person_keypoints, images = get_data()

# save one random image
random_image = random.randint(0, len(images))
images[random_image].save('random_image.jpg')

# for i in captions['annotations']:
#     print(i['caption'])
#
# print('=' * 100)
#
# for i in instances['annotations']:
#     print(i['category_id'])
#
# print('=' * 100)
#
# for i in person_keypoints['annotations']:
#     print(i['keypoints'])


