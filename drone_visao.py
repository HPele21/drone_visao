import cv2 #lib pro processamento imagem e video
import numpy as np #lib pra manipular os arrays
from pyzbar.pyzbar import decode #lib pra decodificar qrcode e codigo de barras

cap = cv2.VideoCapture(0) #objeto para a captura e webcam id
cap.set(3,640) #largura(640 pixels)
cap.set(4,480) #altura(480 pixels)

while True: #loop

    success,img = cap.read() #faz a leitura

    for barcode in decode(img): #decodifica qualquer qrcode ou codigo de barras
        print(barcode.data)
        myData = barcode.data.decode('utf_8') #conversao e armazenamento do conteudo
        print(myData)
        pts = np.array([barcode.polygon], np.int32) #obtem os pontos e cria o array
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5) #define a imagem, os pontos, a cor e espessura
        pts2 = barcode.rect #posiçao do poligono
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2) #colocando o conteudo na borda

    cv2.imshow('Result', img) #mostra a imagem
    cv2.waitKey(1) #delay
