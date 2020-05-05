# Water filtration plantation - Sys-20581-WD1-Main-Controller
# W4trF4-ci1Main \ SlashDN - on ALERT! CALL - 1002930229300420
# Last update - 24.03.2020

lawEnforcementUpdate = "MUST READ! - Due to concerns regarding an upcoming water crisis, \n the prices are to be raised from 12Nok for every 1000Liters(m^3) to 25Nok, a 210% increase \nstarting from the next month and going forwards, the daily legal amount of water per person daily will be set at 20Liters, due to the severity of the situation, \n those who happen overstep these boundaries will have to pay a fine of 1250 Nok pr/liter \n "
import time
import random

#Access level
#System class
class waterTreatmentFacilitySystem:
    def __init__(self, currentWaterAvailability, waterQuality, currentPopulation , pricePrLiter, currentLegalWaterAmount):
        #Water availability in Liter
        self.currentWaterAvailability = currentWaterAvailability

        #Water quality scale 1-10
        self.waterQuality = waterQuality

        #population for X county
        self.currentPopulation = currentPopulation

        # Price of water pr person by the liter
        self.pricePrLiter = pricePrLiter

        # Daily legal amount of water pr person
        self.currentLegalWaterAmount = currentLegalWaterAmount

#Construction 
centralSystemOslo = waterTreatmentFacilitySystem(89234072308942235324, 6, 693494, 25, 20)
dailyWaterUsageLiterPrPerson = 197

def dailyWaterQuotaPrice():
    dailyPrice = centralSystemOslo.pricePrLiter*centralSystemOslo.currentLegalWaterAmount
    print(dailyPrice)


#checkSystem
continueCheckPrompt = True

#Realistic simulation functions
def logOut():
    print("logging out. . .")
    time.sleep(2)
    print("Bye!")
    exit()

def checkWaterAvailability():
    print("\n The | VannSkli Oslo water purification and treatment plant  | currently has ",centralSystemOslo.currentWaterAvailability, " Liter available for distrubution\n")
    
def checkWaterQuality():
    print("\n From last checkup -| 19.04.2020 |- \n | Current Ph levels: 6.2 - Expected to reach 5.7 by 05.05.2020 due to increase in Co2 level| \n |  Color: Clean, slight mist has formed  due to the change in turbidity | \n | Microbiology - No  danger - Normal bacterial growth | \n | Turbidity: Subtle increase in tubidity: PET and PVC to be the cause. | \n overall score - ", centralSystemOslo.waterQuality)

def checkCountyPopulation():
    print("\n | Population in Oslo: ", centralSystemOslo.currentPopulation, " People | \n | Due to the increase in droughts around the country, VannSkli and all other major water purification plants must aid eachother with supplying drinkable water to the population in these upcoming dire times. \n")

def checkWaterPrice():
    print("\n | Current water price: ", centralSystemOslo.pricePrLiter, " Nok pr/liter | \n Price of the daily water-quota = ", dailyWaterQuotaPrice())

#Main control
def systemMain():
    print(lawEnforcementUpdate)
    while continueCheckPrompt:
         desiredCheck = input("\n What would you like to check? \n [WaterAvailability] [WaterQuality] [CountyPopulation] [WaterPrice] [Q] to quit: ")
         if desiredCheck == "WaterAvailability":          
            checkWaterAvailability()

         elif desiredCheck =="WaterQuality":
            checkWaterQuality()
           
         elif desiredCheck == "CountyPopulation":            
            checkCountyPopulation()

         elif desiredCheck == "WaterPrice":
            checkWaterPrice()

         elif desiredCheck == "Q":
            logOut()
         
         else: print("\n Your input |", desiredCheck, " | is not an valid option. Try again. \n")

#Simulates connecting to a server
simulationServers =["192.168.1.200", "192.168.1.254", "192.168.0.1", "192.168.123.254", "192.168.1.1"]
def serverEmulationConnect():
    print("Fetching connections. . . ")
    time.sleep(1)

    for i in simulationServers:
        print("Attempting connection -->", i)
        time.sleep(2)

# security check simulation  and immersion
def realisticEmulationWait():
        print("Wait")
        for i in range(3):
            emulationSleepTime = random.randint(1,3)
            time.sleep(emulationSleepTime)
            print("Working. . . wait")

#Asks for login&pass
def adminPrompt():
        name = input("Name: ")
        pswd = input("Pswd: ")
        checkValidClearance(name, pswd)

#Checks credentials
def checkValidClearance(idField, pswdField):
    if idField == "KeithyKeith" and pswdField == "HorseBatteryStaple":
        realisticEmulationWait()
        serverEmulationConnect()
        print("Welcome!")
    else:
        print("Access denied")
        exit()

adminPrompt()
systemMain()
