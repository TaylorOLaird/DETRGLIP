import json
from PIL import Image
import glob

def load_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def laod_image(file):
    image_list = []
    for filename in glob.glob(f'{file}*.jpg'):
        im = Image.open(filename)
        image_list.append(im)


def get_data():
    captions = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/captions_val2017.json')
    instances = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/instances_val2017.json')
    person_keypoints = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/person_keypoints_val2017.json')
    images = laod_image('../../../groups/course.cap6411/Dataset/coco/val2017/*.jpg')

    return captions, instances, person_keypoints


captions, instances, person_keypoints = get_data()

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


