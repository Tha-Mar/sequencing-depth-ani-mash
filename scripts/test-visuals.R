# Check if required packages are installed or not
if (!requireNamespace("stringr", quietly = TRUE)) {
  install.packages("stringr")
}
library(stringr)

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)


###### Reading Results ######

ANI_results <- paste0('../test-fastani-mash-data/fastani_results.tab')
MASH_results <- paste0('../test-fastani-mash-data/compiled_mash_distances.tab')
#Read Fastani output file and store as a dataframe
ani_result <- read.table(ANI_results, header=FALSE, sep="\t", row.names=1, check.names=FALSE)

#Add header to ani table
ani_header <- cbind("reference", "ani", "ortholog_count", "total")
colnames(ani_result) <- ani_header

#Read mash output file and store as a dataframe
mash_result <- read.table(MASH_results, header=FALSE, sep="\t", row.names=1, check.names=FALSE)

#Add header to ani table
mash_header <- cbind("reference", "mash", "p_value", "matching_hashes")
colnames(mash_result) <- mash_header

# Combine dataframes
combined_df <- data.frame(
  ani = ani_result$ani,
  mash = mash_result$mash,
  row.names = rownames(ani_result)
)

#Add coverage and subset columns
row_paths <- rownames(combined_df)

# Extract the "coverage_subset"
matches <- str_extract(row_paths, "_([:digit:]+)_([:digit:]+)")

# Extract the coverage and subset by removing the underscore
coverage_subset <- str_remove(matches, "_")

# Split the extracted string into two separate parts (coverage and subset)
split_values <- str_split(coverage_subset, "_")

#Save coverage and subset into different lists
coverage <- c()
subset <- c()
for (pair in split_values) {
  # Check if coverage is 5 and change it to "05" if true
  if (pair[1] == 5) {
    coverage <- c(coverage, "05")  # Append "05" as a string
  } else {
    coverage <- c(coverage, pair[1])  # Append the actual coverage value
  }
  subset <- c(subset, pair[2])
}

#Add vectors to combined dataframe
combined_df$coverage <- coverage
combined_df$subset <- subset


###### Visualization ######


# Create a directory to save visuals
# Check if the directory exists before creating it
if (!dir.exists("../test_ani_mash_visuals")) {
  dir.create("../test_ani_mash_visuals")
} 


#Write combined table as tab delimited file
write.table(combined_df, file="../test_ani_mash_visuals/ani_mash_score_table.txt", sep="\t", quote=F)

## Scatter Plot ##

# Save Plot
png("../test_ani_mash_visuals/Scatter_plot.png", width = 800, height = 600)  # Open graphics device
# Make Plot
ggplot(combined_df, aes(x = ani, y = mash, color = factor(coverage))) +
  geom_point() +
  labs(x = "ANI Score", y = "MASH Score", color = "Coverage Depth") +
  theme_minimal() +
  theme(
    axis.title.x = element_text(size = 16),
    axis.title.y = element_text(size = 16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 12)
  )
#Close device
dev.off()  

## Box Plot (ANI) ##

# Save Plot
png("../test_ani_mash_visuals/ani_boxplot_plot.png", width = 800, height = 600)  # Open graphics device
# Make plot 
ggplot(combined_df, aes(x = factor(coverage), y = ani, fill = factor(coverage))) +
  geom_boxplot() +
  labs(x = "Coverage Depth", y = "ANI Score") +
  theme_minimal() +
  theme(
    axis.title.x = element_text(size = 16),
    axis.title.y = element_text(size = 16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 12)
  )
#Close device
dev.off()  

## Box Plot (mash) ##

# Save Plot
png("../test_ani_mash_visuals/mash_boxplot_plot.png", width = 800, height = 600)  # Open graphics device
# Make plot 
ggplot(combined_df, aes(x = factor(coverage), y = mash, fill = factor(coverage))) +
  geom_boxplot() +
  labs(x = "Coverage Depth", y = "mash Score") +
  theme_minimal() +
  theme(
    axis.title.x = element_text(size = 16),
    axis.title.y = element_text(size = 16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 12)
  )
#Close device
dev.off()  

## Faceted Scatter Plot

# Save Plot
png("../test_ani_mash_visuals/faceted_scatter_plot.png", width = 800, height = 600)  # Open graphics device
ggplot(combined_df, aes(x = ani, y = mash)) +
  geom_point() +
  facet_wrap(~ coverage) +
  labs(x = "ANI Score", y = "MASH Score") +
  theme_minimal() +
  theme(
    axis.title.x = element_text(size = 16),
    axis.title.y = element_text(size = 16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 12)
  )
#Close device
dev.off()  




