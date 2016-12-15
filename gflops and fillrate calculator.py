from tabulate import tabulate
from os import system as cmd
while True:
    # Getting the input.
    shader1,tmp1,rop1 = map(int,input('Enter the core config:').split(":"))
    core1 = int(input('Enter the core clock(in MHz):'))
    bit1 = int(input("Enter the bits of the GPU:"))
    mem1 = int(input("Enter the memory clock(in MHz)(card must be GDDR5 or DDR3):"))
    #The math
    gflops1 = (shader1*core1*2/1000)
    gpixels1 = (core1*rop1/1000)
    gtexels1 = (core1*tmp1/1000)
    gbytes1 = (mem1*2*bit1/4/1000)
    #The results
    print ("The core config is: ",shader1,":",tmp1,":",rop1)
    print ("The memory clock is: ",mem1," MHz","  The core clock is: ",core1," MHz")
    print (gflops1 ," GFLOPS")
    print (gpixels1 ," Gpixel/s")
    print (gtexels1 ," Gtexel/s")
    print (gbytes1 ,"GB/s")
    print (" ")
    print (" ")
    print ("Type 1 to start again, type 2 to caompare this card with another one, or type 3 to quit.")
    choice = input()
    if choice == "1":
        cmd("cls")
        continue
    elif choice == "2":
        shader2,tmp2,rop2 = map(int,input("Enter the core config (GPU 2):").split(":"))
        core2 = int(input("Enter the core clock(in MHz)(GPU2):"))
        bit2 = int(input("Enter the bits of the GPU (GPU2):"))
        mem2 = int(input("Enter the memory clock(in MHz)(card must be GDDR5 or DDR3) (GPU2):"))
        gflops2 = (shader2*core2*2/1000)
        gpixels2 = (core2*rop2/1000)
        gtexels2 = (core2*tmp2/1000)
        gbytes2 = (mem2*2*bit2/4/1000)
        table =[["  ","GPU1","GPU2","Difference"],["GFLOPS",gflops1,gflops2,gflops1-gflops2],["Gpixel/s",gpixels1,gpixels2,gpixels1-gpixels2],["Gtexel/s",gtexels1,gtexels2,gtexels1-gtexels2],["GB/s",gbytes1,gbytes2,gbytes1-gbytes2]]
        print(tabulate(table))
        print(" ")
        choice
    elif choice == "3":
        break
