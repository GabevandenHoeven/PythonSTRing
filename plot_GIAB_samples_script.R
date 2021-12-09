
# Install these packages if they are not installed yet.
# install.packages("tidyverse")
# install.packages("ggbeeswarm")


library(tidyverse)
library(ggbeeswarm)

data <- read.csv(file.choose())

# Used dataset file for the plots in the research is GIAB_beide.xlsx.
# Reference lengths for tools can be found in GIAB.xlsx

data %>%
  ggplot(aes(x=Gene, y=Allele, fill=Gene, colour=Gene)) +
  geom_beeswarm(shape="diamond", cex=1, size=1.3, na.rm=TRUE, dodge.width=1,
                priority="descending") +
  facet_wrap(~Tool) +
  labs(y="Allele size",
       title="Called allele size of GIAB samples per gene") +
  theme_bw()
ggsave(filename="Allele_size_per_gene.png")


data %>%
  ggplot(aes(x=Gene, y=Normalised, fill=Gene, colour=Gene)) +
  geom_beeswarm(shape="diamond", cex=1, size=1.3, na.rm=TRUE, dodge.width=1,
                priority="descending") +
  facet_wrap(~Tool) +
  labs(y="Normalised allele size",
       title="Normalised allele size of GIAB samples per gene") +
  theme_bw()
ggsave(filename="Allele_size_per_gene_normalised.png")

