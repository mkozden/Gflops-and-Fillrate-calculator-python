from tabulate import tabulate
from os import system as cmd
import os , time
def clear():
    cmd("cls" if os.name == "nt" else "clear")
while True:
    # Getting the input.
    shader1,tmp1,rop1 = map(int,input('Enter the core config:').split(":"))
    core1 = int(input('Enter the core clock(in MHz):'))
    bit1 = int(input("Enter the bits of the GPU:"))
    memtype1 = str(input("Enter what type of memory you have (GDDR3,GDDR5,HBM etc.):")).lower()
    if memtype1 == "gddr5" or memtype1 =="gddr5x":
        mem1 = int(input("Enter memory transfer speed(in MT/s):"))
    else:
        mem1 = int(input("Enter the memory clock(in MHz):"))
    #The math
    gflops1 = (shader1*core1*2/1000)
    gpixels1 = (core1*rop1/1000)
    gtexels1 = (core1*tmp1/1000)
    if memtype1 == "ddr3" or memtype1 == "gddr3" or memtype1 == "hbm" or memtype1 == "hbm1" or memtype1 == "hbm2":
        gbytes1 = (mem1*bit1*2/8/1000)
    elif memtype1 == "gddr5" or memtype1 == "gddr5x":
        gbytes1 = (mem1*bit1/8/1000)
    #The results
    print ("The core config is: ",shader1,":",tmp1,":",rop1)
    print ("The memory type is:",memtype1.upper(),"The memory clock is: ",mem1," MHz","  The core clock is: ",core1," MHz")
    print (gflops1 ," GFLOPS")
    print (gpixels1 ," Gpixel/s")
    print (gtexels1 ," Gtexel/s")
    print (gbytes1 ,"GB/s")
    print (" ")
    print (" ")
    print ("Type 1 to start again, type 2 to compare this card with another one, or type 3 to quit.")
    choice = input()
    if choice == "1":
        clear()
        continue
    elif choice == "2":
        shader2,tmp2,rop2 = map(int,input("Enter the core config (GPU 2):").split(":"))
        core2 = int(input("Enter the core clock(in MHz)(GPU2):"))
        bit2 = int(input("Enter the bits of the GPU (GPU2):"))
        memtype2 = str(input("Enter what type of memory you have (GDDR3,GDDR5,HBM etc.):")).lower()
        if memtype2 == "gddr5" or memtype2 == "gddr5x":
            mem2 = int(input("Enter memory transfer speed(in MT/s):"))
        else:
            mem2 = int(input("Enter the memory clock(in MHz):"))
        gflops2 = (shader2*core2*2/1000)
        gpixels2 = (core2*rop2/1000)
        gtexels2 = (core2*tmp2/1000)
        if memtype2 == "ddr3" or memtype2 == "gddr3" or memtype2 == "hbm" or memtype2 == "hbm1" or memtype2 == "hbm2":
            gbytes2 = (mem2 * bit2 * 2 / 8 / 1000)
        elif memtype2 == "gddr5" or memtype2 == "gddr5x":
            gbytes2 = (mem2 * bit2 / 8 / 1000)
        table=[[" ","GPU1","GPU2","Difference(%)"],["GFLOPS",gflops1,gflops2,(gflops1-gflops2)/gflops2*100],["Gpixel/s",gpixels1,gpixels2,(gpixels1-gpixels2)/gpixels2*100],["Gtexel/s",gtexels1,gtexels2,(gtexels1-gtexels2)/gtexels2*100],["GB/s",gbytes1,gbytes2,(gbytes1-gbytes2)/gbytes2*100],["Average Diff.","-","-",(((gflops1-gflops2)/gflops2*100)+((gtexels1-gtexels2)/gtexels2*100)+((gpixels1-gpixels2)/gpixels2*100)+((gbytes1-gbytes2)/gbytes2*100))/4]]
        print(tabulate(table))
        time.sleep(3)
        print("Press 1 to start again, type 2 to quit")
        choice2 = input()
        if choice2 == "1":
            continue
        elif choice2 == "2":
            break
        else:
            print("Somethin' ain't right")
            raise TypeError
        break
    elif choice == "3":
        break
        quit()
