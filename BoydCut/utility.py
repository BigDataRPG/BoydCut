import tensorflow as tf
import pandas as pd
import pickle
import pythainlp
import pathlib

def load_word_embbed():
    HERE = pathlib.Path(__file__).parent
    df_embbed = pd.read_pickle(f"{HERE}/utility_data/word2vec_scb_orchid.pkl")
    print("Load word2vec done")
    return df_embbed

def load_pos_index():
    HERE = pathlib.Path(__file__).parent
    with open(f"{HERE}/utility_data/pos_idx_dict.pkl", 'rb') as handle:
        unq_pos = pickle.load(handle)
        print("Load pos done")
    return unq_pos

def load_word_file():
    HERE = pathlib.Path(__file__).parent
    df_word = pd.read_csv(f"{HERE}/utility_data/wordidx_scb_orchid.csv")
    print("Load word file done")
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
                #_buffer_ls.append(np.array([0]*100))
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

    return pos_to_idx, char_to_idx


def get_prediction(_array, _thres=0.5):
    return [1 if i > _thres else 0 for i in _array]


def get_pos(_sentence_ls):
    return pythainlp.tag.pos_tag(_sentence_ls, corpus='orchid')


def check_sentence_segment(_para_ls, _label_ls):
    n_para = len(_para_ls)
    sentences_ls = []
    buffer_ls =[]
    for _idx, _word, _label in zip(range(n_para), _para_ls, _label_ls[:n_para]):
        if _label == 0:
            print(_word, end="|", flush=True)
            buffer_ls.append(_word)
            buffer_ls.append("|")
            if _idx==n_para-1:
                sentence = "".join(buffer_ls)
                sentences_ls.append(sentence)
                buffer_ls = []
        elif _label == 1:
            print(_word, end="\n", flush=True)
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