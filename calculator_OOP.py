"""
TODO:
Future plan: Move to a graphical user interface
"""
from rich.console import Console
from rich.table import Table

console = Console()


class GPU:
	def __init__(self, core_cfg, core_clk, mem_type, bus_width, mem_clk):
		self.core_cfg = str(core_cfg)
		self.core_clk = int(core_clk)
		self.mem_type = str(mem_type)
		self.bus_width = int(bus_width)
		self.mem_clk = int(mem_clk)
		self.shader, self.tmu, self.rop = map(int, self.core_cfg.split(":"))

	def gflops(self):
		return self.shader * self.core_clk * 2 / 1000

	def gpixels(self):
		return self.rop * self.core_clk / 1000

	def gtexels(self):
		return self.tmu * self.core_clk / 1000

	def gbytes(self):
		if self.mem_type == "ddr3" or self.mem_type == "gddr3" or self.mem_type == "hbm" or self.mem_type == "hbm1" or\
				self.mem_type == "hbm2":
			return self.mem_clk * self.bus_width / 4 / 1000
		elif self.mem_type == "gddr5":
			return self.mem_clk * self.bus_width / 2 / 1000
		elif self.mem_type == "gddr5x" or self.mem_type == "gddr6":
			return self.mem_clk * self.bus_width / 1000
		elif self.mem_type == "gddr6x":
			return self.mem_clk * self.bus_width * 2 / 1000
		else:
			print("invalid memory type, try again")
			raise TypeError


def clrdff(a, b):
	a, b = float(a), float(b)
	diff = ((b-a)/a)*100
	diff = round(diff, 3)
	if diff > 0:
		return f"[green]+{diff}[/green]"
	elif diff < 0:
		return f"[red]{diff}[/red]"
	else:
		return f"{diff}"


def clr(x):
	if x > 0:
		return f"[green]+{x}[/green]"
	elif x < 0:
		return f"[red]{x}[/red]"
	else:
		return f"{x}"


gpus = []
straight_to_exit = None

while True:
	core = input("Enter core config:")
	coreclk = int(input("Enter core clock (in MHz):"))
	bus = int(input("Enter bus width:"))
	memtype = str(input("Enter what type of memory you have (GDDR3,GDDR5,HBM etc.):")).lower()
	memclk = int(input("Enter the memory clock(in MHz) (as reported in GPU-Z, NOT MSI Afterburner):"))
	gpu = GPU(core, coreclk, memtype, bus, memclk)
	gpus.append(gpu)
	choice = input("Press 1 to add another GPU\nPress 2 to go to results\nAny other key to exit without results\n")
	if choice == "1":
		continue
	elif choice == "2":
		straight_to_exit = False
		break
	else:
		straight_to_exit = True
		break

if not straight_to_exit:
	table = Table(show_header=True, header_style="bold")
	table.add_column("GPU")
	table.add_column("GFLOPS")
	table.add_column("Pixel Fillrate (GPixel/s)")
	table.add_column("Texture Fillrate (GTexel/s")
	table.add_column("Bandwidth (GB/s)")
	table.add_column("Average difference(%)", justify="center")
	for index, gpu in enumerate(gpus):
		if len(gpus) > 1:
			if index == 0:
				table.add_row(f"GPU{index+1}", f"{gpu.gflops()}", f"{gpu.gpixels()}", f"{gpu.gtexels()}", f"{gpu.gbytes()}", "")
				first_gpu = gpu
			else:
				table.add_row(f"GPU{index + 1}",
				              f"{gpu.gflops()}    "+clrdff(first_gpu.gflops(), gpu.gflops()),
				              f"{gpu.gpixels()}    "+clrdff(first_gpu.gpixels(), gpu.gpixels()),
				              f"{gpu.gtexels()}    "+clrdff(first_gpu.gtexels(), gpu.gtexels()),
				              f"{gpu.gbytes()}    "+clrdff(first_gpu.gbytes(), gpu.gbytes()),
				              ""+(clr(round(((float(clrdff(first_gpu.gflops(), gpu.gflops()).strip("f[]redgrn/+"))+
				                      float(clrdff(first_gpu.gpixels(), gpu.gpixels()).strip("f[]redgrn/+"))+
				                      float(clrdff(first_gpu.gtexels(), gpu.gtexels()).strip("f[]redgrn/+"))+
				                      float(clrdff(first_gpu.gbytes(), gpu.gbytes()).strip("f[]redgrn/+")))/4), 3))))
		if len(gpus) == 1:
			table.add_row(f"GPU{index + 1}", f"{gpu.gflops()}", f"{gpu.gpixels()}", f"{gpu.gtexels()}", f"{gpu.gbytes()}", "")
	console.print(table)
	input("Press any key to exit")
