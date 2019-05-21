import os

l = ["TOC.html",
"acknowledgements.html",
"notation.html",
"intro.html",
"part_basics.html",
"linear_algebra.html",
"prob.html",
"numerical.html",
"ml.html",
"part_practical.html",
"mlp.html",
"regularization.html",
"optimization.html",
"convnets.html",
"rnn.html",
"guidelines.html",
"applications.html",
"part_research.html",
"linear_factors.html",
"autoencoders.html",
"representation.html",
"graphical_models.html",
"monte_carlo.html",
"partition.html",
"inference.html",
"generative_models.html",
"bib.html",
"index-.html"]

n = '{num:02d}'.format(num=0)

for i in l:
    a = "mv " + i + " " + n + ".html"
    n = '{num:02d}'.format(num=int(n)+1)
    os.system(a)
