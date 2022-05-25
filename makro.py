import keyboard
import time
import pyautogui

print("[------------------------]\n     Howert Makro v1.0\n[------------------------]")
a = input("Makroyu başlatmak için rastgele bir tuşa tıklayınız. ")
bb = int(input("Tek tıkta kaç kez basılacağınızı giriniz (Kısaca kaç cps olsun. Craftrise vb. oynayacak iseniz 3 ideal.) >> "))
gg = input("Makroyu hangi tuşa atayayım? >> ")
print(f"Makro başlatılmıştır. {gg} tuşuna basarak {bb} cps makroyu kullanabilirsiniz.")
def makro():
    for x in range(bb):
      pyautogui.click()
while True:
  if keyboard.is_pressed(f"{gg}"):
    makro()
