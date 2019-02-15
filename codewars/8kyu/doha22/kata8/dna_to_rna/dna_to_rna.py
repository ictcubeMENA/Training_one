def DNAtoRNA(dna):
    # create a function which returns an RNA sequence from the given DNA sequence

  res = dna.replace('T','U') 
  return res   

def DNAtoRNA2(dna):
    return "".join(["U" if c=="T" else c for c in dna])