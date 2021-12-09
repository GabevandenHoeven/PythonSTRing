
# Install these packages if they are not installed yet.
# install.packages("tidyverse")
# install.packages("ggbeeswarm")

# This R script will only plot for one tool specifically for lobSTR
# If you want to compare tools, use plot_GIAB_sample_script.R

library(tidyverse)
library(ggbeeswarm)

data <- read.csv("results_lobstr.csv")

data %>%
  ggplot(aes(x=Gene, y=Allele, fill=Gene, colour=Gene)) +
  geom_beeswarm(shape="diamond", cex=1, size=1.3, na.rm=TRUE, dodge.width=1,
                priority="descending") +
  labs(y="Allele size",
       title="Called allele size of GIAB samples per gene for lobSTR") +
  theme_bw()
ggsave(filename="Allele_size_per_gene_lobstr.png")

data %>%
  ggplot(aes(x=Gene, y=Normalised, fill=Gene, colour=Gene)) +
  geom_beeswarm(shape="diamond", cex=1, size=1.3, na.rm=TRUE, dodge.width=1,
                priority="descending") +
  labs(y="Normalised allele size",
       title="Normalised allele size of GIAB samples per gene for lobSTR") +
  theme_bw()
ggsave(filename="Allele_size_per_gene_lobstr_normalised.png")

