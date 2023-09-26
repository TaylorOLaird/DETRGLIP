import json
from PIL import Image
import glob
import random
from transformers import pipeline


def load_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def load_images(file):
    image_list = []
    for filename in glob.glob(f'{file}*.jpg'):
        im = Image.open(filename)
        image_list.append(im)

    return image_list


def get_data():
    captions = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/captions_val2017.json')
    instances = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/instances_val2017.json')
    person_keypoints = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/person_keypoints_val2017.json')
    images = load_images('../../../groups/course.cap6411/Dataset/coco/val2017/')

    return captions, instances, person_keypoints, images


captions, instances, person_keypoints, images = get_data()

# save one random image
random_image = random.randint(0, len(images))
test_image = images[random_image]
images[random_image].save('random_image.jpg')

pipe = pipeline(model="aychang/fasterrcnn-resnet50-cpu")
pipe(test_image)
