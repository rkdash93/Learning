
import random
from speak import *

def paheli():
    p_list = ['Din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye', 
    'Ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray',
    'Aisa likhiye sabd banaaye, phal, phool, aur mithai bun jaaye']
    sel_p = random.choice(p_list)
    print(sel_p)
    speak(sel_p)
    par1,par2,task_paheli = task('paheli')
    #task_paheli = input('Enter answer:')

    if sel_p == 'Din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye' and (task_paheli.lower() =='mombatti' or task_paheli =='candle'):
        speak('sahi jawaab')
        print('sahi jawaab')
    elif sel_p == 'Ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray' and (task_paheli.lower() == 'aasman' or task_paheli == 'akash'):
        speak('sahi jawaab')
        print('sahi jawaab')
    elif sel_p == 'Aisa likhiye sabd banaaye, phal, phool, aur mithai bun jaaye' and task_paheli.lower() == 'gulab jamun':    
        speak('sahi jawaab')
        print('sahi jawaab')
    else:
        speak('galat jawaab')
        print('galat jawab')    
