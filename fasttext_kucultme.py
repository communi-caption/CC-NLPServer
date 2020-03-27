import fasttext
import fasttext.util

from gensim.models.keyedvectors import KeyedVectors
from gensim.models.wrappers import FastText

ft = fasttext.load_model('fasttext_cc/cc.tr.300.bin')
print("300 bin loaded")

fasttext.util.reduce_model(ft, 100)
print("300 bin reduced")

ft.save_model('fasttext_cc/cc.tr.100.bin')
print("100 bin saved")

model = FastText.load_fasttext_format('fasttext_cc/cc.tr.100.bin')
print("100 bin read")

model.wv.save_word2vec_format('fasttext_cc/cc.tr.100.vec', binary=False)
print("100 text saved")