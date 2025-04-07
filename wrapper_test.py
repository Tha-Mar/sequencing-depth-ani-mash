import os 


SRR = "SRR32805580"

#Run script to download SRR fastq files and assemble with SPAdes
os.system(f"python ./scripts/test_SRA.py --input {SRR}")
os.system(f'python ./scripts/test_subsample.py --input {SRR}')
os.system(f'python ./scripts/assembly.py --input {SRR}')
os.system(f'python ./scripts/fastani-mash.py --input {SRR}')
os.system('Rscript ./scripts/visuals.R')
