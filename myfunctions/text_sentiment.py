import matplotlib.pyplot as plt

def plot_sentiment(x):
    # Create figure and axis objects with a larger figure size
    fig, ax = plt.subplots(figsize=(15, 2))

    # Plot horizontal lines
    ax.hlines(y=0, xmin=-1, xmax=0, color='r', linestyle='-', linewidth=5)
    ax.hlines(y=0, xmin=0, xmax=1, color='b', linestyle='-', linewidth=5)

    if x < 0:
        # Plot red point
        ax.plot(x, 0, marker='o', markersize=15, color='red')
    else:
        # Plot blue point
        ax.plot(x, 0, marker='o', markersize=15, color='blue')

    # Set plot limits
    ax.set_xlim(-1, 1)

    # Set plot labels
    ax.set_xlabel('Vader Score')
    ax.set_ylabel('Negative')

    # Hide the y-axis
    ax.yaxis.set_visible(False)

    # Set the text aligned to the right
    ax.text(1, 0.05, 'Positive',
            horizontalalignment='right',
            verticalalignment='bottom',
            transform=ax.transAxes)

    ax.text(0.06, 0.05, 'Negative',
            horizontalalignment='right',
            verticalalignment='bottom',
            transform=ax.transAxes)

    ax.text(0.52, 0.05, 'Neutral',
            horizontalalignment='right',
            verticalalignment='bottom',
            transform=ax.transAxes)

    # Return the plot
    return fig