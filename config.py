# function to plot distribution plot

def dist_plot(data,title):
    sns.set_theme(context="notebook",palette="OrRd_r",style="whitegrid")
    sns.histplot(data,kde=True,stat="count")
    plt.title(title)
    plt.show()