from viz_graphs import *
from viz_functions import *
import argparse
import time
from multiprocessing import Process, Lock, Manager

##################################################################################################################################################################################################################################################################
starttime = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input", help="choose type of analysis", action="store")
parser.add_argument("-p_value", "--pval", help="choose type of analysis", action="store")
parser.add_argument("-fc", "--log2fc", help="choose type of analysis", action="store")
parser.add_argument("-top", "--top_mirnas", help="choose type of analysis", action="store")
parser.add_argument("-tool_dir", "--tool_directory", help="tool directory path", action="store")
parser.add_argument("-statistic", "--stat", help="tool directory path", action="store")
parser.add_argument("-diff_tool", "--tool", help="tool directory path", action="store")

args = parser.parse_args()

l=Lock()
number = int(args.top_mirnas)
log2fc = float(args.log2fc)
pval = float(args.pval)
iso_star_flag=0
non_star_flag=0

if args.tool=="2":

   raw_EdgeR = read(args.input,0)
   EdgeR = [x.rstrip("\n").split("\t") for x in raw_EdgeR]
   del EdgeR[0]
   for x in EdgeR:
       if "/" in x[0]:
           x[0]=x[0].split("/")[0]+"★"

   if args.stat=="1":
      non_templated = [[x[0],x[1],x[4]] for x in EdgeR if "nt" in x[0] and x[1]!="NA" and x[4]!="NA"]
      matures = [[x[0],x[1],x[4]] for x in EdgeR if 'chr' in x[0].split("_")[-1] and "nt" not in x[0] and x[1]!="NA" and x[4]!="NA"]
      isoforms = [[x[0],x[1],x[4]] for x in EdgeR if 'chr' not in x[0].split("_")[-1] and "nt" not in x[0] and x[1]!="NA" and x[4]!="NA"]
   else:
      non_templated = [[x[0],x[1],x[5]] for x in EdgeR if "nt" in x[0] and x[1]!="NA" and x[5]!="NA"]
      matures = [[x[0],x[1],x[5]] for x in EdgeR if 'chr' in x[0].split("_")[-1] and "nt" not in x[0] and x[1]!="NA" and x[5]!="NA"]
      isoforms = [[x[0],x[1],x[5]] for x in EdgeR if 'chr' not in x[0].split("_")[-1] and "nt" not in x[0] and x[1]!="NA" and x[5]!="NA"]

if args.tool=="1":

   raw_Deseq = read(args.input,0)
   Deseq = [x.rstrip("\n").split("\t") for x in raw_Deseq]
   for x in Deseq:
       if "/" in x[0]:
           x[0]=x[0].split("/")[0]+"★"

   if args.stat=="1":
      non_templated = [[x[0],x[2],x[5]] for x in Deseq if "nt" in x[0] and x[2]!="NA" and x[5]!="NA"]
      matures = [[x[0],x[2],x[5]] for x in Deseq if 'chr' in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[5]!="NA"]
      isoforms = [[x[0],x[2],x[5]] for x in Deseq if 'chr' not in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[5]!="NA"]
   elif args.stat=="2":
      non_templated = [[x[0],x[2],x[6]] for x in Deseq if "nt" in x[0] and x[2]!="NA" and x[6]!="NA"]
      matures = [[x[0],x[2],x[6]] for x in Deseq if 'chr' in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[6]!="NA"]
      isoforms = [[x[0],x[2],x[6]] for x in Deseq if 'chr' not in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[6]!="NA"]
   else:
      non_templated = [[x[0],x[2],x[1]] for x in Deseq if "nt" in x[0] and x[2]!="NA" and x[1]!="NA"]
      matures = [[x[0],x[2],x[1]] for x in Deseq if 'chr' in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[1]!="NA"]
      isoforms = [[x[0],x[2],x[1]] for x in Deseq if 'chr' not in x[0].split("_")[-1] and "nt" not in x[0] and x[2]!="NA" and x[1]!="NA"]


diff_matures,diff_isoforms,diff_non_templated,names,non_temp,mat_iso = preproccess(non_templated,matures,isoforms,log2fc,pval,args.stat)
for x in mat_iso[:number]:
    if "★" in x[0]:
        iso_star_flag=1
        break
for x in non_temp[:number]:
    if "★" in x[0]:
        non_star_flag=1
        break


if non_templated!=[]:
   analysis="2"
   p=[Process(target=top_diff,args=(non_temp,number,"nt",l))]
   p.extend([Process(target=top_diff,args=(mat_iso,number,"t",l))])
   p.extend([Process(target=top_scatter_non,args=(diff_matures,diff_isoforms,diff_non_templated,names,number))])

else:
   analysis="1"
   p=[Process(target=top_diff,args=(mat_iso,number,"t",l))]
   p.extend([Process(target=top_scatter_tem,args=(diff_matures,diff_isoforms,names,number))])

[x.start() for x in p]
[x.join() for x in p]

pdf_after_DE(analysis,args.top_mirnas,args.tool_directory,iso_star_flag,non_star_flag)

print('That took {} seconds'.format(time.time() - starttime))

