import os

l = ["contents/TOC.html",
"contents/acknowledgements.html",
"contents/notation.html",
"contents/intro.html",
"contents/part_basics.html",
"contents/linear_algebra.html",
"contents/prob.html",
"contents/numerical.html",
"contents/ml.html",
"contents/part_practical.html",
"contents/mlp.html",
"contents/regularization.html",
"contents/optimization.html",
"contents/convnets.html",
"contents/rnn.html",
"contents/guidelines.html",
"contents/applications.html",
"contents/part_research.html",
"contents/linear_factors.html",
"contents/autoencoders.html",
"contents/representation.html",
"contents/graphical_models.html",
"contents/monte_carlo.html",
"contents/partition.html",
"contents/inference.html",
"contents/generative_models.html",
"contents/bib.html",
"contents/index-.html"]

a = "wget http://www.deeplearningbook.org/"

for i in l:
    b = a + i
    os.system(b) 
