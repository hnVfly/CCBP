"""GluonCV Model Zoo"""
# pylint: disable=wildcard-import
from .model_zoo import get_model, get_model_list
from .model_store import pretrained_model_list
from .faster_rcnn import *
from .ssd import *
from .cifarresnet import *
from .cifarwideresnet import *
from . import segbase
from .resnetv1b import *
from .nasnet import *
from .alexnet import *
from .densenet import *
from .inception import *
from .resnet import *
from .squeezenet import *
from .vgg import *
from .mobilenet import *