from BoydCut.utility import *


def main(_loaded_model):
    boydcut = BoydCut()

    print("Hello BoydCut")
    print(f"Raw Sentence: \nประเทศฝรั่งเศสแผ่นดินใหญ่ทอดตัวตั้งแต่ทะเลเมดิเตอร์เรเนียนจนถึงช่องแคบอังกฤษและทะเลเหนือ")
    print(f"Segmentation Sentence: ")

    sent_ls = boydcut.sentenize("ประเทศฝรั่งเศสแผ่นดินใหญ่ทอดตัวตั้งแต่ทะเลเมดิเตอร์เรเนียนจนถึงช่องแคบอังกฤษและทะเลเหนือ")
    for sent in sent_ls:
        print(sent)

    sent_ls = boydcut.sentenize(['ประเทศฝรั่งเศส','แผ่นดิน','ใหญ่','ทอดตัว','ตั้งแต่','ทะเลเมดิเตอร์เรเนียน','จนถึง','ช่อง','แคบ','อังกฤษ','และ','ทะเล','เหนือ'], _tokenize=False)
    for sent in sent_ls:
        print(sent)

if __name__ == "__main__":
    loaded_model = load_model()
    main(loaded_model)
