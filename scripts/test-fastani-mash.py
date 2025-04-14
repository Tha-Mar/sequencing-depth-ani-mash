import subprocess
import argparse 
import glob
import os


#get all sub assembly file paths
assemblies = glob.glob('../test_data/SRR32805580_*_*_contigs.fasta') 
#path for full assembly
full_assembly = '../test_data/full_cov_contigs.fasta'

#downloads mash if not already downloaded
if not os.path.exists('./mash-Linux64-v2.3/mash'):
    wget_mash = 'wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar'
    tar_mash = 'tar xvf mash-Linux64-v2.3.tar'
    
    subprocess.run(wget_mash, shell=True)
    subprocess.run(tar_mash, shell=True)

#creates directory for mash and fastani results
os.makedirs('../test-fastani-mash-data', exist_ok=True)
mash_path = './mash-Linux64-v2.3/mash'

#clears the file of old data
open("../test-fastani-mash-data/compiled_mash_distances.tab", "w").close() 

#runs mash for each sub assembly
for assembly in assemblies:
    mash_dist = mash_path+ ' dist ' + assembly + ' ' + full_assembly + ' > ../test-fastani-mash-data/temp_mash_distances.tab'
    subprocess.run(mash_dist, shell=True)
    with open ('../test-fastani-mash-data/temp_mash_distances.tab', 'r') as temp_data:
        input = temp_data.readline()
    with open ('../test-fastani-mash-data/compiled_mash_distances.tab','a') as output:
        output.write(input + '\n')

#removes the temporary file
os.remove('../test-fastani-mash-data/temp_mash_distances.tab')

#clears the file of old data
open("../test-fastani-mash-data/fastani_results.tab", "w").close()

#runs fastani for each sub assembly
for assembly in assemblies:
    fastani_cmd = 'fastANI -q ' + assembly + ' -r ' + full_assembly + ' -o ../test-fastani-mash-data/temp_fastani.tab'
    subprocess.run(fastani_cmd, shell=True)
    
    with open('../test-fastani-mash-data/temp_fastani.tab', 'r') as temp_file:
            result = temp_file.readline()
    with open('../test-fastani-mash-data/fastani_results.tab', 'a') as output:
            output.write(result + '\n')

#removes the temporary file
os.remove('../test-fastani-mash-data/temp_fastani.tab')



 


