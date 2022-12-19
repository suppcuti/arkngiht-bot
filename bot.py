from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def clickimg(img,confiden,t):
    x, y = pyautogui.locateCenterOnScreen(img,grayscale=True,confidence=confiden)
    sleep(t)
    pyautogui.click(x,y)
    sleep(t)

def hire_tag(*args):
    for i in args:
        if i == "tag_supporter.png" and pyautogui.locateCenterOnScreen("tag_supporter.png",grayscale=True,confidence=0.96) == None:
            return
        if pyautogui.locateCenterOnScreen(i,grayscale=True,confidence=0.9):
            continue
        else:
            return
    
    for i in args:
        if i == "tag_supporter.png":
            x,y=pyautogui.locateCenterOnScreen(i,grayscale=True,confidence=0.96)
            pyautogui.click(x,y)
            print(i)
        x,y= pyautogui.locateCenterOnScreen(i,grayscale=True,confidence=0.9)
        pyautogui.click(x,y)
        print(i)
    return True

def press(*args):
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

def pressloop(key,n):
    while n > 0:
        n -= 1
        sleep(1)
        press(key)
        print(key)
        sleep(1)

def startGame():
    x, y = pyautogui.locateCenterOnScreen("icon.png",grayscale=True,confidence=0.7)
    pyautogui.click(x,y)
    print("Mo Icon")
    sleep(20)
    click(x,y)
    print("Tiep Tuc")
    sleep(15)
    i=0
    if pyautogui.locateCenterOnScreen("start.png",confidence=0.7) != True:
        while i < 5 :
            i = i+1
            sleep(5)
            pyautogui.click()
            if pyautogui.locateCenterOnScreen("start.png",confidence=0.7):
                clickimg('start.png',0.7,1)
                break
    if pyautogui.locateCenterOnScreen("start.png",confidence=0.7):
        clickimg('start.png',0.7,1)
    sleep(15)
    print("Hoan Thanh Mo Game")
    main()

def basedaily():
    print("Bat dau Base Daily")
    sleep(5)
    if  pyautogui.locateCenterOnScreen("base.png",grayscale=True,confidence=0.8):
        x, y = pyautogui.locateCenterOnScreen("base.png",grayscale=True,confidence=0.8)
        pyautogui.click(x,y)
        sleep(5)
    sleep(6.5)
    x, y = pyautogui.locateCenterOnScreen("basenofi.png",confidence=0.75)
    sleep(1)
    pyautogui.click(x,y)
    sleep(2)
    pressloop("h",4)
    sleep(1)
    pyautogui.click(x,y)
    slave()
    main()

def fillclue():
    # x, y = pyautogui.locateCenterOnScreen("clue.png",grayscale=True,confidence=0.8)
    # pyautogui.click(x,y)
    # sleep(5)
    # x, y = pyautogui.locateCenterOnScreen("clueopen.png",grayscale=True,confidence=0.8)
    # pyautogui.click(x,y)
    # sleep(2)
    while pyautogui.locateCenterOnScreen("Blank Clue.png",grayscale=True,confidence=0.8):
        x, y = pyautogui.locateCenterOnScreen("Blank Clue.png",grayscale=True,confidence=0.8)
        pyautogui.click(x,y)    
        sleep(3)
        keyboard.press_and_release("Alt + Shift + R")
        sleep(3)
    main()

def recruit():
    if pyautogui.locateCenterOnScreen("repage.png",grayscale=False,confidence=0.75):
        clickimg("repage.png",0.8,0.9)
    sleep(2)
    while pyautogui.locateCenterOnScreen("Hire.png",grayscale=True,confidence=0.75):
        x, y = pyautogui.locateCenterOnScreen("Hire.png",grayscale=True,confidence=0.75)
        pyautogui.click(x,y)    
        sleep(3)
        press('x')
        sleep(15)
        pyautogui.click(x,y) 
        sleep(3)
        pyautogui.click(x,y)        
        sleep(1)
        if pyautogui.locateCenterOnScreen("hire_renew.png",confidence=0.8):
            print('Mo Recriument Refesh')
            reloop_hire()
        else:
            print('Mo Recriument thuong')
            filler()
            sleep(1)
            press('l')
            sleep(1)
            press('o')
            sleep(1)
        sleep(3)
    while pyautogui.locateCenterOnScreen("main.png",confidence=0.8) != ImageNotFoundException  :
        sleep(1)
        press('esc')
        pyautogui.click()
        sleep(1)   
        if pyautogui.locateCenterOnScreen("main.png",confidence=0.75):
            break

def single_tag(n):
    if  pyautogui.locateCenterOnScreen(n,grayscale=True,confidence=0.8):
        x, y = pyautogui.locateCenterOnScreen(n,grayscale=True,confidence=0.8)
        pyautogui.click(x,y)
        print(n)    
        return True
        
def filler():
    print("--------------- Start Fillter Tag ---------------")
    if single_tag("tag_top.png") == True :
        print("===========x============x============")
        print("=============x========x==============")
        print("===============TOP TAG===============")
        print("=============x========x==============")
        print("============x===========x============")

        return True
    if single_tag("tag_top2.png") == True :
        print("===========x============x============")
        print("=============x========x==============")
        print("===============TOP TAG===============")
        print("=============x========x==============")
        print("============x===========x============")        
        return True
    if single_tag("tag_senior.png") == True :
        return True
    if single_tag("tag_nuker.png") == True :
        return True
    if single_tag("tag_crowd-control.png") == True :
        return True
    if single_tag("tag_summon.png") == True :
        return True
    #100% ra 5 sao 
    if hire_tag("tag_sp.png","tag_vanguard.png") == True :
        return True
    if hire_tag("tag_sp.png","tag_dp-recover.png") == True :
        return True
    if hire_tag("tag_defense.png","tag_dps.png") == True :
        return True
    if hire_tag("tag_defender.png","tag_dps.png") == True :
        return True
    if hire_tag("tag_defense.png","tag_guard.png") == True :
        return True
    if hire_tag("tag_defender.png","tag_survival.png") == True :
        return True
    if hire_tag("tag_defense.png","tag_survival.png") == True :
        return True
    if hire_tag("tag_defender.png","tag_shift.png") == True :
        return True
    if hire_tag("tag_defense.png","tag_shift.png") == True :
        return True
    if hire_tag("tag_shift.png","tag_dps.png") == True :
        return True
    if hire_tag("tag_shift.png","tag_slow.png") == True :
        return True
    if hire_tag("tag_specialist.png","tag_slow.png") == True :
        return True
    if hire_tag("tag_supporter.png","tag_dps.png") == True :
        return True
    if hire_tag("tag_supporter.png","tag_debuff.png") == True :
        return True
    if hire_tag("tag_aoe.png","tag_debuff.png") == True :
        return True
    if hire_tag("tag_debuff.png","tag_fast-redeploy.png") == True :
        return True
    if hire_tag("tag_debuff.png","tag_specialist.png") == True :
        return True
    if hire_tag("tag_debuff.png","tag_melee.png") == True :
        return True
    if hire_tag("tag_survival.png","tag_specialist.png") == True :
        return True
    if hire_tag("tag_dps.png","tag_specialist.png") == True :
        return True
    if hire_tag("tag_healing.png","tag_dps.png") == True :
        return True
    if hire_tag("tag_healing.png","tag_caster.png") == True :
        return True
    if hire_tag("tag_healing.png","tag_slow.png") == True :
        return True
    if hire_tag("tag_caster.png","tag_dps.png","tag_slow.png") == True :
        return True
    
    print("--------------- Ko 5*---------------")

    if single_tag("tag_shift.png") == True :
        return True   
    if single_tag("tag_specialist.png") == True :
        return True   
    
    if  pyautogui.locateCenterOnScreen("tag_sp.png",grayscale=True,confidence=0.96):
        x, y = pyautogui.locateCenterOnScreen("tag_sp.png",grayscale=True,confidence=0.96)
        pyautogui.click(x,y)
        print("tag_sp.png")    
        return True   
    
    if single_tag("tag_fast-redeploy.png") == True :
        return True    
    if single_tag("tag_debuff.png") == True :
        return True
    # 4 sao
    if hire_tag("tag_healing.png","tag_vanguard.png") == True:
        return True
    if hire_tag("tag_healing.png","tag_dp-recover.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_guard.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_melee.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_dps.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_sniper.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_caster.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_aoe.png") == True:
        return True
    if hire_tag("tag_slow.png","tag_dps.png","tag_ranged") == True:
        return True
    if hire_tag("tag_survival.png","tag_sniper.png") == True:
        return True
    if hire_tag("tag_survival.png","tag_ranged.png") == True:
        return True

    print("--------------- Ko 4*---------------")

def reloop_hire():
    if pyautogui.locateCenterOnScreen("hire_renew.png",confidence=0.8):
        Timdchayko = filler()
        if Timdchayko == True :
            sleep(0.5)
            press('l')
            sleep(0.5)
            press('o')
            return
        if Timdchayko != True or None  :
            clickimg("hire_renew.png",0.8,0.5)
            press('j')
            sleep(2)
            reloop_hire()
    if pyautogui.locateCenterOnScreen("hire_done.png",confidence=0.8):
        filler()
        sleep(0.5)
        press('l')
        sleep(0.5)
        press('o')
        sleep(0.5)

def hire():
    for rc in  pyautogui.locateAllOnScreen("renow.png",grayscale=True,confidence=0.96):
        sleep(1)
        x,y = pyautogui.center(rc)
        sleep(1)
        pyautogui.click(x,y)        
        print('Mo Recriument')
        sleep(1)
        if pyautogui.locateCenterOnScreen("hire_renew.png",confidence=0.8):
            print('Mo Recriument Refesh')
            reloop_hire()
        else:
            print('Mo Recriument thuong')
            filler()
            sleep(1)
            press('l')
            sleep(1)
            press('o')
            sleep(1)
    for rc in  pyautogui.locateAllOnScreen("renow2.png",grayscale=True,confidence=0.96):
        sleep(1)
        x,y = pyautogui.center(rc)
        sleep(1)
        pyautogui.click(x,y)        
        print('Mo Recriument')
        sleep(1)
        if pyautogui.locateCenterOnScreen("hire_renew.png",confidence=0.8):
            print('Mo Recriument Refesh')
            reloop_hire()
        else:
            print('Mo Recriument thuong')
            filler()
            sleep(1)
            press('l')
            sleep(1)
            press('o')
            sleep(1)
    main() 

def farm():
    clickimg("farm.png",0.8,0.5)
    sleep(1)
    press('o')
    sleep(3)
    keyboard.press_and_release("Shift + A")

def done_farm():
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateCenterOnScreen('out1.png',confidence=0.9,grayscale=True):
            clickimg("out1.png",0.8,1)
            sleep(1)
            keyboard.press_and_release("Ctrl + Shift + U")
            break
    main(),sleep(2),clickimg('misson.png',0.8,5),clickimg('collect_all.png',0.8,1),main()

def find_dorm():
    sleep(3)
    if pyautogui.locateCenterOnScreen("slave1.png",confidence=0.8):
        clickimg("slave1.png",0.7,0.5)
    sleep(1)
    while pyautogui.locateCenterOnScreen("slave_dorm.png",confidence=0.8) != ImageNotFoundException  :
        darging()
        sleep(0.5)
        if pyautogui.locateCenterOnScreen("slave_dorm.png",confidence=0.75):
            x,y = pyautogui.locateCenterOnScreen("slave_dorm.png",confidence=0.75)
            x= x +100
            pyautogui.click(x,y)
            break

def slave():
    sleep(2)

    find_dorm()
    sleep(2)
    count = slave_re()
    if  count > 5:
        sleep(2)
        find_dorm()
        sleep(2)
        count = slave_re()
        if  count > 5:
            sleep(2)
            find_dorm()
            sleep(2)
            slave_re()
    sleep(2)
    press('esc'),sleep(2)
    clickimg('slave1.png',0.8,0.1),sleep(2)
    phanbiet_factory(),sleep(2)
    sleep(2)
    main()

def slave_re():
    counts = 0
    count = countimg("test2.png")
    sleep(0.9)
    press('g')
    sleep(0.5)
    for slave in pyautogui.locateAllOnScreen('test2.png',grayscale=True, confidence=0.9):
        sleep(0.1)
        counts= counts +1
        x,y = pyautogui.center(slave)
        sleep(0.5)
        pyautogui.click(x,y)
        if counts == 5:
            sleep(0.5)
            press('k')
            sleep(1)
            darging()
            sleep(1)
            break
    sleep(0.5)
    press('k')
    sleep(1)
    return count

def countimg(img):
    count = 0
    for slave in pyautogui.locateAllOnScreen(img,grayscale=True , confidence=0.9):
        count= count +1
        print(slave)
    print(count)
    return count

def countimg2(img):
    count = 0
    for slave in pyautogui.locateAllOnScreen(img,grayscale=False , confidence=0.96):
        count= count +1
        print(slave)
    print(count)
    return count
def slave_re2():
    count = 0
    for slave in pyautogui.locateAllOnScreen('slave_die.png', confidence=0.96):
        x,y = pyautogui.center(slave)
        sleep(1)
        pyautogui.click(x,y)
        count= count +1
    print(count)

def Find_x(x) :
    if pyautogui.locateCenterOnScreen("slave1.png",confidence=0.8):
        clickimg("slave1.png",0.7,0.5)
    sleep(1)
    while pyautogui.locateCenterOnScreen(x,confidence=0.8) != ImageNotFoundException  :
        sleep(1)
        if pyautogui.locateCenterOnScreen(x,confidence=0.75):
            x,y = pyautogui.locateCenterOnScreen(x,confidence=0.75)
            x= x +120
            pyautogui.click(x,y)
            break

def fill_trading1(x):
    count = 0
    for slave in pyautogui.locateAllOnScreen(x, confidence=0.96):
        sleep(0.5)
        count= count +1
        x,y = pyautogui.center(slave)
        sleep(0.5)
        pyautogui.click(x,y)
        print(count)
        if count == 3:
            press("k")
            break

def main():
    print("====================================")
    while pyautogui.locateCenterOnScreen("main.png",confidence=0.8) != ImageNotFoundException  :
        sleep(1)
        press('esc')
        sleep(1)   
        if pyautogui.locateCenterOnScreen("main.png",confidence=0.75):
            break

def bot():
    startGame()
    sleep(2)
    basedaily()
    sleep(2)
    recruit()
    sleep(2)
    farm()

def darging():
    x, y = pyautogui.locateCenterOnScreen("base1.png",grayscale=True,confidence=0.8)
    pyautogui.moveTo(x+350,y+350)
    sleep(1),pyautogui.dragTo(x+350,y,duration=1)
def darging2(m):
    x, y = pyautogui.locateCenterOnScreen("base1.png",grayscale=True,confidence=0.8)
    
    pyautogui.moveTo(x+350,y+m)
    sleep(0.3),pyautogui.dragTo(x+350,y,duration=2),sleep(1)

def refill_savle(x,y,z):
    sleep(1)
    if pyautogui.locateCenterOnScreen(x,grayscale=True,confidence=0.8) and pyautogui.locateCenterOnScreen(y,grayscale=True,confidence=0.8) and pyautogui.locateCenterOnScreen(z,grayscale=True,confidence=0.8):
        press('g')
        clickimg(x,0.8,0.1),clickimg(y,0.8,0.1),clickimg(z,0.8,0.1)
        press('k')
        return 
    press('s')
    sleep(1)
    if pyautogui.locateCenterOnScreen(x,grayscale=True,confidence=0.8) and pyautogui.locateCenterOnScreen(y,grayscale=True,confidence=0.8) and pyautogui.locateCenterOnScreen(z,grayscale=True,confidence=0.8):
        press('g')
        clickimg(x,0.8,0.1),clickimg(y,0.8,0.1),clickimg(z,0.8,0.1)
        press('k')
    else:
        return False

def free_slave():
    press('x'), sleep(0.5), press('e'), press('r')

def toolong():
    sleep(1)
    if pyautogui.locateCenterOnScreen("slave_eletric.png",grayscale=True,confidence=0.8):
        x,y = pyautogui.locateCenterOnScreen("slave_eletric.png",grayscale=True,confidence=0.8)
        x= x +100
        pyautogui.click(x,y)
        sleep(2),slave_eletric(),sleep(2)

def refill_savle2(x):
    sleep(1)
    if pyautogui.locateCenterOnScreen(x,grayscale=True,confidence=0.8) :
        press('g')
        clickimg(x,0.8,0.1)
        press('k')
        return 
    press('s')
    sleep(1)
    if pyautogui.locateCenterOnScreen(x,grayscale=True,confidence=0.8):
        press('g')
        clickimg(x,0.8,0.1)
        press('k')
    else:
        return False

def slave_factory_vang():
    if refill_savle("gold_slave1.png","gold_slave2.png","gold_slave3.png") != False:
        return
    if refill_savle("gold_slave4.png","gold_slave5.png","gold_slave6.png") != False:
        return
    if refill_savle("all_slave1.png","all_slave2.png","all_slave3.png") != False:
        return
    if refill_savle("all_slave4.png","all_slave5.png","all_slave6.png") != False:
        return
    if refill_savle("all_slave7.png","all_slave8.png","all_slave9.png") != False:
        return
    if refill_savle("basic1.png","basic2.png","basic3.png") != False:
        return
    if refill_savle("basic4.png","basic5.png","basic6.png") != False:
        return
    if refill_savle2("weedy.png") != False:
        return
    
def slave_factory_exp():
    if refill_savle("exp_slave1.png","exp_slave2.png","exp_slave3.png") != False:
        return
    if refill_savle("exp_slave4.png","exp_slave5.png","exp_slave6.png") != False:
        return
    if refill_savle("all_slave1.png","all_slave2.png","all_slave3.png") != False:
        return
    if refill_savle("all_slave4.png","all_slave5.png","all_slave6.png") != False:
        return
    if refill_savle("all_slave7.png","all_slave8.png","all_slave9.png") != False:
        return
    if refill_savle("basic1.png","basic2.png","basic3.png") != False:
        return
    if refill_savle("basic4.png","basic5.png","basic6.png") != False:
        return
    if refill_savle2("weedy.png") != False:
        return

def slave_trader():
    if refill_savle("trader1.png","trader2.png","trader3.png") != False:
        return
    if refill_savle("trader1-1.png","trader1-2.png","trader1-3.png") != False:
        return
    if refill_savle("trader4.png","trader5.png","trader6.png") != False:
        return
    if refill_savle("traderr1.png","traderr2.png","traderr3.png") != False:
        return
    if pyautogui.locateCenterOnScreen('trade1.png',confidence=0.8,grayscale=True):
        clickimg('trade1.png',0.8,1),press('s'),sleep(2),clickimg('trade2.png',0.8,0.1),clickimg('trade3.png',0.8,0.1),press('k')
    return

def slave_off():
    if refill_savle2("off1.png") != False:
        return
    if refill_savle2("off2.png") != False:
        return
    if refill_savle2("off3.png") != False:
        return
    if refill_savle2("off4.png") != False:
        return

def slave_eletric():    
    if refill_savle2("ele1.png") != False:
        return
    if refill_savle2("ele2.png") != False:
        return
    if refill_savle2("ele3.png") != False:
        return
    if refill_savle2("ele4.png") != False:
        return
    if refill_savle2("ele5.png") != False:
        return
def phanbiet_factory():
    sleep(1),press('r'),sleep(1),free_slave(),sleep(1),press('k'),sleep(1)
    darging2(250)#Tang1 
    sleep(0.5)
    if pyautogui.locateCenterOnScreen("slave_factory-empty.png",grayscale=True,confidence=0.8):
        clickimg("slave_factory-empty.png",0.8,0.1)
        sleep(2),slave_factory_vang(),sleep(2)
    if pyautogui.locateCenterOnScreen("slave_trading.png",grayscale=True,confidence=0.8):
        clickimg("slave_trading.png",0.8,0.1)
        sleep(2),slave_trader(),sleep(2),
    
    toolong()
    darging2(250)
    sleep(0.5)
    darging2(250)#Tang 2
    sleep(0.5)
    if pyautogui.locateCenterOnScreen("slave_factory-empty.png",grayscale=True,confidence=0.8):
        clickimg("slave_factory-empty.png",0.8,0.1)
        sleep(2),slave_factory_vang(),sleep(2)
    if pyautogui.locateCenterOnScreen("slave_trading.png",grayscale=True,confidence=0.8):
        clickimg("slave_trading.png",0.8,0.1)
        sleep(2),slave_trader(),sleep(2)

    darging2(250)
    sleep(0.5)
    toolong()

    darging2(250)
    sleep(0.5)
    if pyautogui.locateCenterOnScreen("office_empty.png",grayscale=True,confidence=0.8):
        x,y = pyautogui.locateCenterOnScreen("office_empty.png",grayscale=True,confidence=0.8)
        x= x +100
        pyautogui.click(x,y)
        sleep(2),slave_off(),sleep(2)
    darging2(200)#Tang 3
    sleep(0.5)
    if pyautogui.locateCenterOnScreen("slave_factory-empty.png",grayscale=True,confidence=0.8):
        clickimg("slave_factory-empty.png",0.8,0.1),sleep(2)
        sleep(2),slave_factory_exp(),sleep(2),
    sleep(2)
    if pyautogui.locateCenterOnScreen("slave_factory-empty.png",grayscale=True,confidence=0.8):
        clickimg("slave_factory-empty.png",0.8,0.1),sleep(2)
        sleep(2),slave_factory_exp(),sleep(2)
    toolong()

def cc(img):
    count = 0
    for slave in pyautogui.locateAllOnScreen(img,grayscale=False , confidence=0.96):
        count= count +1
        print(slave)
    print(count)
    return count

cmd = input()
if cmd == "start":
    startGame()
if cmd == "recruit":
    recruit()
if cmd == "slave_e":
    slave_factory_exp()
if cmd == "slave_g":
    slave_factory_vang()
if cmd == "slave_t":
    slave_trader()
if cmd == "slave_ele":
    slave_eletric()
if cmd == "pb":
    phanbiet_factory()
if cmd == "bot":
    bot(),bot(),done_farm(),done_farm()
if cmd == "farm":
    farm()
if cmd == "base":
    basedaily()
if cmd == "slave_re":
    slave_re()
if cmd == "d_farm":
    done_farm(),done_farm()
if cmd == "countimg":
    tag=input()
    countimg2(tag)


