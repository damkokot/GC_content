import argparse
from Bio import SeqIO, Entrez
from Bio.SeqUtils import GC
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt


class ContentGC():
    """
    Calculating GC content in genome sequence
    of various organisms. The information
    will be displayed via graphical presentation.
    """

    def __init__(self, sequence: str, step: int, window: int):
        """

        :param sequence: fasta file name or organism's NCBI ID
        :param step: starting nucleotide index for each GC content computation
        :param window: size of computing spectrum
        """
        self.sequence = sequence
        self.step = step
        self.window = window

    def get_file(self):
        """
        Downloading fasta file from NCBI database
        or reading fasta file from local directory.

        :return: fasta file from NCBI database or fasta file from local destination
        """
        file_name = f'{self.sequence}.fasta'

        if Path(file_name).exists():
            return file_name

        Entrez.email = 'A.N.Other@example.com'
        handle = Entrez.efetch(db='nucleotide', id=self.sequence, rettype='fasta', retmode='txt')
        rec = handle.read()
        with open(file_name,'w') as f:
            f.write(rec)

        return file_name

    def file_content(self):

        """
        Checks if file is in directory and takes out the sequence via parsing.
        :return: genome seqeunce of an organism
        """

        if not Path(self.get_file()).exists():
            print('ERROR : no such file ')

        seq = [record.seq for record in SeqIO.parse(self.get_file(), 'fasta')][0]
        return seq

    def computing(self):
        '''
        Computing GC content for selected organism's genome seqeunce.

        :return: List that contains gc content for each window size
        '''
        gc_cont = []
        start_position = 0
        content = self.file_content()
        while (start_position+self.window) < len(content):
            gc_cont_window = content[start_position:start_position+self.window]
            compute = GC(gc_cont_window)
            gc_cont.append(compute)
            start_position += self.step

        return gc_cont

    def plot_content(self):
        '''

        :return: Lineplot representing GC content in percentage values.
        '''

        sns.set(rc={"figure.figsize": (20, 10)})
        sns.lineplot(data=self.computing()).set(title="GC content of the organism")
        plt.xlabel('Step')
        plt.ylabel('Percentage')
        plt.savefig('files/gc_cont')
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Computing organism's genome GC content")
    parser.add_argument('sequence', type=str, help='provide fasta file name of the genome or its NCBI ID')
    parser.add_argument('-st', '--step', type=int, default=20, help='window range')
    parser.add_argument('-w', '--window', type=int, default=1000, help='calculation start step')
    args = parser.parse_args()
    gc = ContentGC(args.sequence,args.step,args.window)
    gc.plot_content()



