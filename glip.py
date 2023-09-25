import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import random
from tqdm import tqdm
import pickle
import json


def load_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def get_data():
    captions = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/captions_val2017.json')
    instances = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/instances_val2017.json')
    person_keypoints = load_json('../../../groups/course.cap6411/Dataset/coco/annotations/person_keypoints_val2017.json')

    return captions, instances, person_keypoints


captions, instances, person_keypoints = get_data()

for i in captions['annotations']:
    print(i['caption'])

print('=' * 100)
