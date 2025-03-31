import subprocess
import argparse 
import os 
import glob

'''def check_arg(args=None):
    parser = argparse.ArgumentParser(description='SRR for fastANI and Mash')
    parser.add_argument('-i', '--input', help='path to input data',required ='True') #add command line arguement for input file
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input #store input file path

SRR = infile

wget_mash = 'wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar'
tar_mash = 'tar xvf mash-Linux64-v2.3.tar'
'''

SRR = 'SRR32805580'

assemblies = glob.glob('../../sub_assemblies/*/contigs.fasta')
full_assembly = '../spades-out/contigs.fasta'
print(assemblies)

wget_mash = 'wget https://github.com/marbl/Mash/releases/download/v2.3/mash-Linux64-v2.3.tar'
tar_mash = 'tar xvf mash-Linux64-v2.3.tar'

subprocess.run(wget_mash, shell=True)
subprocess.run(tar_mash, shell=True)


mash_path = './mash-Linux64-v2.3/mash'

for assembly in assemblies:
    mash_dist = mash_path+ ' dist ' + assembly + ' ' + full_assembly
    subprocess.run(mash_dist, shell=True)

