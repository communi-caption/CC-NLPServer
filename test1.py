from deepsegment import DeepSegment
import json

################################################################################################################################################
i_window = 7
test_datas = [
    #'sevgi anlasmak degildir nedensiz de sevilir',
    #'nedensiz de sevilir sevgi anlasmak degildir',
    #'bu sırada kapıya bekçi kulübesi olarak kullanılan bir ikinci kat inşa ettiler bu katın inşa amacı olası bir rum isyanına karşı şehri korumaktı',
    #'sessizlik içinde sürdürdükleri yaşam savaşlarına devam ederken dış dünyanın dehşetiyle de yüzleşmek zorunda kaldı bilinmeze doğru tehlikeli bir şekilde gitmeye zorlanırken kumdan yolun ardında pusuda yatan ve ses yoluyla avlanan yaratıkların tek tehlike olmadığının da kısa sürede farkına vardı',
    #"buraya kadar geldi kaldı kahve içmeden gitti vicdansız",
    #"eve gittim evden çıktım",
    #"ali okula gitti beyza da okuldan geldi",
    #"merhaba nasılsın iyiyim sen nasılsın",
    #"şu an ben çağdaş hocayım bitirme projeniz olmamış çocuklar hepinizi bıraktım",
    #"merhaba Türkiyede eczaneler hangi saatlerde açıktır sabah 9dan akşam 5e kadar açıklar saat kaç saat yedi buçuk o halde eczaneler kapalı mıdır nöbetçi eczaneler açık olmalı hangi eczanenin nöbetçi olduğunu nasıl öğrenebilirim internette nöbetçi eczane aratabilir veya kapalı bir eczanenin kapısından adres alabilirsiniz teşekkür ederim iyi akşamlar",
    "burası sizce uygun mu uygunsa karavanınızı buraya çekebilirsiniz burası uygun öğleden sonra güneş de almaz bol ağaç olması çok iyi denize 100 metreyiz her türlü konfor yok ama tuvaletlerimiz temizdir ve bize yakın iki tane ucuz lokanta var iyi bizden başka kaç tane karavan var henüz daha çok kişi gelmedi burası kalabalık değil sizden başka iki karavan daha var böylesi daha iyi",
    "boş musunuz taksime kadar ne kadar tutar lütfen burada durun bir şey alacağım beni biraz bekler misiniz sağa dönün sola dönün bir sonraki sağa dönün gelecek kavşakta geri dönün"
    ]
test_datasets = [
    "trained/too_old/4_sentence_ve_altyazi",
    "trained/all",
    "trained/altyazilar_not_456_senteces",
    "trained/altyazilar_not_123456_sentences",
    "trained/altyazilar_not_456_yes8_sentences",
]
################################################################################################################################################

def perform_segment(segmenter):
    pass
    pass


################################################################################################################################################
results = {}

index = 0
for test_data in test_datas:
    results[str(index)] = {}
    index = index + 1

index = 0
for test_data in test_datas:
    print(test_data)

    for data_set in test_datasets:
        results[str(index)][data_set] = {}

    for data_set in test_datasets:
        print(data_set)
        f_checkpoint = data_set + "/checkpoint"
        f_params = data_set + "/params"
        f_utils = data_set + "/utils"
        segmenter = DeepSegment(lang_code=None, checkpoint_path=f_checkpoint, params_path=f_params, utils_path=f_utils, tf_serving=False, checkpoint_name=None)
        res = segmenter.segment_long(test_data, n_window=i_window)
        results[str(index)][data_set] = res

    index = index + 1

################################################################################################################################################
print(results)