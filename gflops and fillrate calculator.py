shader = input('Enter the number of shader processors:')
tmp = input('Enter the amount of TMPs:')
rop = input('Enter the amount of ROPs:')
core = input('Enter the core clock(in MHz):')
shader = int(shader)
core = int(core)
tmp = int(tmp)
rop = int(rop)
gflops = ((shader*core*2)/1000)
gpixels = ((core*rop)/1000)
gtexels = ((core*tmp)/1000)
print (str(gflops) + " GFLOPS")
print (str(gpixels) + " Gpixel/s")
print (str(gtexels) + " Gtexel/s")
print (" ")
print ("press ENTER to exit")
input()
