import os
while True:
    # Getting the input.
    shader,tmp,rop = map(int,input('Enter the core config:').split(":"))
    core = int(input('Enter the core clock(in MHz):'))
    bit = int(input("Enter the bits of the GPU:"))
    mem = int(input("Enter the memory clock(in MHz):"))
    #The math
    gflops = (shader*core*2/1000)
    gpixels = (core*rop/1000)
    gtexels = (core*tmp/1000)
    gbytes = (mem*2*bit/4/1000)
    #The results
    print ("The core config is: ",shader,":",tmp,":",rop)
    print ("The memory clock is: ",mem," MHz","  The core clock is: ",core," MHz")
    print (gflops ," GFLOPS")
    print (gpixels ," Gpixel/s")
    print (gtexels ," Gtexel/s")
    print (gbytes,"GB/s")
    print (" ")
    print (" ")
    print ("Type 1 to start again,or type 2 to quit.")
    user_input = input()
    if user_input == "1":
        os.system("cls")
        continue
    elif user_input == "2":
        break
