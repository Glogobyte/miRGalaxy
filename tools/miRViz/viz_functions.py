import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt

#########################################################################################

# Read a file and return it as a list
def read(path, flag):
    if flag == 0:
        with open(path) as fp:
            file=fp.readlines()
        fp.close()
        return file

    if flag == 1:
        with open(path) as fp:
            file = fp.read().splitlines()
        fp.close()
        return file

# Write a list to a txt file
def write(path, list):
    with open(path,'w') as fp:
        for x in list:
            fp.write(str("\t".join(x[1:-1])))
    fp.close()


################################################################################################################################################################>

def top_diff(miRNA_info, number,flag,l):

    Kind=[]

    miRNA_info.sort(key = lambda x: abs(x[1]),reverse=True)
    miRNA_info = miRNA_info[:number]
    miRNA_info.sort(key = lambda x: x[0])

    for x in miRNA_info:
        if x[1] > 0:
           Kind.append(True)
        elif x[1] < 0:
           Kind.append(False)
        else:
           Kind.append("Zero")

    top_miRNA = {"Names": [x[0] for x in miRNA_info],
                  "Log2FC": [x[1] for x in miRNA_info],
                  "Kind": Kind};

    df_miRNA = pd.DataFrame(data=top_miRNA)
    df_miRNA = df_miRNA.sort_values(by=['Names'])
    if df_miRNA.empty==False:
     h1=df_miRNA.plot.barh(x= 'Names',y='Log2FC',color=df_miRNA.Kind.map({True: 'g', False: 'r', 'Zero':'k'})) 
     figure = plt.gcf()  # get current figure
     figure.set_size_inches(5, 12) # set figure's size manually to your full screen (32x18)
     up_reg = mpatches.Patch(color='green', label='Upregulated')
     down_reg = mpatches.Patch(color='red', label='Downregulated')
     font = font_manager.FontProperties(weight='bold', style='normal')
     l3 = plt.legend(handles=[up_reg,down_reg],bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
     h1.set_ylabel(" ", fontsize=3, fontweight='bold')
     h1.set_xlabel("Log2FC", fontsize=12, fontweight='bold')
     plt.axvline(x=0, color="k")

     plt.grid(axis='y', linewidth=0.2)
     plt.grid(axis='x', linewidth=0.2)
     if flag=='t':
        plt.savefig('tem.png', bbox_inches='tight', dpi=300)
     if flag=='nt':
        plt.savefig('non.png', bbox_inches='tight', dpi=300)


################################################################################################################################################################>

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

################################################################################################################################################################>

def top_scatter_non(matures,isoforms,non_temp,uni_names,number):

    mat_names=[]
    mat_log2fc=[]

    iso_names=[]
    iso_log2fc=[]

    non_temp_names=[]
    non_temp_log2fc=[]

    count=0
    for x in uni_names:
        flag = False
        if count<number:
          for y in matures:
            if x in y[0]:
               mat_log2fc.append(y[1])
               mat_names.append(x)
               flag=True
          for y in isoforms:
            if x in y[0]:
               iso_log2fc.append(y[1])
               iso_names.append(x)
               flag=True
          for y in non_temp:
            if x in y[0]:
               non_temp_log2fc.append(y[1])
               non_temp_names.append(x)
               flag=True
          if flag==True:
             count+=1

    mat_df = pd.DataFrame(dict(names=mat_names, log2fc=mat_log2fc))
    iso_df = pd.DataFrame(dict(names=iso_names, log2fc=iso_log2fc))
    non_df = pd.DataFrame(dict(names=non_temp_names, log2fc= non_temp_log2fc))

    iso_df.sort_values(by=['names'])
    mat_df.sort_values(by=['names'])
    non_df.sort_values(by=['names'])

    fig, ax = plt.subplots()

    h3=ax.scatter(iso_df['log2fc'],iso_df['names'],edgecolors='k',linewidth=1, marker='o', c='red',alpha=0.4)
    h1=ax.scatter(mat_df['log2fc'],mat_df['names'],edgecolors='k',linewidth=1, marker='o', c='green',alpha=0.4)
    h2=ax.scatter(non_df['log2fc'],non_df['names'],edgecolors='k',linewidth=1, marker='o', c='orange',alpha=0.4)

    l3 = plt.legend([h1,h2,h3],["RefSeq miRNA","Non-templated isomiR","Templated isomiR"],bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
    plt.axvline(x=0, color="k")
    plt.grid(axis='y', linewidth=0.2)
    plt.grid(axis='x', linewidth=0.2)
    plt.xlabel("Log2FC", fontsize=12, fontweight='bold')
    plt.yticks(rotation=0,ha="right", fontsize=10)
    plt.xticks(rotation=0,ha="right", fontsize=10)
    plt.tight_layout()
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 12) # set figure's size manually to your full screen (32x18)
    plt.savefig('a2.png', bbox_inches='tight', dpi=300)

#########################################################################################################################################################################################################################################

def top_scatter_tem(matures,isoforms,uni_names,number):

    mat_names=[]
    mat_log2fc=[]

    iso_names=[]
    iso_log2fc=[]

    count=0
    for x in uni_names:
        flag = False
        if count<number:
          for y in matures:
            if x in y[0]:
               mat_log2fc.append(y[1])
               mat_names.append(x)
               flag=True
          for y in isoforms:
            if x in y[0]:
               iso_log2fc.append(y[1])
               iso_names.append(x)
               flag=True
          if flag==True:
             count+=1

    mat_df = pd.DataFrame(dict(names=mat_names, log2fc=mat_log2fc))
    iso_df = pd.DataFrame(dict(names=iso_names, log2fc=iso_log2fc))

    iso_df.sort_values(by=['names'])
    mat_df.sort_values(by=['names'])

    fig, ax = plt.subplots()

    h3=ax.scatter(iso_df['log2fc'],iso_df['names'],edgecolors='k',linewidth=1, marker='o', c='red',alpha=0.4)
    h1=ax.scatter(mat_df['log2fc'],mat_df['names'],edgecolors='k',linewidth=1, marker='o', c='green',alpha=0.4)

    l3 = plt.legend([h1,h3],["RefSeq miRNA","Templated isomiR"],bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
    plt.axvline(x=0, color="k")
    plt.grid(axis='y', linewidth=0.2)
    plt.grid(axis='x', linewidth=0.2)
    plt.xlabel("Log2FC", fontsize=12, fontweight='bold')
    plt.yticks(rotation=0,ha="right", fontsize=10)
    plt.xticks(rotation=0,ha="right", fontsize=10)
    plt.tight_layout()
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 12) # set figure's size manually to your full screen (32x18)
    plt.savefig('a2.png', bbox_inches='tight', dpi=300)


##############################################################################################################################################################################################################################################

def preproccess(non_templated,matures,isoforms,log2fc,pval,stat):

       if stat=="3":
          non_temp = [[x[0],float(x[1]),float(x[2])] for x in non_templated if abs(float(x[1]))>log2fc and float(x[2])>pval]
          mat = [[x[0],float(x[1]),float(x[2])] for x in matures if abs(float(x[1]))>log2fc and float(x[2])>pval]
          iso = [[x[0],float(x[1]),float(x[2])] for x in isoforms if abs(float(x[1]))>log2fc and float(x[2])>pval]
       else:
         non_temp = [[x[0],float(x[1]),float(x[2])] for x in non_templated if abs(float(x[1]))>log2fc and float(x[2])<pval]
         mat = [[x[0],float(x[1]),float(x[2])] for x in matures if abs(float(x[1]))>log2fc and float(x[2])<pval]
         iso = [[x[0],float(x[1]),float(x[2])] for x in isoforms if abs(float(x[1]))>log2fc and float(x[2])<pval]

       mat_iso = mat+iso

       if not non_temp and not mat and not iso:
          sys.exit("There aren't entries which meet these criteria")

       mat.sort(key = lambda x: abs(float(x[1])),reverse=True)
       iso.sort(key = lambda x: abs(float(x[1])),reverse=True)
       non_temp.sort(key = lambda x: abs(float(x[1])),reverse=True)

       all=mat+iso+non_temp
       all.sort(key = lambda x: abs(float(x[1])), reverse=True)
       names=[x[0].split("_")[0] for x in all]
       uni_names=unique(names)

       diff_non_templated = [[x[0],float(x[1]),float(x[2])] for x in non_templated if abs(float(x[1]))>1 and float(x[2])<pval and x[0].split("_")[0] in uni_names]
       diff_matures = [[x[0],float(x[1]),float(x[2])] for x in matures if abs(float(x[1]))>1 and float(x[2])<pval and x[0].split("_")[0] in uni_names]
       diff_isoforms = [[x[0],float(x[1]),float(x[2])] for x in isoforms if abs(float(x[1]))>1 and float(x[2])<pval and x[0].split("_")[0] in uni_names]

       diff_matures.sort(key = lambda x: abs(float(x[1])),reverse=True)
       diff_isoforms.sort(key = lambda x: abs(float(x[1])),reverse=True)
       diff_non_templated.sort(key = lambda x: abs(float(x[1])),reverse=True)

       return diff_matures,diff_isoforms,diff_non_templated,uni_names,non_temp,mat_iso

################################################################################################################################################################################################################################################>

