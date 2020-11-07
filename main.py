import sys,random,time,os


playing = True
money = 100
fishCaught = 0
fishingLicense=False
rod=False
ack = False
firstTime = os.path.isfile('c.txt')

if firstTime == False:
    print('Well hello there, fisherman, I see this is your first time playing!')
    print('Would you like a short tutorial to start you off?')
    tutorial = input()
    #add tutorial code later

else:
    print('Welcome back, fisherman, do you want to continue your old save?')
    #add saving code here

loc = input('Where would you like to start, Homer (Kodiak Region), or the Kvichak River (Bristol Bay Region)? ')

if loc.lower() == 'homer' or loc.lower() == 'kodiak':
    loc = 'Homer, Kodiak Region'
    print('\nYou will start in Homer, Kodiak Region.\n')
elif loc.lower() == 'kvichak river' or loc.lower() == 'bristol bay':
    loc = 'Kvichak River, Bristol Bay Region'
    print('\nYou will start near the Kvichak River, Bristol Bay Region.\n')
else:
    print('Unknown starting location, please rerun the program.')

while playing:
    print('Money: ',money)
    print('Fish Caught: ',fishCaught)
    print('Location: ',loc)
    main = input('\nWhat would you like to do? ')


    if not fishingLicense:
        if ack ==True:
            pass
        else:
            print('You do not have a fishing license, you are not allowed to fish here without one. Do you want to buy one, or risk getting fined by the police? ')
            risk = input()
            if risk.lower() == 'risk' or risk.lower() == 'fine':
                print('Okay, take this as your formal warning.')
                ack = True
            elif risk.lower() == 'buy':
                print('You spend $25 on a fishing license for 20 turns.')
                money =-25
                fishingLicense=True
            else:
                print('Unknown, please try again.')

    if not rod:
        print('\n\nYour grandfather approaches you,')
        time.sleep(1)
        print('he used to be a fisherman,')
        time.sleep(2)
        print('but retired when he got into an accident in Adak.')
        time.sleep(4)
        print('He hands you his old fishing rod,')
        time.sleep(2)
        print('I\'ts a bit old but it\'ll do the job until you can afford a brand new one.\n\n')
        time.sleep(3)
