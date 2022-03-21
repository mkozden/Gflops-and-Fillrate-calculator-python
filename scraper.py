import json
from selenium import webdriver
import time
import os


class Scraper:
	def __init__(self):
		self.browser = webdriver.Chrome()
		self.check_file()

	def get_gpus(self):
		self.browser.get("https://www.techpowerup.com/gpu-specs/")
		searchbox = self.browser.find_element_by_id("quicksearch")
		searchbox.send_keys(" ")
		time.sleep(8)
		table = self.browser.find_element_by_css_selector("#ajaxresults > table > tbody")
		items = table.find_elements_by_tag_name("tr")
		items_final = []
		i = 0
		for item in items:
			props = item.find_elements_by_tag_name("td")
			name = props[0].find_element_by_tag_name("a").text
			memory = props[4].text.split(",")
			if len(memory) == 3:
				memorytype = memory[1]
				buswidth = memory[2].split()[0]
			else:
				memorytype = None
				buswidth = None
			coreclk = props[5].text.split()[0]
			memclk = props[6].text.split()[0]
			corecfg = props[7].text.split("/")
			if len(corecfg) == 4:
				corecfg = [int(corecfg[0]) + int(corecfg[1]), int(corecfg[2]), int(corecfg[3])]
			elif len(corecfg) == 3:
				corecfg = [int(corecfg[0]), int(corecfg[1]), int(corecfg[2])]
			else:
				corecfg = None
			itemdict = {"name": name, "cfg": corecfg, "memtype": memorytype, "buswidth": buswidth, "coreclk": coreclk, "memclk": memclk}
			items_final.append(itemdict)
			i += 1
			print(f"{i}/{len(items)}")
		self.cleanup(items_final)

	def check_file(self):
		if os.path.exists("gpu_data.json") and os.path.getsize("gpu_data.json") != 0:
			current_date = time.time()
			if current_date - os.path.getmtime("gpu_data.json") > 31536000:
				print("The file is older than a year, updating")
				self.get_gpus()
			else:
				self.browser.quit()
				itemlist = json.load(open("gpu_data.json", "r"))
				self.cleanup(itemlist)
		else:
			self.get_gpus()

	def cleanup(self, itemlist):
		def dictnonecheck(dictionary):
			for key, value in dictionary.items():
				if key == "memtype":
					if value is None or value.lower().lstrip(" ") not in ["sdr", "ddr", "ddr2", "gddr2", "ddr3", "gddr3", "gddr5", "lpddr5", "gddr5x", "gddr6", "gddr6x", "hbm", "hbm2"]:
						return False
					else:
						return True
		itemlist = [i for i in filter(dictnonecheck, itemlist)]
		cleaned = []
		added = []
		for item in itemlist:
			if item["name"] not in added:
				added.append(item["name"])
				cleaned.append(item)
		self.save_json(cleaned)
		print(f"Saved {len(cleaned)} gpus to file")

	@staticmethod
	def save_json(itemlist, filename="gpu_data.json"):
		with open(filename, "w") as file:
			json.dump(itemlist, file)


scp = Scraper()
