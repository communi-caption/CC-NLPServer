from deepsegment import train, generate_data

lines = open('datasets/merged/altyazilar_not_456_yes8_sentences.txt', encoding="utf8").readlines()
print(lines[2])

x, y = generate_data(lines[10000:], max_sents_per_example=6, n_examples=10000)
vx, vy = generate_data(lines[:10000], max_sents_per_example=6, n_examples=1000)

train(x, y, vx, vy, epochs=2, batch_size=64, save_folder='./trained/altyazilar_not_456_yes8_sentences', glove_path='embedding/fasttext_cc/cc.tr.100.vec')