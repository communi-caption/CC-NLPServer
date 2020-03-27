import segment
import colorama
colorama.init()

segment.PREDEFINED_ENABLED = True
print("--- ready ---")

#print(perform_segment("merhaba nasılsınız ali okula gitti beyza da okuldan geldi"))
#print(perform_segment("merhaba benim adım ali senin adın nedir"))

test_sentences = [
    "merhaba ben ayhan memnun oldum ben de murat nasılsınız iyiyim teşekkür ederim ya siz ben de iyiyim",
    "hotel rezervasyonu yaptırmak istiyordum varış tarihiniz ne zaman mayısın 14ünde varmış olacağım ne kadar kalacaksınız 3 gece için tutmak istiyordum odada kaç kişi kalıcak tek başıma kalacağım sigara içilebilir ya da içilemez odalardan hangisini isterdiniz sigara içilmeyen odadan istiyorum rezervasyonunuzu yaptık giriş için geldiğinizde lütfen 4 gibi burada olun",
    "merhaba merhaba nasılsınız çok iyiyim nereden geliyorsunuz paristen geliyorum okuyor musunuz evet üniversitede okuyorum",
    "mesleğiniz ne işiniz ne ne iş yapıyorsunuz nerede çalışıyorsunuz ben star gazetesinde gazeteciyim ben x şirketinde muhasebeciyim altı yıldır şoförüm",
    "müze hangi günler açık pazartesi hariç her gün açığız türkiye’de genellikle pazartesileri müzeler kapalıdır müze saat  kaçtan kaça kadar açık müzemiz sabah saat dokuzdan akşam 6 ya kadar kesintisiz açıktır 2 tam bir de öğrenci bileti lütfen İçerde fotoğraf çekebilirsiniz kulaklık ister misiniz evet lütfen 3 kulaklık alalım tam bilet 15 tl ve on sekiz yaşa kadar altmış beş yaştan sonra indirimli bilet on tldir  sizin toplam kırk tl tuttu kulaklıklar ücretsizdir benim elli liram var buyrun on lira para üstünüz İçerde bir kafe var mı evet sandviç salata  içecek gibi yiyecekler satan bir kafemiz mevcuttur kafe alt kattadır",
    "taksi boş musunuz evet ne tarafa gitmek istiyorsunuz aksaraya gitmek istiyorum valizlerinizi bagaja koyalım hangi yoldan gidelim en kısa yoldan gidelim acelem var nasıl isterseniz borcum ne kadar aksimetre 22 tl tuttu bende 50 tl var sizde üstü var mı buyurun paranın üstünü alın valizlerinize yardım edeyim",
    "efendim kapalı yerlerde sigara içmek yasak biliyorsunuz ama bahçemizde sigara içebilirsiniz orada yasak değil şu masaya oturabilirsiniz	 it’s not forbidden there you can have a seat  at that table tamam bana orta şekerli bir kahve kızıma da bir dondurma getirir misiniz dondurma  neli olsun vişne ve çukulatalı olsun ateşiniz var mı ben yakayım ben arada bir bu pastaneye gelirim gazetemi okur bir türk kahvesi içerim bu pastaneyi eskiden beri çok severim ben de burayı sevdim dondurması da çok lezzetli teşekkürler babacığım",
    "merhaba doktor iki farklı sorun yaşıyorum hoşgeldiniz  dinliyorum kolumda böyle kırmızı bir leke çıktı ve kaşınıyor görünüşte egzamaya benziyor ancak ben dahiliyeciyim  bu leke için bir dermatoloğa görünmeniz gerekiyor for this blemish o halde ikinci sorunumu anlatayım sık sık başım ağrıyor ve bazen çok şiddetli olabiliyor	 bunun pek çok sebebi olabilir  bunun için bir nöroloğa görünmenizi tavsiye ediyorum",
    "ayten abla günaydın sana aidat makbuzunu getirdim hmm 30 lira vereyim bekle geliyorum osman efendi abla çöpünü de çıkarayım kapının önüne teneke kutular atılmış onları da çöpe at osman efendi attım bile abla yarın akşam apartman toplantısı var haberin var mı var ben de katılacağım kim yeni yönetici seçilecek biliyor musun doktor turgay aday olacakmış diyorlar haydi hayırlısı bana da bir ekmek getirir misin lütfen tabii ayten abla görüşürüz",
    "merhaba ben murat demirin annesiyim hoş geldiniz şöyle oturun ben murat’ın notlarına baktım hepsi çok iyi fakat murat biraz dalgın derslerde sıkılıyor gibi matematiği ve müziği çok iyi ama tarih  coğrafyayı sevmiyor coğrafyadan altı  tarihten beş aldı fena değil tabii ama diğer bütün dersleri daha iyi arkadaşlarıyla uyumlu genelde sessiz ve nazik bir talebe bunları duyduğuma memnun oldum evde de güzel ders çalışıyor odası muntazam ve temiz korkmaya gerek yok murat sınıfımdaki en iyi talebelerimden biri eşime de anlatınca o da sevinecek İyi günler teşekkürler veli bey",
]

print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
print("#######################################################################################################################")
print(colorama.Style.RESET_ALL)

for test_sentence in test_sentences:
    print(segment.perform_segment(test_sentence))
    print()

print(colorama.Fore.YELLOW + colorama.Style.BRIGHT)
print("#######################################################################################################################")
print(colorama.Style.RESET_ALL)
