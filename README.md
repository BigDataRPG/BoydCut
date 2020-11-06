# BoydCut: Thai Sentence Segmenter
> Bidirectional LSTM-CNN Model for Thai Sentence Segmenter


# Development Status
This project is the part of my Thesis in Master's degree at Big Data Engineering, CITE, Dhurakij Pundij University
https://cite.dpu.ac.th/bigdata/


**My Advisor**
- Asst. Prof. Dr. Duangjai Jitkongchuen
- Asst. Prof. Dr. Peerasak Intarapaiboon


# Requirements
- Tensorflow 2.0+
- Python 3.6.x
- pip install -r requirements
> if pip install -r requirements not work please follow Installation steps

## Installation steps
- pip install numpy pandas tensorflow
- pip install deepcut
- pip install pythainlp

## How to use and Examples
- Version 1.0.0
```
boydcut = BoydCut()
sent_ls = boydcut.sentenize("ประเทศฝรั่งเศสแผ่นดินใหญ่ทอดตัวตั้งแต่ทะเลเมดิเตอร์\
                                        เรเนียนจนถึงช่องแคบอังกฤษและทะเลเหนือ")
for sent in sent_ls:
    print(sent)

> <B-CLS>ประเทศฝรั่งเศส|แผ่นดิน|ใหญ่|ทอด|ตัว|ตั้งแต่|ทะเลเมดิเตอร์เรเนียน|จนถึง|ช่อง|แคบ<E-CLS>
> <B-CLS>อังกฤษ|และ|ทะเล|เหนือ<E-CLS>


boydcut = BoydCut()
sent_ls = boydcut.sentenize(['ประเทศฝรั่งเศส','แผ่นดิน','ใหญ่','ทอดตัว','ตั้งแต่',
                            'ทะเลเมดิเตอร์เรเนียน','จนถึง','ช่อง','แคบ',
                            'อังกฤษ','และ','ทะเล','เหนือ'], _tokenize=False)
for sent in sent_ls:
    print(sent)

> <B-CLS>ประเทศฝรั่งเศส|แผ่นดิน|ใหญ่|ทอด|ตัว|ตั้งแต่|ทะเลเมดิเตอร์เรเนียน|จนถึง|ช่อง|แคบ<E-CLS>
> <B-CLS>อังกฤษ|และ|ทะเล|เหนือ<E-CLS>
```

## Limitation 
- Document feeding is not available yet !
- Max Word for feeding: 200 words / paragraph
- Please use "\n" for decrease size of paragraph
- Results: [sentence1, sentence2, sentence3,..., sentenceN]

## Dependency
- POS apply pythainlp.tag.pos_tag(_sentence_ls, corpus="orchid") 
- Tokenization apply pythainlp.tokenize.word_tokenize(_text_ls, engine="deepcut")



# Contributor
Sorratat Sirirattanajakarin (Boyd)

- Youtube: https://youtube.com/c/BigDataRPG
- Fanpage: https://www.facebook.com/bigdatarpg/
- Medium: https://www.medium.com/bigdataeng
- Github: https://www.github.com/BigDataRPG
- Kaggle: https://www.kaggle.com/boydbigdatarpg
- Linkedin: https://www.linkedin.com/in/boyd-sorratat
- Twitter: https://twitter.com/BoydSorratat
- GoogleScholar: https://scholar.google.com/citations?user=9cIeYAgAAAAJ&hl=en

# License and reference
Please make sure to cite the paper if you use BoydCut for your research ^^:
>**BoydCut: Bidirectional LSTM-CNN Model for Thai Sentence Segmenter** 
*S. Sirirattanajakarin, D. Jitkongchuen, P. Intarapaiboon* 2020 1st International Conference on Big Data Analytics and Practices (IBDAP)


