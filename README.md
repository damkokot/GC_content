# GC_content
Task within studies' subject 'Genomika porównawcza'

GC content of of nucelic acids (or genomes) points various properties of the specific sequence:
* in polymerase chain reaction (PCR) experiments, GC content of short oligonucleotides known as primers is used to predict oligonucleotides' annealing temperature to the template DNA (higher the GC content indicates higher melting temp.)
* bearing in mind the fact above, it is said that nucleic strands with higher GC content are more stable (more triple hydrogen bonds)
* variation in GC content creates mosaic-like formation called isochores, GC-rich isochores contains protein coding genes thus determination of those regions maps gene-rich sequence
* use to higher-level hierarchical classification in the species problem in non-eukaryotic taxonomy

# Script
Provided scrpit allows to present in graphical way the GC content of the organism's genome.

# Usage

```bash
# Fasta file of Escherichia coli K12 substrain MG1655
python .\gc_content.py files/U00096.3 --step=150 --window=1500

# NCBI ID of Escherichia coli O157:H7 str. Sakai DNA
python .\gc_content.py BA000007.3 --step=1000 --window=4000

```

<html>
<body>
    <div>
        <h4>GC_content plots</h4>
        <p>
            <img src="demo/gc_cont.png" width="100%">
        </p>
        <p>
            <img src="demo/gc_cont1.png" width="100%">
        </p>
    </div>
</body>
</html>
