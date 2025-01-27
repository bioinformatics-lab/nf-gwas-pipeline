#!/usr/bin/env python

if __name__ == '__main__':
    import subprocess
    import os
    
    print('Initializing paths...')
    path = os.path.realpath(__file__)
    path = '/'.join(path.split('/')[:-2])

    print('Initializing config...')
    with open('{0}/temp.config'.format(path), 'w') as outfile:
        with open('{0}/gwas.config'.format(path), 'r') as infile:
            for line in infile:
                if line.lstrip().startswith('indir'):
                    outfile.write('  indir  = "{0}/data"\n'.format(path))
                elif line.lstrip().startswith('outdir'): 
                    outfile.write('  outdir = "{0}/results"\n'.format(path))
                else:
                    outfile.write(line)

    subprocess.call(['rm', '-rf', '{0}/gwas.config'.format(path)])
    subprocess.call(['mv', '{0}/temp.config'.format(path),
                           '{0}/gwas.config'.format(path)])

    with open('{0}/configs/temp.config'.format(path), 'w') as outfile:
        with open('{0}/configs/gwas_1KG_logistic.config'.format(path), 'r') as infile:
            for line in infile:
                if line.lstrip().startswith('indir'):
                    outfile.write('  indir  = "{0}/data"\n'.format(path))
                elif line.lstrip().startswith('outdir'): 
                    outfile.write('  outdir = "{0}/result-gwas-1KG-logistic"\n'.format(path))
                else:
                    outfile.write(line)

    subprocess.call(['rm', '-rf', '{0}/configs/gwas_1KG_logistic.config'.format(path)])
    subprocess.call(['mv', '{0}/configs/temp.config'.format(path),
                           '{0}/configs/gwas_1KG_logistic.config'.format(path)])

    with open('{0}/configs/temp.config'.format(path), 'w') as outfile:
        with open('{0}/configs/gene_1KG_linear.config'.format(path), 'r') as infile:
            for line in infile:
                if line.lstrip().startswith('indir'):
                    outfile.write('  indir  = "{0}/data"\n'.format(path))
                elif line.lstrip().startswith('outdir'): 
                    outfile.write('  outdir = "{0}/result-gene-1KG-linear"\n'.format(path))
                else:
                    outfile.write(line)

    subprocess.call(['rm', '-rf', '{0}/configs/gene_1KG_linear.config'.format(path)])
    subprocess.call(['mv', '{0}/configs/temp.config'.format(path),
                           '{0}/configs/gene_1KG_linear.config'.format(path)])

    with open('{0}/configs/temp.config'.format(path), 'w') as outfile:
        with open('{0}/configs/gwla_1KG_linear_slope.config'.format(path), 'r') as infile:
            for line in infile:
                if line.lstrip().startswith('indir'):
                    outfile.write('  indir  = "{0}/data"\n'.format(path))
                elif line.lstrip().startswith('outdir'): 
                    outfile.write('  outdir = "{0}/result-gwla-1KG-linear-slope"\n'.format(path))
                else:
                    outfile.write(line)

    subprocess.call(['rm', '-rf', '{0}/configs/gwla_1KG_linear_slope.config'.format(path)])
    subprocess.call(['mv', '{0}/configs/temp.config'.format(path),
                           '{0}/configs/gwla_1KG_linear_slope.config'.format(path)])

    print('Initializing nf...')
    with open('{0}/temp.nf'.format(path), 'w') as outfile:
        with open('{0}/gwas.nf'.format(path), 'r') as infile:
            for line in infile:
                    outfile.write(line.replace("$PWD", "{0}".format(path)))

    subprocess.call(['rm', '-rf', '{0}/gwas.nf'.format(path)])
    subprocess.call(['mv', '{0}/temp.nf'.format(path),
                           '{0}/gwas.nf'.format(path)])

    print('Initializing test data...')
    with open('{0}/data/toy_vcf.csv'.format(path), 'w') as outfile:
        for i in range(1, 23):
            outfile.write("chr_{0},{1}/data/vcf/vcf_file{0}.vcf.gz\n".format(i, path))

    with open('{0}/data/1KG_vcf.csv'.format(path), 'w') as outfile:
        for i in range(1, 23):
            outfile.write("chr_{0},{1}/data/1KG_vcf/1KG_phase3_subset_chr{0}.vcf.gz\n".format(i, path))

    print('Success!')
    print('Pipeline Directory : {0}'.format(path))
