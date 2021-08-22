import cv2
print("Yoo")
url = "http://10.196.4.244:8080/video"
cap = cv2.VideoCapture(url)
minarea=500
framWidth = 640
frameHeight=480
color =(0,100,255)
#width id number 3
cap.set(3,framWidth)
#length id number 4
cap.set(4,frameHeight)
#for brightness
cap.set(10,300)
cascade = cv2.CascadeClassifier("Resources/haarcascade_licence_plate_rus_16stages.xml")
while True:
    success, img = cap.read()
    img = cv2.resize(img,(500,500))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberplates = cascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberplates:
        area=w*h
        if area>minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"Number Plate",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("NumberPlate",imgRoi)

    cv2.imshow("vdo",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break