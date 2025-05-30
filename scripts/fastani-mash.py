import subprocess
import argparse 
import os 
import glob
import sys

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='SRR for fastANI and Mash')
    parser.add_argument('-i', '--input', help='path to input data',required ='True') #add command line arguement for input file
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input #store input file path

SRR = infile

#get all sub assembly file paths
assemblies = glob.glob('../sub_assemblies-'+SRR+'/*/contigs.fasta') 
#path for full assembly
full_assembly = '../spades-out-'+SRR+'/contigs.fasta'

#downloads mash if not already downloaded
if not os.path.exists('./mash-Linux64-v2.3/mash'):
    wget_mash = 'wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar'
    tar_mash = 'tar xvf mash-Linux64-v2.3.tar'
    
    subprocess.run(wget_mash, shell=True)
    subprocess.run(tar_mash, shell=True)

#creates directory for mash and fastani results
os.makedirs('../fastani-mash-data-'+SRR, exist_ok=True)
mash_path = './mash-Linux64-v2.3/mash'

#clears the file of old data
open("../fastani-mash-data-"+SRR+"/compiled_mash_distances.tab", "w").close() 

#runs mash for each sub assembly
mash_count = 0
for assembly in assemblies:
    mash_dist = mash_path+ ' dist ' + assembly + ' ' + full_assembly + ' > ../fastani-mash-data-'+SRR+'/temp_mash_distances.tab'
    subprocess.run(mash_dist, shell=True)
    with open ('../fastani-mash-data-'+SRR+'/temp_mash_distances.tab', 'r') as temp_data:
        input = temp_data.readline()
    if input:
        mash_count += 1
        with open ('../fastani-mash-data-'+SRR+'/compiled_mash_distances.tab','a') as output:
            output.write(input + '\n')

#removes the temporary file
os.remove('../fastani-mash-data-'+SRR+'/temp_mash_distances.tab')

#clears the file of old data
open("../fastani-mash-data-"+SRR+"/fastani_results.tab", "w").close()

#runs fastani for each sub assembly
fastani_count = 0
for assembly in assemblies:
    fastani_cmd = 'fastANI -q ' + assembly + ' -r ' + full_assembly + ' -o ../fastani-mash-data-'+SRR+'/temp_fastani.tab'
    subprocess.run(fastani_cmd, shell=True)
    
    if os.path.getsize('../fastani-mash-data-'+SRR+'/temp_fastani.tab') > 0:
        with open('../fastani-mash-data-'+SRR+'/temp_fastani.tab', 'r') as temp_file:
            result = temp_file.readline()
        if result:
            fastani_count += 1
            with open('../fastani-mash-data-'+SRR+'/fastani_results.tab', 'a') as output:
                output.write(result + '\n')

#removes the temporary file
os.remove('../fastani-mash-data-'+SRR+'/temp_fastani.tab')



 


