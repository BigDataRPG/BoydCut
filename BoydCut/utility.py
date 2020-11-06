import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
import numpy as np
import pandas as pd
import pickle
import pythainlp
import pathlib

def load_word_embbed():
    HERE = pathlib.Path(__file__).parent
    df_embbed = pd.read_pickle(f"{HERE}/utility_data/word2vec_scb_orchid.pkl")
    print("Load word2vec already !")
    return df_embbed

def load_pos_index():
    HERE = pathlib.Path(__file__).parent
    with open(f"{HERE}/utility_data/pos_idx_dict.pkl", 'rb') as handle:
        unq_pos = pickle.load(handle)
        print("Load pos already !")
    return unq_pos

def load_word_file():
    HERE = pathlib.Path(__file__).parent
    df_word = pd.read_csv(f"{HERE}/utility_data/wordidx_scb_orchid.csv")
    print("Load word file already !")
    return df_word


def post_padding(_pre_ls, _thres=200):

    _post_ls = []

    for _each_ls in _pre_ls:
        _buffer_ls = []
        _n_len = len(_each_ls)
        if _n_len < _thres:
            for _each in _each_ls:
                _buffer_ls.append(_each)
            for _ in range(_thres-_n_len):
                _buffer_ls.append("0")
            _post_ls.append(_buffer_ls)
        elif _n_len >= _thres:
            _post_ls.append(_each_ls[:_thres])

    return _post_ls


def get_dict_embbed():
    ## Get Data
    unq_pos = load_pos_index()

    ## POS
    idx_to_pos = {}
    pos_to_idx = {}

    for idx, pos in enumerate(unq_pos):
        idx_to_pos[idx + 2] = pos
        pos_to_idx[pos] = idx + 2
    idx_to_pos[0] = "PAD"
    idx_to_pos[1] = "UNK"
    pos_to_idx["PAD"] = 0
    pos_to_idx["UNK"] = 1

    df_word = load_word_file()

    ## CHAR
    unq_word_ls = df_word["unq_word"].tolist()
    unq_word_ls = [str(i) for i in unq_word_ls]
    unq_char_ls = list(set("".join(unq_word_ls)))

    idx_to_char = {}
    char_to_idx = {}
    for idx, char in enumerate(unq_char_ls):
        idx_to_char[idx + 2] = char
        char_to_idx[char] = idx + 2

    idx_to_char[0] = "PAD"
    idx_to_char[1] = "UNK"
    char_to_idx["PAD"] = 0
    char_to_idx["UNK"] = 1

    print("Load dict already !")

    return pos_to_idx, char_to_idx


def get_prediction(_array, _thres=0.5):
    return [1 if i > _thres else 0 for i in _array]


def get_pos(_sentence_ls):
    return pythainlp.tag.pos_tag(_sentence_ls, corpus='orchid')


def check_sentence_segment(_para_ls, _label_ls):

    n_para = len(_para_ls)
    sentences_ls = []
    buffer_ls = []

    for _idx, _word, _label in zip(range(n_para), _para_ls, _label_ls[:n_para]):

        if _idx == 0:
            buffer_ls.append("<B-CLS>")

        if _idx != 0:
            if (_label_ls[_idx-1] == 1):
                buffer_ls.append("<B-CLS>")

        if (_label == 0) & (_idx+1!=n_para):
            buffer_ls.append(_word)
            buffer_ls.append("|")
            if _idx==n_para-1:
                sentence = "".join(buffer_ls)
                sentences_ls.append(sentence)
                buffer_ls = []

        elif (_label == 1) | (_idx+1==n_para):
            buffer_ls.append(_word)
            buffer_ls.append("<E-CLS>")
            sentence = "".join(buffer_ls)
            sentences_ls.append(sentence)
            buffer_ls = []

    return sentences_ls


## Mockup Text
def test_text(version=1):
    HERE = pathlib.Path(__file__).parent
    if version==1:
        f = open(f"{HERE}/utility_data/longtext_v1", 'r', encoding="utf8")
        long_text = f.read()
        return long_text
    else:
        f = open(f"{HERE}/utility_data/longtext_v2", 'r', encoding="utf8")
        long_text = f.read()
        return long_text

## Load Model
def load_model():
    HERE = pathlib.Path(__file__).parent
    loaded_model = tf.keras.models.load_model(f"{HERE}/model/boydcut_model", compile=False)
    print("Load model done")
    return loaded_model



def get_word_embbed(_words, _word_embed=None):

    try:
        return _word_embed[_words]
    except:
        return np.array([1]*100)

def get_pos_embbed(_pos, _pos_dict=None):

    try:
        return _pos_dict[_pos]
    except:
        return 0

def get_char_embbed(_char, _char_dict=None):

    try:
        return _char_dict[_char]
    except:
        return 0


def transform_char(_sentences, max_len=200, max_len_char=20, _char_dict=None):

    _X_char = []
    _sent_seq = []
    _word_seq = []
    for _sent in _sentences:

        for _words in _sent[:max_len]:

            num_char = len(_words)
            if num_char >= max_len_char:
                for char in _words[:max_len_char]:
                    _word_seq.append(get_char_embbed(char, _char_dict))
            else:
                left_char = max_len_char - num_char
                for char in _words:
                    _word_seq.append(get_char_embbed(char, _char_dict))
                for _ in range(left_char):
                    _word_seq.append(0)

            _sent_seq.append(_word_seq)
            _word_seq = []

        _X_char.append(_sent_seq)
        _sent_seq = []

    return _X_char



class BoydCut:
    def __init__(self):
        self.df_embbed = load_word_embbed()
        self.pos_to_idx, self.char_to_idx = get_dict_embbed()

        # instantiate model
        self.model = load_model()

    def sentenize(self, _text_ls, _tokenize=True):

        def _handling_inference(_text_ls):
            _X_word_test_pad = post_padding([_text_ls], _thres=200)
            _X_word_test_tensor = tf.convert_to_tensor(
                np.array([[get_word_embbed(word, self.df_embbed) for word in word_ls] for word_ls in _X_word_test_pad]))

            _X_pos_test = get_pos(_text_ls)
            _X_pos_test = [pair[1] for pair in _X_pos_test]
            _X_pos_test_pad = post_padding([_X_pos_test], _thres=200)
            _X_pos_test_tensor = tf.convert_to_tensor(
                np.array([[get_pos_embbed(pos, self.pos_to_idx) for pos in pos_ls] for pos_ls in _X_pos_test_pad]))

            _X_char_test_tensor = tf.convert_to_tensor(np.array(transform_char(_X_word_test_pad, _char_dict=self.char_to_idx)))

            _y_pred = self.model.predict({"word_embedding_input": _X_word_test_tensor,
                                             "pos_embedding_input": _X_pos_test_tensor,
                                             "char_embedding_input": _X_char_test_tensor})

            _y_pred_ = get_prediction(_y_pred[0][:, 1], _thres=0.5)

            # Inference
            _sentences_ls = check_sentence_segment(_text_ls, _y_pred_)

            return _sentences_ls

        if _tokenize:
            _text_ls = pythainlp.tokenize.word_tokenize(_text_ls, engine="deepcut")
            _sentences_ls = _handling_inference(_text_ls)
            return _sentences_ls
        else:
            _sentences_ls = _handling_inference(_text_ls)
            return _sentences_ls