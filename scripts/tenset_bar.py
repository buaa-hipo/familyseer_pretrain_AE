
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
import matplotlib.ticker as ticker

def acc_and_count():
    def add_value_labels(ax, spacing=1, upper=450, lower=-100):
        """Add labels to the end of each bar in a bar chart.

        Arguments:
            ax (matplotlib.axes.Axes): The matplotlib object containing the axes
                of the plot to annotate.
            spacing (int): The distance between the labels and the bars.
        """

        # For each bar: Place a label
        for rect in ax.patches:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            #if y_value < upper and y_value > lower:
            #    continue
            y = y_value
            if y_value > upper:
                y = upper
            if y_value < lower:
                y = lower
            # Number of points between bar and label. Change to your liking.
            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place
            label = "{:.0f}".format(y_value)

            # Create annotation
            ax.annotate(
                label,                      # Use `label` as label
                (x_value, y),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                va=va)                      # Vertically align label differently for
                                            # positive and negative values.

    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # prepare data
    number = []
    acc = []
    
    # Average_acc
    #f = open("average_acc.csv")
    #for line in f:
    #    div = line.split(',')
    #    tenset_acc.append(float(div[0]))
    #    family_acc.append(float(div[1]))
    
    # All_acc
    f = open("countacc.csv")
    for line in f:
        div = line.split(',')
        number.append(float(div[0]))
        acc.append(float(div[1]))
    # print('======== loaded ========')
    # print(redundancy)
    #tenset_acc=tenset_acc[:160]
    #family_acc=family_acc[:160]
    plt.rcParams['font.family'] = "Times New Roman"
    plt.rcParams.update({'font.size': 12})
    plt.rcParams['hatch.linewidth'] = 0.1  # previous pdf hatch linewidth

    # brewer2mpl.get_map args: set name set type number of colors
    # bmap = brewer2mpl.get_map('RdYlBu', 'diverging', 5)

    mycolors = [ '#3399CC', '#003366', '#CCCCCC','#666666' ]
    #mycolors = [ '#fc8d59', '#99d594' ]
    #mycolors = [ '#fc8d59', '#99d594' ]
    # # set color
    #plt.rcParams['axes.color_cycle'] = mycolors
    # print(plt.style.available)
    # plt.style.use('seaborn-darkgrid')
    title = ['[-100%,-20%)','[-20%,-10%)','[-10%,0)','[0,10%)','[10%,20%)','[20%,100%)']
    
    
    
    
    # Plot configuration
    f, ax1 = plt.subplots(1, 1, figsize=(7, 3))
    plt.xticks(rotation=0)
    # make the figure tight
    ax1.set_xlim(-0.5,len(acc)-0.5)
    xlabels = [i for i in range(0,len(acc),1)]
    #ax1.set_xticks(xlabels)
    #ax1.set_xticklabels(labels)
    ax1.set_ylim(0,450)

    

    # ax1.set_xlabel('Cases')
    ax1.set_ylabel('# of subgraph',fontsize=18)
    font = {'style':'normal','weight':'bold'}
    ax1.spines['bottom'].set_position(('data', 0))
    #ax1.spines['top'].set_color("none")
    ax1.spines['right'].set_color("none")
    #x = [ i for i in range(1, len(labels))]
    #x = [i * 3 for i in x]
    #ax1.set_zorder(1)
    #offset_acc = [family_acc[i]-tenset_acc[i] for i in range(0,len(family_acc))]
    #offset_acc.append(0)
    #offset_acc.sort()
    #print(offset_acc.index(0))
    #x1= x
    
    ax2 = ax1.twinx()
    #ax2.set_zorder(0)
    
    ax2.set_ylim(-0.03,0.09)
    ax2.set_ylabel('Top-1 accuracy improvement',fontsize=18)

    ax2.plot(title, acc,color=mycolors[0],linestyle='--',ms=10)
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=1))
    #ax2.spines['bottom'].set_position(('data', 0))
    ax2.spines['top'].set_color("none")
    #ax2.spines['bottom'].set_linestyle((0,(16,16)))
    ax2.spines['bottom'].set_color("none")
    #ax2.set_ylabel('Impact top-1 accuracy change',fontsize=9)
    #ax2.set_yticks(fontsize=9)
    width = 0.4
    ax1.set_xlabel('The range of the top-1 accuracy change (FamilySeer-TenSet)',loc='center',fontsize=12)
    #bar1 = ax1.barh([i for i in xlabels], tenset_acc, color="deepskyblue")
    bar1 = ax1.bar(title, number, color=mycolors[1], width=width, label='TenSet Accuracy', edgecolor=mycolors[1], linewidth=0.1,zorder=5)
    ax1.plot([-1,0,1,2,3,4,5,6,7],[111 for i in range(-1,8,1)],linestyle='--',color='grey',alpha=0.8,zorder=1)
    #bar2 = ax1.bar([i for i in xlabels], family_acc, color=mycolors[0], width=width, label='FamilySeer Accuracy', edgecolor=mycolors[0], linewidth=0.1,zorder=1)
    #bar3 = ax1.bar([i+width/2 for i in xlabels], FAMILYSEER_GPU, color=mycolors[1], width=width, label='FamilySeer+GPU', edgecolor='black', linewidth=0.1,zorder=5)
    #bar4 = ax1.bar([i+3*width/2 for i in xlabels], FAMILYSEER_GPU_PARALLEL, color=mycolors[0], width=width, label='FamilySeer+GPU+PARALLEL', edgecolor='black', linewidth=0.1,zorder=5)
    #ax1.set_xticks(fontsize=9)
    add_value_labels(ax1)
    #plt.xticks([-1],[""])
    #ax1.annotate(s='',xy=(-0.5,0),xytext=(-0.5,-32),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    offset=-1
    #X轴竖线
    
    #plt.yticks([-1],[""])
    
    '''
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenet 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenetv2 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet50 v1",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet152 v2",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"BERT Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"RoBERTa Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"GPT2 Small",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"S.T Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(text='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Geomean",fontdict=font,verticalalignment="bottom",horizontalalignment="center")
    '''
    #ax1.legend(loc='upper right', ncol=4)

    f.savefig('figure-9.pdf', bbox_inches = 'tight')
    plt.show()

def draw_offset():
    def add_value_labels(ax, spacing=1, upper=0.5, lower=-0.5):
        """Add labels to the end of each bar in a bar chart.

        Arguments:
            ax (matplotlib.axes.Axes): The matplotlib object containing the axes
                of the plot to annotate.
            spacing (int): The distance between the labels and the bars.
        """

        # For each bar: Place a label
        for rect in ax.patches:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            if y_value < upper and y_value > lower:
                continue
            y = y_value
            if y_value > upper:
                y = upper
            if y_value < lower:
                y = lower
            # Number of points between bar and label. Change to your liking.
            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place
            label = "{:.1f}".format(y_value)

            # Create annotation
            ax.annotate(
                label,                      # Use `label` as label
                (x_value, y),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                va=va)                      # Vertically align label differently for
                                            # positive and negative values.

    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # prepare data
    tenset_acc = []
    family_acc = []
    
    # Average_acc
    #f = open("average_acc.csv")
    #for line in f:
    #    div = line.split(',')
    #    tenset_acc.append(float(div[0]))
    #    family_acc.append(float(div[1]))
    
    # All_acc
    f = open("family_acc.csv")
    for line in f:
        family_acc.append(float(line.replace("\n","")))
    
    f = open("tenset_acc.csv")
    for line in f:
        tenset_acc.append(float(line.replace("\n","")))
    # print('======== loaded ========')
    # print(redundancy)
    #tenset_acc=tenset_acc[:160]
    #family_acc=family_acc[:160]

    plt.rcParams.update({'font.size': 8})
    plt.rcParams['hatch.linewidth'] = 0.1  # previous pdf hatch linewidth

    # brewer2mpl.get_map args: set name set type number of colors
    # bmap = brewer2mpl.get_map('RdYlBu', 'diverging', 5)

    mycolors = [ '#3399CC', '#003366', '#CCCCCC','#666666' ]
    #mycolors = [ '#fc8d59', '#99d594' ]
    mycolors = [ '#fc8d59', '#99d594' ]
    # # set color
    #plt.rcParams['axes.color_cycle'] = mycolors
    # print(plt.style.available)
    # plt.style.use('seaborn-darkgrid')

    # Plot configuration
    f, ax1 = plt.subplots(1, 1, figsize=(12, 4))
    plt.xticks(rotation=0)
    # make the figure tight
    ax1.set_xlim(-1,len(tenset_acc))
    xlabels = [i for i in range(0,len(tenset_acc),1)]
    #ax1.set_xticks(xlabels)
    #ax1.set_xticklabels(labels)
    ax1.set_ylim(-0.5,0.5)

    # ax1.set_xlabel('Cases')
    ax1.set_ylabel('Accuracy')
    font = {'style':'normal','weight':'bold'}

    #x = [ i for i in range(1, len(labels))]
    #x = [i * 3 for i in x]

    offset_acc = [family_acc[i]-tenset_acc[i] for i in range(0,len(family_acc))]
    #offset_acc.append(0)
    #offset_acc.sort()
    #print(offset_acc.index(0))
    
    #x1= x
    width = 1
    #bar1 = ax1.barh([i for i in xlabels], tenset_acc, color="deepskyblue")
    bar1 = ax1.bar([i for i in xlabels], offset_acc, color=mycolors[1], width=width, label='TenSet Accuracy', edgecolor=mycolors[1], linewidth=0.1,zorder=5,alpha=0.8)
    #bar2 = ax1.bar([i for i in xlabels], family_acc, color=mycolors[0], width=width, label='FamilySeer Accuracy', edgecolor=mycolors[0], linewidth=0.1,zorder=1)
    #bar3 = ax1.bar([i+width/2 for i in xlabels], FAMILYSEER_GPU, color=mycolors[1], width=width, label='FamilySeer+GPU', edgecolor='black', linewidth=0.1,zorder=5)
    #bar4 = ax1.bar([i+3*width/2 for i in xlabels], FAMILYSEER_GPU_PARALLEL, color=mycolors[0], width=width, label='FamilySeer+GPU+PARALLEL', edgecolor='black', linewidth=0.1,zorder=5)
    add_value_labels(ax1)
    plt.xticks([-1],[""])
    #ax1.annotate(s='',xy=(-0.5,0),xytext=(-0.5,-32),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    offset=-1
    #X轴竖线
    '''
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenet 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenetv2 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet50 v1",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet152 v2",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"BERT Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"RoBERTa Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"GPT2 Small",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"S.T Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(text='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Geomean",fontdict=font,verticalalignment="bottom",horizontalalignment="center")
    '''
    ax1.legend(loc='upper right', ncol=4)

    f.savefig('../../../wlq/tenset_acc_bar.pdf', bbox_inches = 'tight')
    plt.show()

#draw_offset()

def draw_horizon():
    def add_value_labels(ax, spacing=1, upper=1.4, lower=0.0):
        """Add labels to the end of each bar in a bar chart.

        Arguments:
            ax (matplotlib.axes.Axes): The matplotlib object containing the axes
                of the plot to annotate.
            spacing (int): The distance between the labels and the bars.
        """

        # For each bar: Place a label
        for rect in ax.patches:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            if y_value < upper and y_value > lower:
                continue
            y = y_value
            if y_value > upper:
                y = upper
            if y_value < lower:
                y = lower
            # Number of points between bar and label. Change to your liking.
            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place
            label = "{:.1f}".format(y_value)

            # Create annotation
            ax.annotate(
                label,                      # Use `label` as label
                (x_value, y),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                va=va)                      # Vertically align label differently for
                                            # positive and negative values.

    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # prepare data
    tenset_acc = []
    family_acc = []
    
    # Average_acc
    f = open("average_acc.csv")
    for line in f:
        div = line.split(',')
        tenset_acc.append(float(div[0]))
        family_acc.append(float(div[1]))
    
    # All_acc
    #f = open("family_acc.csv")
    #for line in f:
    #    family_acc.append(float(line.replace("\n","")))
    
    #f = open("tenset_acc.csv")
    #for line in f:
    #    tenset_acc.append(float(line.replace("\n","")))
    # print('======== loaded ========')
    # print(redundancy)
    #tenset_acc=tenset_acc[:160]
    #family_acc=family_acc[:160]

    #offset_acc = [family_acc[i]-tenset_acc[i] for i in range(0,len(family_acc))]
    #offset_acc.append(0)
    #offset_acc.sort()
    #print(offset_acc.index(0))
    
    
    plt.rcParams.update({'font.size': 8})
    plt.rcParams['hatch.linewidth'] = 0.1  # previous pdf hatch linewidth

    # brewer2mpl.get_map args: set name set type number of colors
    # bmap = brewer2mpl.get_map('RdYlBu', 'diverging', 5)

    mycolors = [ '#3399CC', '#003366', '#CCCCCC','#666666' ]
    #mycolors = [ '#fc8d59', '#99d594' ]
    mycolors = [ '#fc8d59', '#99d594' ]
    # # set color
    #plt.rcParams['axes.color_cycle'] = mycolors
    # print(plt.style.available)
    # plt.style.use('seaborn-darkgrid')

    # Plot configuration
    f, ax1 = plt.subplots(1, 1, figsize=(12, 4))
    plt.xticks(rotation=0)
    # make the figure tight
    ax1.set_xlim(-1,len(tenset_acc))
    xlabels = [i for i in range(0,len(tenset_acc),1)]
    #ax1.set_xticks(xlabels)
    #ax1.set_xticklabels(labels)
    ax1.set_ylim(0.4,1.1)

    # ax1.set_xlabel('Cases')
    ax1.set_ylabel('Accuracy')
    font = {'style':'normal','weight':'bold'}

    #x = [ i for i in range(1, len(labels))]
    #x = [i * 3 for i in x]


    #x1= x
    width = 1
    #bar1 = ax1.barh([i for i in xlabels], tenset_acc, color="deepskyblue")
    bar1 = ax1.bar([i for i in xlabels], tenset_acc, color=mycolors[1], width=width, label='TenSet Accuracy', edgecolor=mycolors[1], linewidth=0.1,zorder=5,alpha=0.8)
    bar2 = ax1.bar([i for i in xlabels], family_acc, color=mycolors[0], width=width, label='FamilySeer Accuracy', edgecolor=mycolors[0], linewidth=0.1,zorder=1)
    #bar3 = ax1.bar([i+width/2 for i in xlabels], FAMILYSEER_GPU, color=mycolors[1], width=width, label='FamilySeer+GPU', edgecolor='black', linewidth=0.1,zorder=5)
    #bar4 = ax1.bar([i+3*width/2 for i in xlabels], FAMILYSEER_GPU_PARALLEL, color=mycolors[0], width=width, label='FamilySeer+GPU+PARALLEL', edgecolor='black', linewidth=0.1,zorder=5)
    add_value_labels(ax1)
    plt.xticks([-1],[""])
    #ax1.annotate(s='',xy=(-0.5,0),xytext=(-0.5,-32),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    offset=-1
    #X轴竖线
    '''
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenet 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenetv2 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet50 v1",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet152 v2",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"BERT Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"RoBERTa Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"GPT2 Small",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"S.T Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(text='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Geomean",fontdict=font,verticalalignment="bottom",horizontalalignment="center")
    '''
    ax1.legend(loc='upper right', ncol=4)

    f.savefig('../../../wlq/tenset_acc_bar.pdf', bbox_inches = 'tight')
    plt.show()

#draw_horizon()

def draw():
    def add_value_labels(ax, spacing=1, upper=1.4, lower=0.0):
        """Add labels to the end of each bar in a bar chart.

        Arguments:
            ax (matplotlib.axes.Axes): The matplotlib object containing the axes
                of the plot to annotate.
            spacing (int): The distance between the labels and the bars.
        """

        # For each bar: Place a label
        for rect in ax.patches:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            if y_value < upper and y_value > lower:
                continue
            y = y_value
            if y_value > upper:
                y = upper
            if y_value < lower:
                y = lower
            # Number of points between bar and label. Change to your liking.
            space = spacing
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place
            label = "{:.1f}".format(y_value)

            # Create annotation
            ax.annotate(
                label,                      # Use `label` as label
                (x_value, y),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                va=va)                      # Vertically align label differently for
                                            # positive and negative values.

    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    # prepare data
    tenset_acc = []
    family_acc = []
    f = open("average_acc.csv")
    for line in f:
        div = line.split(',')
        tenset_acc.append(float(div[0]))
        family_acc.append(float(div[1]))
    
    # print('======== loaded ========')
    # print(redundancy)
    #tenset_acc=tenset_acc[:160]
    #family_acc=family_acc[:160]

    plt.rcParams.update({'font.size': 8})
    plt.rcParams['hatch.linewidth'] = 0.1  # previous pdf hatch linewidth

    # brewer2mpl.get_map args: set name set type number of colors
    # bmap = brewer2mpl.get_map('RdYlBu', 'diverging', 5)

    mycolors = [ '#3399CC', '#003366', '#CCCCCC','#666666' ]
    #mycolors = [ '#fc8d59', '#99d594' ]
    mycolors = [ '#fc8d59', '#99d594' ]
    # # set color
    #plt.rcParams['axes.color_cycle'] = mycolors
    # print(plt.style.available)
    # plt.style.use('seaborn-darkgrid')

    # Plot configuration
    f, ax1 = plt.subplots(1, 1, figsize=(12, 4))
    plt.xticks(rotation=0)
    # make the figure tight
    ax1.set_ylim(-1,len(tenset_acc))
    xlabels = [i for i in range(0,len(tenset_acc),1)]
    #ax1.set_xticks(xlabels)
    #ax1.set_xticklabels(labels)
    ax1.set_xlim(-0.0,1.0)

    # ax1.set_xlabel('Cases')
    ax1.set_xlabel('Accuracy')
    font = {'style':'normal','weight':'bold'}

    #x = [ i for i in range(1, len(labels))]
    #x = [i * 3 for i in x]


    #x1= x
    width = 1
    #bar1 = ax1.barh([i for i in xlabels], tenset_acc, color="deepskyblue")
    bar1 = ax1.barh([i for i in xlabels], tenset_acc, color=mycolors[1], height=width, label='TenSet Accuracy', edgecolor=mycolors[1], linewidth=0.1,zorder=5, alpha=0.5)
    bar2 = ax1.barh([i for i in xlabels], family_acc, color=mycolors[0], height=width, label='FamilySeer Accuracy', edgecolor=mycolors[0], linewidth=0.1,zorder=1)
    #bar3 = ax1.bar([i+width/2 for i in xlabels], FAMILYSEER_GPU, color=mycolors[1], width=width, label='FamilySeer+GPU', edgecolor='black', linewidth=0.1,zorder=5)
    #bar4 = ax1.bar([i+3*width/2 for i in xlabels], FAMILYSEER_GPU_PARALLEL, color=mycolors[0], width=width, label='FamilySeer+GPU+PARALLEL', edgecolor='black', linewidth=0.1,zorder=5)
    add_value_labels(ax1)
    plt.yticks([-1],[""])
    #ax1.annotate(s='',xy=(-0.5,0),xytext=(-0.5,-32),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    offset=-1
    #X轴竖线
    '''
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenet 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=2.0, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Mobilenetv2 0.5",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet50 v1",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"ResNet152 v2",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"BERT Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"RoBERTa Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"GPT2 Small",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(s='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"S.T Large",fontdict=font,verticalalignment="bottom",horizontalalignment="center")

    offset=offset+6
    ax1.annotate(text='',xy=(offset,0.8),xytext=(offset,-0.05),arrowprops=dict(facecolor='black', headlength=20, width=0.1, headwidth=0.01))
    ax1.text(offset+3,-0.1,"Geomean",fontdict=font,verticalalignment="bottom",horizontalalignment="center")
    '''
    ax1.legend(loc='upper right', ncol=4)

    f.savefig('../../../wlq/tenset_acc_bar.pdf', bbox_inches = 'tight')
    plt.show()

#draw()

def extract_data():
    
    symbol = dict()
    symbol['acc'] = ['peak1: ', '']
    symbol['task'] = ['LearningTask(workload_key=', ', target=\'cuda -keys=cuda']
    symbol['not_task']=['Task 0 = LearningTask(workload_key=',', target=\'cuda -keys=cuda']
    
    # tenset精度提取
    ta = open("tenset_acc.log", "r")
    acccsv = open("tenset_acc.csv","w")
    titlecsv = open("tenset_acc_title.csv","w")
    for line in ta:
        
        #if line.find("./dataset/measure_records/ansor_log") != -1:
            #print(line.replace("\n","")) 
        
        if line.find(symbol['acc'][0]) != -1:
            strings = symbol['acc'][0]
            first = line.find(strings) + len(strings)
            temp = line[first:]
            #print(temp)
            try:
                temp = float(temp)
            except:
                temp = None
            if temp is not None:
                acccsv.write(str(temp)+'\n')
            else:
                print ("########################")

        if line.find(symbol['task'][0]) != -1 & line.find(symbol['not_task'][0]) == -1:
            strings = symbol['task'][0]
            first = line.find(strings) + len(strings)
            strings = symbol['task'][1]
            end = line.find(strings)
            temp = line[first+1:end-1]
            #print(temp)

            if temp is not None:
                titlecsv.write(str(temp)+'\n')
            else:
                print ("########################")
    ta.close()
    acccsv.close()
    titlecsv.close()
    
    # tenset_add精度提取
    ta = open("tenset_add_acc.log", "r")
    acccsv = open("tenset_add_acc.csv","w")
    titlecsv = open("tenset_add_acc_title.csv","w")
    for line in ta:
        
        #if line.find("./dataset/measure_records/ansor_log") != -1:
            #print(line.replace("\n","")) 
        
        if line.find(symbol['acc'][0]) != -1:
            strings = symbol['acc'][0]
            first = line.find(strings) + len(strings)
            temp = line[first:]
            #print(temp)
            try:
                temp = float(temp)
            except:
                temp = None
            if temp is not None:
                acccsv.write(str(temp)+'\n')
            else:
                print ("########################")

        if line.find(symbol['task'][0]) != -1 & line.find(symbol['not_task'][0]) == -1:
            strings = symbol['task'][0]
            first = line.find(strings) + len(strings)
            strings = symbol['task'][1]
            end = line.find(strings)
            temp = line[first+1:end-1]
            #print(temp)

            if temp is not None:
                titlecsv.write(str(temp)+'\n')
            else:
                print ("########################")
    ta.close()
    acccsv.close()
    titlecsv.close()
    
    # family精度提取
    fa = open("family_acc.log","r")
    acccsv = open("family_acc.csv","w")
    titlecsv = open("family_acc_title.csv","w")
    
    for line in fa:
        if line.find(symbol['acc'][0]) != -1:
            strings = symbol['acc'][0]
            first = line.find(strings) + len(strings)
            temp = line[first:]
            try:
                temp = float(temp)
            except:
                temp = None
            if temp is not None:
                acccsv.write(str(temp)+'\n')
            else:
                print ("########################")
    
        if line.find(symbol['task'][0]) != -1 & line.find(symbol['not_task'][0]) == -1:
            strings = symbol['task'][0]
            first = line.find(strings) + len(strings)
            strings = symbol['task'][1]
            end = line.find(strings)
            temp = line[first+1:end-1]
            #print(temp)

            if temp is not None:
                titlecsv.write(str(temp)+'\n')
            else:
                print ("########################")
    fa.close()
    acccsv.close()
    titlecsv.close()
    
    # family_add精度提取
    fa = open("family_add_acc.log","r")
    acccsv = open("family_add_acc.csv","w")
    titlecsv = open("family_add_acc_title.csv","w")
    
    for line in fa:
        if line.find(symbol['acc'][0]) != -1:
            strings = symbol['acc'][0]
            first = line.find(strings) + len(strings)
            temp = line[first:]
            try:
                temp = float(temp)
            except:
                temp = None
            if temp is not None:
                acccsv.write(str(temp)+'\n')
            else:
                print ("########################")
    
        if line.find(symbol['task'][0]) != -1 & line.find(symbol['not_task'][0]) == -1:
            strings = symbol['task'][0]
            first = line.find(strings) + len(strings)
            strings = symbol['task'][1]
            end = line.find(strings)
            temp = line[first+1:end-1]
            #print(temp)

            if temp is not None:
                titlecsv.write(str(temp)+'\n')
            else:
                print ("########################")
    fa.close()
    acccsv.close()
    titlecsv.close()
    
extract_data()

def delete_unpair_data():
    fwcsv = open("family_acc.csv","r+")
    ftcsv = open("family_acc_title.csv","r+")
    fdata = []
    ftitle = []
    for line in fwcsv:
        fdata.append(line.replace("\n",""))
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    
    #twcsv = open("tenset_acc.csv","r+")
    ttcsv = open("tenset_acc_title.csv","r")
    #tdata=[]
    ttitle=[]
    #for line in twcsv:
    #    tdata.append(line.replace("\n",""))
    for line in ttcsv:
        ttitle.append(line.replace("\n",""))

    for index_i,i in enumerate(ftitle):
        #print (i[16:48])
        if i not in ttitle:
            ftitle.remove(i)
            fdata.pop(index_i)
            
    #print(len(ftitle),"  ",len(fdata))        

    for data in fdata:
        fwcsv.write(data+'\n')
    for title in ftitle:
        ftcsv.write(title+'\n')
    
    fwcsv.close()
    ftcsv.close()
    ttcsv.close()    
    
    # ====================================
    
    fwcsv = open("family_add_acc.csv","r+")
    ftcsv = open("family_add_acc_title.csv","r+")
    fdata = []
    ftitle = []
    for line in fwcsv:
        fdata.append(line.replace("\n",""))
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    
    #twcsv = open("tenset_acc.csv","r+")
    ttcsv = open("tenset_add_acc_title.csv","r")
    #tdata=[]
    ttitle=[]
    #for line in twcsv:
    #    tdata.append(line.replace("\n",""))
    for line in ttcsv:
        ttitle.append(line.replace("\n",""))

    for index_i,i in enumerate(ftitle):
        #print (i[16:48])
        if i not in ttitle:
            ftitle.remove(i)
            fdata.pop(index_i)
            
    #print(len(ftitle),"  ",len(fdata))        

    for data in fdata:
        fwcsv.write(data+'\n')
    for title in ftitle:
        ftcsv.write(title+'\n')
    
    fwcsv.close()
    ftcsv.close()
    ttcsv.close()    
        
#delete_unpair_data()

def shift_data():
    ftcsv = open("family_acc_title.csv","r")
    ftitle = []
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    
    twcsv = open("tenset_acc.csv","r")
    ttcsv = open("tenset_acc_title.csv","r")
    tdata=[]
    ttitle=[]
    for line in twcsv:
        tdata.append(line.replace("\n",""))
    for line in ttcsv:
        ttitle.append(line.replace("\n",""))
    
    #print(ttitle)
    for index_i,i in enumerate(ftitle):
        #print (i[16:48])
        for index_j,j in enumerate(ttitle):
            #print(j)
            if i == j:
                print(index_i,"  ",index_j)
                ttitle[index_i],ttitle[index_j] = ttitle[index_j],ttitle[index_i]
                tdata[index_i],tdata[index_j] = tdata[index_j],tdata[index_i]
                
    ncsv = open("tenset_acc_transpose.csv","w")
    ntcsv = open("tenset_acc_title_transpose.csv","w")
    
    for data in tdata:
        ncsv.write(data+'\n')
    for title in ttitle:
        ntcsv.write(title+'\n')
    
    ftcsv.close()
    twcsv.close()
    ttcsv.close()
    ncsv.close()
    ntcsv.close()
    
    
    # =========================================
    ftcsv = open("family_add_acc_title.csv","r")
    ftitle = []
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    
    twcsv = open("tenset_add_acc.csv","r")
    ttcsv = open("tenset_add_acc_title.csv","r")
    tdata=[]
    ttitle=[]
    for line in twcsv:
        tdata.append(line.replace("\n",""))
    for line in ttcsv:
        ttitle.append(line.replace("\n",""))
    
    #print(ttitle)
    
    for index_i,i in enumerate(ftitle):
        #print (i[16:48])
        for index_j,j in enumerate(ttitle):
            #print(j)
            if i == j:
                print(index_i,"  ",index_j)
                ttitle[index_i],ttitle[index_j] = ttitle[index_j],ttitle[index_i]
                tdata[index_i],tdata[index_j] = tdata[index_j],tdata[index_i]
                
    ncsv = open("tenset_add_acc_transpose.csv","w")
    ntcsv = open("tenset_add_acc_title_transpose.csv","w")
    
    for data in tdata:
        ncsv.write(data+'\n')
    for title in ttitle:
        ntcsv.write(title+'\n')
    
    ftcsv.close()
    twcsv.close()
    ttcsv.close()
    ncsv.close()
    ntcsv.close()

shift_data()

def average_data():
    twcsv = open("tenset_acc_transpose.csv","r")
    fwcsv = open("family_acc.csv","r")
    ftcsv = open("family_acc_title.csv","r")
    
    ftitle=[]
    tdata=[]
    fdata=[]
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    for line in twcsv:
        tdata.append(float(line.replace("\n","")))
    for line in fwcsv:
        fdata.append(float(line.replace("\n","")))
    
    
    
    avcsv = open("average_acc.csv","w")
    flag = 0
    flag_title = ftitle[0][2:34]
    for i,title in enumerate(ftitle):
        if flag_title != title[2:34]:
            #print(tdata[flag:i])
            avcsv.write("{},{}\n".format(np.average(tdata[flag:i]),np.average(fdata[flag:i])))
            flag_title= title[2:34]
            flag = i
        else:
            if i==len(ftitle):
                avcsv.write("{},{}\n".format(np.average(tdata[flag:i]),np.average(fdata[flag:i])))
            continue
        
#average_data()

def countacc():
    twcsv = open("tenset_acc_transpose.csv","r")
    fwcsv = open("family_acc.csv","r")
    ftcsv = open("family_acc_title.csv","r")
    
    ftitle=[]
    tdata=[]
    fdata=[]
    for line in ftcsv:
        ftitle.append(line.replace("\n",""))
    for line in twcsv:
        tdata.append(float(line.replace("\n","")))
    for line in fwcsv:
        fdata.append(float(line.replace("\n","")))
    
    range_list = [0,0,0,0,0,0]
    offset_value_list = [0,0,0,0,0,0]
    cacsv = open("countacc.csv","w")
    for i,title in enumerate(ftitle):
        offset = fdata[i]-tdata[i]
        if offset<-0.2:
            range_list[0] = range_list[0] + 1
            offset_value_list[0] = offset_value_list[0] + offset
        elif offset>=-0.2 and offset<-0.1:
            range_list[1] = range_list[1] + 1
            offset_value_list[1] = offset_value_list[1] + offset
        elif offset>=-0.1 and offset<-0.0:
            range_list[2] = range_list[2] + 1
            offset_value_list[2] = offset_value_list[2] + offset
        elif offset>=0.0 and offset<0.1:
            range_list[3] = range_list[3] + 1
            offset_value_list[3] = offset_value_list[3] + offset
        elif offset>=0.1 and offset<0.2:
            range_list[4] = range_list[4] + 1
            offset_value_list[4] = offset_value_list[4] + offset
        elif offset>=0.2:
            range_list[5] = range_list[5] + 1
            offset_value_list[5] = offset_value_list[5] + offset
        else:
            print("error")
            input()
    for i in range(0,len(range_list)):
        cacsv.write("{},{}\n".format(range_list[i],offset_value_list[i]/1194))
        
    cacsv.close()
countacc()

acc_and_count()
