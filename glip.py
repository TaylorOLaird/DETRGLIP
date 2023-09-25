import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import random
from tqdm import tqdm
import pickle


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def get_data():
    label_names = unpickle('../../../../groups/course.cap6411/cifar-10-batches-py/batches.meta')

    labels = []
    for i in range(len(label_names[b'label_names'])):
        # strip the b' and ' from the label names
        labels.append(label_names[b'label_names'][i].decode("utf-8"))

    # load the image data
    data = unpickle('../../../../groups/course.cap6411/cifar-10-batches-py/test_batch')

    images_data = data[b'data']
    targets = data[b'labels']

    new_images_data = []

    for img in images_data:
        img = img.reshape(3, 32, 32)
        img = img.transpose(1, 2, 0)
        img = Image.fromarray(img, 'RGB')
        new_images_data.append(img)

    return new_images_data, targets, labels