import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

class Exploratory_Analysis:
    def __init__(self, df, visuals):
        self.df=df
        self.visuals=visuals
    
    def ExploratoryAnalysis(self):
        numeric_cols = self.df.select_dtypes(include='number').columns.tolist()
        corrmatix=self.df[numeric_cols].corr()
        print(corrmatix)

        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col].hist(bins=30)
                plt.title(col)
                plt.savefig(os.path.join(self.visuals,f"{col}_histogram.png"))
                plt.tight_layout()
                plt.show()

                plt.figure(figsize=(10,6))
                sns.boxplot(x=self.df[col])
                plt.title(col)
                plt.savefig(os.path.join(self.visuals,f"{col}_boxplot.png"))
                plt.show()