# Getting the input.
shader = input('Enter the number of shader processors:')
tmp = input('Enter the amount of TMPs:')
rop = input('Enter the amount of ROPs:')
core = input('Enter the core clock(in MHz):')
#Something that has to be done in order to make this work.
shader = int(shader)
core = int(core)
tmp = int(tmp)
rop = int(rop)
#The math
gflops = ((shader*core*2)/1000)
gpixels = ((core*rop)/1000)
gtexels = ((core*tmp)/1000)
#The results
print (str(gflops) + " GFLOPS")
print (str(gpixels) + " Gpixel/s")
print (str(gtexels) + " Gtexel/s")
print (" ")
print ("press ENTER to exit")
input()
