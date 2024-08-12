import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, konum, genislik, yukseklik, deger):
        self.konum = konum
        self.genislik = genislik
        self.yukseklik = yukseklik
        self.deger = deger

    def ciz(self, img):
        # Butonları çiz
        cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                      (50, 50, 50), 3)
        cv2.putText(img, self.deger, (self.konum[0] + 20, self.konum[1] + 55), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)

    def klikKontrol(self, x, y):
        global img  # img değişkenine global erişim sağlamak için ekledik
        if self.konum[0] < x < self.konum[0] + self.genislik and \
                self.konum[1] < y < self.konum[1] + self.yukseklik:
            cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                          (50, 50, 50), 3)
            cv2.putText(img, self.deger, (self.konum[0] + 20, self.konum[1] + 55), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 0, 0), 2)
            return True
        else:
            return False

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating Button
butonListeDegerleri = [['7', '8', '9', '*'],
                       ['4', '5', '6', '='],
                       ['1', '2', '3', '+'],
                       ['0', '/', '.', '-'],
                       ]

butonListesi = []
for x in range(4):
    for y in range(4):
        xkonumu = x * 80 + 700
        ykonumu = y * 80 + 150
        butonListesi.append(Button((xkonumu, ykonumu), 80, 80, butonListeDegerleri[y][x]))


# Değişkenler
denklemim = '2+3'
gecikmeSayaci = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Elin algılanması
    hands, img = detector.findHands(img, flipType=False)

    # Draw All Buttons
    cv2.rectangle(img, (700, 50), (700 + 320, 50 + 100),  # Çerçeveyi 320 piksel genişlikte yaptık
                  (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (700, 50), (700 + 320, 50 + 100),  # Çerçeveyi 320 piksel genişlikte yaptık
                  (50, 50, 50), 3)

    for buton in butonListesi:
        buton.ciz(img)



    # Sonucu göster
    cv2.putText(img, denklemim, (710, 120), cv2.FONT_HERSHEY_PLAIN,
                3, (50, 50, 50), 3)

    # Display
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord('c'):
        denklemim = ''

    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
