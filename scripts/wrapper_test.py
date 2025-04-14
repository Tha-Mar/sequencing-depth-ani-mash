
import os 

os.chdir("./scripts")

os.system(f"python test-fastani-mash.py")
os.system(f"Rscript test-visuals.R")