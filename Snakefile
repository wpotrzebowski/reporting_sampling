datasets:
  10.5281/zenodo.6645201:
    contents:
      Practical6_Ni_simple-chain.mc.gz: src/data/Practical6_Ni_simple-chain.mc.gz
      Practical6_Ni_simple-point.mc.gz: src/data/Practical6_Ni_simple-point.mc.gz
      Practical6_Ni_simple-stats.mc.gz: src/data/Practical6_Ni_simple-stats.mc.gz

rule compute_post:
    input:
        "src/data/Practical6_Ni_simple-chain.mc.gz",
        "src/data/Practical6_Ni_simple-point.mc.gz",
        "src/data/Practical6_Ni_simple-stats.mc.gz"
    output:
        "src/tex/output/mag_sld.txt",
        "src/tex/output/density.txt",
        "src/tex/output/thick.txt",
        "src/tex/figures/post.pdf"
    script:
        "src/scripts/post.py"