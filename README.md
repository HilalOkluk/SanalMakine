# 🖐️ Kamera ile Temassız Hesap Makinesi

Bu proje, el hareketleriyle kontrol edilen **temassız bir hesap makinesi** uygulamasıdır. `OpenCV` ve `cvzone` kütüphaneleriyle geliştirilmiş bu sistemde, kullanıcı elini kameraya göstererek sanal tuşlara tıklayabilir ve matematiksel işlemler gerçekleştirebilir.

---

## 🎯 Proje Amacı

Kullanıcının fiziksel olarak bir nesneye temas etmeden, sadece **parmak hareketleriyle** etkileşime girebildiği etkileşimli bir sistem geliştirmek. Özellikle pandemi sonrası temassız arayüzler popülerlik kazanmıştır. Bu proje, bu tür insan-bilgisayar etkileşiminin (HCI) basit ama işlevsel bir örneğidir.

---

## 📸 Nasıl Çalışır?

- Web kamerası açılır ve eldeki işaret & orta parmak pozisyonları takip edilir.
- İki parmak ucu arasındaki mesafe hesaplanır.
- Bu mesafe belli bir eşikten küçükse (örneğin <70px), bu bir "tıklama" olarak yorumlanır.
- Parmağın konumuna göre ekrandaki sanal butonlardan biri tetiklenir.
- İşlemler yapılır ve sonuç ekrana yazılır.

---

## 🧩 Kullanılan Teknolojiler

- **Python 3**
- **OpenCV** – Görüntü işleme
- **cvzone** – El takibi ve parmak mesafesi ölçümü
- **Mediapipe (cvzone içinde)** – El iskeleti tespiti

---

## 🖱️ Özellikler

- 🧠 Yapay zeka ile el takibi
- 🔢 Temel aritmetik işlemler: `+`, `-`, `*`, `/`, `=`, `.`
- 🧼 Geri silme butonu (C)
- 💡 Ekran üstü hesaplama görüntüleme
- ⏱️ Tek tıklamada yanlışlıkla birden fazla tuş algılanmasını önlemek için gecikme sistemi

---

## ▶️ Ekran Görüntüsü

> 📷 Görsel eklemek istersen: `screenshots/hand_calc_demo.png`

---

## 🛠️ Kurulum

### Gereksinimler:

- Python 3.7+
- Webcam

### Gerekli Kütüphaneleri Yükleyin:

```bash
pip install opencv-python cvzone
```

> `cvzone` modülü otomatik olarak `mediapipe`'i içerir.

---

## 🧪 Uygulamayı Çalıştır

```bash
python el_hesap_makinesi.py
```

> Tüm hesaplama işlemlerini yapmak için kameraya parmaklarınızı gösterin.

---

## 🎮 Kontroller

| Buton | İşlev |
|-------|-------|
| 0-9   | Sayılar |
| + - * / | İşlem operatörleri |
| =     | Hesapla |
| C     | Geri sil |
| ESC   | Programdan çık |
| c     | Ekranı temizle |

---

## 📁 Proje Yapısı

```
el_hesap_makinesi/
├── el_hesap_makinesi.py     # Ana uygulama dosyası
├── README.md                # Bu dosya
└── requirements.txt         # Gerekli kütüphaneler (opsiyonel)
```

---

## 👤 Geliştirici

Bu proje **Hilal Öklük** tarafından geliştirilmemiştir. Eğitim amaçlı olarak farklı kaynaklardan faydalanılmış ve referans kodlar temel alınarak yeniden düzenlenmiştir.

Kaynak alınan projelerden bazıları:

- [`cvzone` örnekleri – Murtaza's Workshop](https://github.com/cvzone/cvzone)
- YouTube üzerindeki el takibi ve sanal klavye/hesap makinesi projeleri
- Açık kaynaklı OpenCV projeleri

Proje, yalnızca **öğrenme ve gösterim amacıyla** uyarlanmıştır. Orijinal geliştiricilere saygıyla 🙏
