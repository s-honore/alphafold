from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


# Opdater protein sekvens
original_sequence = """
MEPPLPVGAQPLATVEGMEMKGPLREPCALTLAQRNGQYELIIQLHEKEQHVQDIIPINSHFRCVQEAEETLLIDIASNSGCKIRVQGDWIRERRFEIPDEEHCLKFLSAVLAAQKAQSQLLVPEQKDSSSWYQKLDTKDKPSVFSGLLGFEDNFSSMNLDKKINSQNQPTGIHREPPPPPFSVNKMLPREKEASNKEQPKVTNTMRKLFVPNTQSGQREGLIKHILAKREKEYVNIQTFRFFVGTWNVNGQSPDSGLEPWLNCDPNPPDIYCIGFQELDLSTEAFFYFESVKEQEWSMAVERGLHSKAKYKKVQLVRLVGMMLLIFARKDQCRYIRDIATETVGTGIMGKMGNKGGVAVRFVFHNTTFCIVNSHLAAHVEDFERRNQDYKDICARMSFVVPNQTLPQLNIMKHEVVIWLGDLNYRLCMPDANEVKSLINKKDLQRLLKFDQLNIQRTQKKAFVDFNEGEIKFIPTYKYDSKTDRWDSSGKCRVPAWCDRILWRGTNVNQLNYRSHMELKTSDHKPVSALFHIGVKVVDERRYRKVFEDSVRIMDRMENDFLPSLELSRREFVFENVKFRQLQKEKFQISNNGQVPCHFSFIPKLNDSQYCKPWLRAEPFEGYLEPNETVDISLDVYVSKDSVTILNSGEDKIEDILVLHLDRGKDYFLTISGNYLPSCFGTSLEALCRMKRPIREVPVTKLIDLEEDSFLEKEKSLLQMVPLDEGASERPLQVPKEIWLLVDHLFKYACHQEDLFQTPGMQEELQQIIDCLDTSIPETIPGSNHSVAEALLIFLEALPEPVICYELYQRCLDSAYDPRICRQVISQLPRCHRNVFRYLMAFLRELLKFSEYNSVNANMIATLFTSLLLRPPPNLMARQTPSDRQRAIQFLLGFLLGSEED
""".replace('\n', '').replace(' ', '')  # Remove newlines and spaces

# Kontrol af sekvenslængde
assert len(original_sequence) == 901, "Length of the original sequence does not match expected value."


# Define the mutation position (451) and the new amino acid (Asparagine, N)
mutation_position = 451 - 1  # Adjust for zero-based indexing
mutated_amino_acid = 'N'

# Introduce the mutation
mutated_sequence = (original_sequence[:mutation_position] +
                    mutated_amino_acid +
                    original_sequence[mutation_position + 1:])
# VERIFY MUTATION
assert mutated_sequence[mutation_position] == mutated_amino_acid, "Mutation was not introduced correctly."


mutated_record = SeqRecord(Seq(mutated_sequence),
                           id="OCRL_mutated", name="OCRL_mutated",
                           description="OCRL protein with Asp451Asn mutation")

# Write the mutated sequence to a FASTA file
fasta_filename = "ocrl_mutated.fasta"
with open(fasta_filename, "w") as output_handle:
    SeqIO.write(mutated_record, output_handle, "fasta")

print(f"Mutated sequence written to {fasta_filename}")