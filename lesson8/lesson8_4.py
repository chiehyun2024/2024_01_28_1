import random
import pyinputplus as pyip

def playGame():
    min = 1
    max = 100
    guess = random.randint(min,max)
    count = 0

    print("============猜數字遊戲============\n\n")
    print(f'要猜的數字是{guess}')
    while(True):
        try:
            keyin = int(input(f'猜數字範圍{min}~{max}:'))
            count += 1
            if keyin<=max and keyin >=min:
                if keyin == guess:
                    print(f'賓果!猜對了,答案是:{guess}')
                    print(f'你猜了{count}次')
                    break
                elif keyin > guess:
                    print('在小一點')
                    max = keyin - 1

                elif keyin < guess :
                    print('在大一點')
                    min = keyin + 1
            else:
                print('超出範圍')

        except:
            print('輸入的格式錯誤')
            count += 1
    
        print(f'已經猜了{count}次')

while(True):
    playGame()
    menu_value = pyip.inputMenu(['yes','no'],prompt='你還要繼續嗎?\n',numbered=True)
    if menu_value == 'no':
        break
print('遊戲結束')   