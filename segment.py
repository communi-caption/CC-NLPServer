from deepsegment import DeepSegment
import json
import string
from util import *
from predefined import *

################################  Constants #######################################
N_WINDOW = 7
MODEL_PATH = "trained/altyazilar_not_456_senteces"
CHECKPOINT_PATH = MODEL_PATH + "/checkpoint"
PARAM_PATH = MODEL_PATH + "/params"
UTILS_PATH = MODEL_PATH + "/utils"
PREDEFINED_ENABLED = True

################################ Init DeepSegmenter ################################
segmenter = DeepSegment(lang_code=None, checkpoint_path=CHECKPOINT_PATH, params_path=PARAM_PATH, utils_path=UTILS_PATH, tf_serving=False, checkpoint_name=None)


################################ Init predefined ################################
def normalize_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.strip().split())
    text = lower_tr(text)
    return text

PREDEFINED_LENGTH = len(PREDEFINED)
PREDEFINED.sort(key=len, reverse=True)
PREDEFINED_NORMALIZED = [normalize_text(x) for x in PREDEFINED]

################################ Function: split with predefined ################################
def split_with_predefined(text):
    text = normalize_text(text)
    text = " " + text + " "
    for i in range(0, PREDEFINED_LENGTH):
        predefined = PREDEFINED_NORMALIZED[i]
        direction = predefined[-1:]
        predefined = predefined[0 : len(predefined) - 1]

        if direction == 'l':
            indicator = "  <|>[[{" + str(i) + "}]]  "
        elif direction == 'r':
            indicator = "  [[{" + str(i) + "}]]<|>  "
        elif direction == 'b':
            indicator = "  <|>[[{" + str(i) + "}]]<|>  "
        else: exit()

        text = text.replace(" " + predefined + " ", indicator)

    def revert(text):
        for i in range(0, PREDEFINED_LENGTH):
            indicator = "[[{" + str(i) + "}]]"
            text = text.replace(indicator, PREDEFINED_NORMALIZED[i][0:len(PREDEFINED_NORMALIZED[i]) - 1])
        return text
    
    splitted = text.split("<|>")
    splitted = [x for x in splitted if len(x) > 0]
    splitted = [revert(x).strip() for x in splitted]

    return splitted


################################ Function: flat lists ################################
def flat_lists(list_of_list):
    result = []
    for the_list in list_of_list:
        for item in the_list:
            result.append(item)
    return result


########################### Function: perform segmentation with ml ###########################
def segment_with_ml(text):
    return segmenter.segment_long(text, n_window=N_WINDOW)


################################ Function: perform segmentation ################################
def perform_segment(text):
    text = normalize_text(text)
    segments = [text]
    if PREDEFINED_ENABLED:
        segments = split_with_predefined(text)
    segments = [segment_with_ml(x) for x in segments]
    return flat_lists(segments)