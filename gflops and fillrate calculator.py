from os import system as cmd
from os import name as osname
from rich.console import Console
from rich.table import Table

console = Console()


def clear():
    cmd("cls" if osname == "nt" else "clear")


while True:
    # Getting the input.
    shader1, tmp1, rop1 = map(int, input('Enter the core config:').split(":"))
    core1 = int(input('Enter the core clock(in MHz):'))
    bit1 = int(input("Enter the bits of the GPU:"))
    memtype1 = str(input("Enter what type of memory you have (GDDR3,GDDR5,HBM etc.):")).lower()
    mem1 = int(input("Enter the memory clock(in MHz) (as reported in GPU-Z, NOT MSI Afterburner):"))
    # The math
    gflops1 = (shader1*core1*2/1000)
    gpixels1 = (core1*rop1/1000)
    gtexels1 = (core1*tmp1/1000)
    if memtype1 == "ddr3" or memtype1 == "gddr3" or memtype1 == "hbm" or memtype1 == "hbm1" or memtype1 == "hbm2":
        gbytes1 = (mem1*bit1/4/1000)
    elif memtype1 == "gddr5":
        gbytes1 = (mem1*bit1/2/1000)
    elif memtype1 == "gddr5x" or memtype1 == "gddr6":
        gbytes1 = (mem1*bit1/1000)
    elif memtype1 == "gddr6x":
        gbytes1 = (mem1*bit1/1000)
    else:
        print("invalid memory type, try again")
        continue
    # The results
    print("The core config is: ", shader1, ":", tmp1, ":", rop1)
    print(f"The memory type is: {memtype1.upper()}\nThe memory clock is: {mem1} MHz\nThe core clock is: {core1} MHz")
    print(gflops1, " GFLOPS")
    print(gpixels1, " Gpixel/s")
    print(gtexels1, " Gtexel/s")
    print(gbytes1, "GB/s")
    print(" ")
    print(" ")
    print("Type 1 to start again, type 2 to compare this card with another one, or type 3 to quit.")
    choice = input()
    if choice == "1":
        clear()
        continue
    elif choice == "2":
        shader2, tmp2, rop2 = map(int, input("Enter the core config (GPU 2):").split(":"))
        core2 = int(input("Enter the core clock(in MHz)(GPU2):"))
        bit2 = int(input("Enter the bits of the GPU (GPU2):"))
        memtype2 = str(input("Enter what type of memory you have (GDDR3,GDDR5,HBM etc.):")).lower()
        mem2 = int(input("Enter the memory clock(in MHz) (as reported in GPU-Z, NOT MSI Afterburner):"))
        gflops2 = (shader2*core2*2/1000)
        gpixels2 = (core2*rop2/1000)
        gtexels2 = (core2*tmp2/1000)
        if memtype2 == "ddr3" or memtype2 == "gddr3" or memtype2 == "hbm" or memtype2 == "hbm1" or memtype2 == "hbm2":
            gbytes2 = (mem2 * bit2 / 4 / 1000)
        elif memtype1 == "gddr5":
            gbytes2 = (mem2 * bit2 / 2 / 1000)
        elif memtype2 == "gddr5x" or memtype2 == "gddr6":
            gbytes2 = (mem2 * bit2 / 1000)
        elif memtype1 == "gddr6x":
            gbytes2 = (mem2 * bit2 / 1000)
        else:
            print("invalid memory type, try again")
            continue
        gflops_diff = ((gflops2 - gflops1) / gflops1)*100
        gpixels_diff = ((gpixels2 - gpixels1) / gpixels1)*100
        gtexels_diff = ((gtexels2 - gtexels1) / gtexels1)*100
        gbytes_diff = ((gbytes2 - gbytes1) / gbytes1)*100
        total_diff = (gflops_diff+gpixels_diff+gtexels_diff+gbytes_diff)/4

        def positive(x):
            x = round(x, 3)
            return f"[green]{x}[/green]"

        def negative(x):
            x = round(x, 3)
            return f"[red]{x}[/red]"

        table = Table(show_header=True, header_style="bold")
        table.add_column("GPU")
        table.add_column("GFLOPS")
        table.add_column("Pixel Fillrate")
        table.add_column("Texture Fillrate")
        table.add_column("Bandwidth")
        table.add_column("Average difference(%)")
        table.add_row("GPU1", f"{gflops1}", f"{gpixels1}", f"{gtexels1}", f"{gbytes1}", "")
        table.add_row("GPU2", f"{gflops2}", f"{gpixels2}", f"{gtexels2}", f"{gbytes2}", "")
        table.add_row("Difference(%)", positive(gflops_diff) if gflops_diff > 0 else negative(gflops_diff), positive(gpixels_diff) if gpixels_diff > 0 else negative(gpixels_diff), positive(gtexels_diff) if gtexels_diff > 0 else negative(gtexels_diff), positive(gbytes_diff) if gbytes_diff > 0 else negative(gbytes_diff), positive(total_diff) if total_diff > 0 else negative(total_diff))
        console.print(table)
        print("Press 1 to start again, type 2 to quit")
        choice2 = input()
        if choice2 == "1":
            continue
        elif choice2 == "2":
            break
        else:
            print("Somethin' ain't right")
            raise TypeError
    elif choice == "3":
        break
