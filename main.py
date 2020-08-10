# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from BoydCut.utility import *
import numpy as np
import os
import pathlib

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
df_embbed = load_word_embbed()
pos_to_idx, char_to_idx = get_dict_embbed()

def get_word_embbed(_words):

    try:
        return df_embbed[_words]
    except:
        return np.array([1]*100)

def get_pos_embbed(_pos):

    try:
        return pos_to_idx[_pos]
    except:
        return 0

def get_char_embbed(_char):

    try:
        return char_to_idx[_char]
    except:
        return 0

def transform_char(sentences, max_len=200, max_len_char=20):
    _X_char = []
    for sentence in sentences:
        sent_seq = []
        for i in range(max_len):
            word_seq = []
            for j in range(max_len_char):
                try:
                    word_seq.append(char_to_idx.get(sentence[i][j]))
                except:
                    word_seq.append(char_to_idx.get("PAD"))
            sent_seq.append(word_seq)
        _X_char.append(np.array(sent_seq))

    return _X_char

def handling_inference(_loaded_model, _test_para):
    _test_ls = pythainlp.tokenize.word_tokenize(_test_para, engine="attacut")

    _X_word_test_pad = post_padding([_test_ls], _thres=200)
    _X_word_test_tensor = tf.convert_to_tensor(
        np.array([[get_word_embbed(word) for word in word_ls] for word_ls in _X_word_test_pad]))

    _X_pos_test = get_pos(_test_ls)
    _X_pos_test = [pair[1] for pair in _X_pos_test]
    _X_pos_test_pad = post_padding([_X_pos_test], _thres=200)
    _X_pos_test_tensor = tf.convert_to_tensor(
        np.array([[get_pos_embbed(pos) for pos in pos_ls] for pos_ls in _X_pos_test_pad]))

    _X_char_test_tensor = tf.convert_to_tensor(np.array(transform_char([_test_ls])))

    _y_pred = _loaded_model.predict({"word_embedding_input": _X_word_test_tensor,
                             "pos_embedding_input": _X_pos_test_tensor,
                             "char_embedding_input": _X_char_test_tensor})

    _y_pred_ = get_prediction(_y_pred[0][:, 1], _thres=0.5)

    # Inference
    check_sentence_segment(_test_ls, _y_pred_)


if __name__ == "__main__":
    print("Hello BoydCut")
    loaded_model = load_model()
    handling_inference(loaded_model, test_text(1))
