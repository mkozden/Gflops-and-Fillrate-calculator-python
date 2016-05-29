# Getting the input.
shader = int(input('Enter the number of shader processors:'))
tmp = int(input('Enter the amount of TMPs:'))
rop = int(input('Enter the amount of ROPs:'))
core = int(input('Enter the core clock(in MHz):'))
#The math
gflops = (shader*core*2/1000)
gpixels = (core*rop/1000)
gtexels = (core*tmp/1000)
#The results
print (gflops ," GFLOPS")
print (gpixels ," Gpixel/s")
print (gtexels ," Gtexel/s")
print (" ")
print ("press ENTER to exit")
input()