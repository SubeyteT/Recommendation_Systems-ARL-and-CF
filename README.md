# Recommendation_Systems-ARL-and-CF

Tavsiye sistemleri, pazarlama stratejileri için sıkça tercih edilen yöntemlerdendir. Bu yaygınlığın sebebi kullanıcı ve ürünlerin kendi içindeki ve birbirleri arasındaki ilişkilerini tahmin etmede elde ettiği başarıdır. Bu projede iki farklı veri seti üzerinde iki farklı tavsiye sistemi algoritması uygulanmıştır: "Birliktelik Kuralı Öğrenimi (Association Rule Learning)" ve "İş Birlikçi Filtreleme (Collaborative Filtering)". Bahsedilen algoritmalar hakkında detaylı bilgi yazının devamında sunulmuştur.

![ARL-CF](https://user-images.githubusercontent.com/83431435/122686645-e5b8ac80-d21a-11eb-8156-d36dab6dfae6.png)

Özellikle son zamanlarda talebi artan tutan e-ticaret sitelerinin ürün yelpazesi oldukça geniştir. Bir kullanıcının bütün siteyi tarayarak istediği ürüne ulaşması ya da kullanıcının geçmiş ve anlık tercihlerine uygun ürün önerisinde bulunmak tavsiye sistemleri olmadan mümkün değildir. Tavsiye sistemleri temelde kullanıcının geçmiş bilgilerini kullanarak tercih ettiği ürünlerin diğer ürünlerle ilişkisini tespit ederek satın alma ihtimali yüksek olan ürünleri karşısına çıkarmak için kullanılır.  

## Association Rule Learning:
Özellikle ürün çeşitliliğinin çok olduğu veri setleri içinde gizlenmiş ilişkileri bulmak için kullanılan bir kural tabanlı bir makine öğrenmesi yöntemidir. Örneğin: bir market veri setinin barındırdığı fişlerin değerlendirilmesi sonucu Süt -> Tereyağı, Süt -> Ekmek gibi birlikte alınan ürünlerin tespit edilmesi. Müşterilerin ortak olarak birlikte alma davranışı gösterdiği ürünleri bulmak önemlidir.

Bir müşterinin süt aldığında ekmek alma olasılığı nedir? Bir müşterinin cips aldığında gazlı içecek alma olasılığı kaç kat artar? Bu soruların cevaplarından elde edilen öngörü çeşitli aksiyonlar alınabilir. Birlikte tercih edilen ürünleri, biri alındığında diğeri de alınan ürünleri tespit etmek gerek e-ticarette ürün önerisi stratejisi, gerek fiziksel marketlerde ürünlerin raf sıralaması, market konumlandırması gibi strateji geliştirmek için önemlidir. Ayrıca, bu kurallar müşteri satın alma davranışlarını kavrayabilmeyi de sağlar. 

Bu birliktelikleri tespit etmek için bir sepet analizi yöntemi olan Apriori Algoritması kullanılır. Tablo-1'de formülleri ve açıklamaları verilen Support, Confidence ve Lift değerleri bulunarak sonuca bağlı çeşitli pazarlama teknikleri kullanılabilir. 

Tablo-1:
![ARL](https://user-images.githubusercontent.com/83431435/122685942-5362d980-d217-11eb-8d49-5a353b34331b.png)

Birliktelik kuralını bulabilmek için bir support değeri belirlendilten sonra sırasıyla iki adımlı süreç izlenir:

1- Tüm sık tekrarlanan çift ve üçlü kombinasyonlar arasından belirlenen eşik değerin altında kalanlar elenir.
3- Elde kalan kombinasyonların support, confidence ve lift değerleri hesaplanarak güçlü birliktelik sergileyen gruplar tespit edilir. Buna göre aksiyon alınır. 

2- Sık tekrarlanan Öğelerden güçlü birliktelik kuralları oluşturulur: Bu kurallar minimum destek ve minimum güven değerlerini karşılamalıdır.

## Colaborative Filtering:

İşbirlikçi filtreleme yöntemleri bir kullanıcının herhangi bir ürüne olan ilgi düzeyini tespit etmek ve buna bağlı ürün filtreleyerek öneride bulunmak için kullanılır. Bu amaç için temelde iki farklı yönteme başvurulur: Model Tabanlı İşbirlikçi Filtreleme ve Bellek Tabanlı İşbirlikçi Filtreleme Yöntemleri. Model Tabanlı İşbirlikçi Filtreleme yöntemleri ise Öğe Tabanlı İşbirlikçi Filtreleme ve Kullanıcı Tabanlı İşbirlikçi Filtreleme olarak ikiye ayrılır. Ancak, bu yöntemler birlikte kullanılarak hibrit bir model de oluşturulabilir.

Kullanıcı temelli filtrelemede amaç kullanıcı davranışları ile öneriler gerçekleştirmektir. Filtreleme yaparken bir kullanıcının bir ürüne olan muhtemel ilgisini bulmak için ilk önce söz konusu ürünü değerlendiren kullanıcılar arasındaki benzerlikler ve aktif kullanıcıya en çok benzeyen kullanıcılar bulunur. Örneğin Spotify'da kişinin tercih ettiği müzikler üzerinden diğer kullanıcılar ile benzerliği tespit edilerek kullanıcıya en çok benzeyen kullanıcıların dinlediği diğer müziklerin önerilmesi. İki kullanıcı arasındaki benzerliğini bulmak içinse kosinüs benzerliği ve pearson korelasyon katsayısı en çok tercih edilen yöntemlerdir. 

Ürün temelli filtreleme ise kullanıcıların verdiği oylar üzerinden ürün benzerliklerini tespit eden bir yöntemdir. Yani örneğin kişi yöntemin bir nesnesi olmaktan çıkarılarak izlediği bir filmle benzer beğenilme yapısı gösteren filmler bulunur. Diğer izleyicilerin toplu olarak farklı filmlere verdiği benzer reaksiyonlar bulunarak benzer filmler de bulunmuş olur. Korelasyonu en yüksek filmler seçilerek kullanıcıya öneri olarak sunulur. 

Bu çalışmada kişi ve öğe temelli (user-based, item-based) hibrit bir model çalışılmıştır. 

Kaynakça:

1. https://www.veribilimiokulu.com/
2. M. Kaur ve S. Kang, “Market Basket Analysis: Identify the Changing Trends of Market Data Using Association Rule Mining”, Procedia Computer Science, c. 85, ss. 78-85, 2016, doi: 10.1016/j.procs.2016.05.180.
3. Oğuzlar, A . (2004). VERİ MADENCİLİĞİNDE BİRLİKTELİK KURALLARI . Öneri Dergisi , 6 (22) , 315-321 . DOI: 10.14783/maruoneri.678958
4. https://burakdogrul.medium.com/overview-of-recommender-systems-and-implementations-cae13088369
5. H. Bulut ve M. Milli, “New prediction methods for collaborative filtering”, Pamukkale J Eng Sci, c. 22, sy 2, ss. 123-128, 2016, doi: 10.5505/pajes.2014.44227.
6. 

