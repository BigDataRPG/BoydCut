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
- pip install -r requirements.txt

### Example Results
```
handling_inference(loaded_model, "ประเทศฝรั่งเศสแผ่นดินใหญ่ทอดตัวตั้งแต่ทะเลเมดิเตอร์\
                                        เรเนียนจนถึงช่องแคบอังกฤษและทะเลเหนือ")

> ประเทศฝรั่งเศส|แผ่นดิน|ใหญ่
> ทอดตัว|ตั้งแต่|ทะเลเมดิเตอร์เรเนียน|จนถึง|ช่อง|แคบ
> อังกฤษ|และ|ทะเล|เหนือ|

handling_inference(loaded_model, "เศษฝรั่งได้ชื่อว่าเป็นประเทศที่มีการประท้วงบ่อยและเยอะที่สุด")

> ศษ|ฝรั่ง|ได้|ชื่อ|ว่า|เป็น|ประเทศ|ที่|มี
> การ|ประท้วง|บ่อย|และ|เยอะ|ที่สุด|
```



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