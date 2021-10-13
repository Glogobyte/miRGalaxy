 # Import FPDF class
 from fpdf import FPDF

 # Import glob module to find all the files matching a pattern
 import glob

def pdf_before_DE(analysis):

  # Image extensions
  if analysis=="2":
     image_extensions = ("c_hist_red.png","t_hist_red.png","pie_non.png","spider_red.png","spider_non_red.png","c_logo.png","t_logo.png","c_bar.png","t_bar.png")
  else:
     image_extensions = ("c_hist_red.png","t_hist_red.png","pie_tem.png","spider_red.png","spider_non_red.png")
  # This list will hold the images file names
  images = []

  # Build the image list by merging the glob results (a list of files)
  # for each extension. We are taking images from current folder.
  for extension in image_extensions:
      images.extend(glob.glob(extension))

  # Create instance of FPDF class
  pdf = FPDF('P', 'in', 'A4')
  # Add new page. Without this you cannot create the document.
  pdf.add_page()
  # Set font to Arial, 'B'old, 16 pts
  pdf.set_font('Arial', 'B', 20.0)

  # Page header
  pdf.cell(pdf.w-0.5, 0.5, 'IsomiR Profile Report',align='C')
  pdf.ln(0.7)
  pdf.set_font('Arial','', 16.0)
  pdf.cell(pdf.w-0.5, 0.5, 'sRNA Length Distribution',align='C')

  # Smaller font for image captions
  pdf.set_font('Arial', '', 11.0)

  # Image caption
  pdf.ln(0.5)

  yh=FPDF.get_y(pdf)
  pdf.image(images[0],x=0.3,w=4, h=3)
  pdf.image(images[1],x=4,y=yh, w=4, h=3)
  pdf.ln(0.3)

  # Image caption
  pdf.cell(0.2)
  pdf.cell(3.0, 0.0, "  Mapped and unmapped reads to custom precussor arm reference DB (5p and 3p arms) in Control (left)")
  pdf.ln(0.2)
  pdf.cell(0.2)
  pdf.cell(3.0, 0.0, "  and Treated (right) groups")


  pdf.ln(0.5)
  h1=FPDF.get_y(pdf)
  pdf.image(images[2],x=1, w=6.5, h=5)
  h2=FPDF.get_y(pdf)
  FPDF.set_y(pdf,h1+0.2)
  pdf.set_font('Arial','', 14.0)
  pdf.cell(pdf.w-0.5, 0.5, 'Template and non-template IsomiRs',align='C')
  pdf.set_font('Arial', '', 11.0)
  FPDF.set_y(pdf,h2)
  FPDF.set_y(pdf,9.5)
  # Image caption
  pdf.cell(0.2)
  if analysis=="2":
     pdf.cell(3.0, 0.0, "  Template, non-template, miRNA reference and unmapped sequences as percentage of total sRNA")
  else:
     pdf.cell(3.0, 0.0, "  Template, miRNA reference and unmapped sequences as percentage of total sRNA")
  pdf.ln(0.2)
  pdf.cell(0.2)
  pdf.cell(3.0, 0.0, "  reads in Control (left) and treated (right) groups")



  pdf.add_page()
  pdf.set_font('Arial', 'B', 16.0)
  pdf.cell(pdf.w-0.5, 0.5, "Reference form and isomiR among total miRNA reads",align='C')
  pdf.ln(0.7)
  pdf.set_font('Arial', 'B', 12.0)
  pdf.cell(pdf.w-0.5, 0.5, "Template isomiR profile (redundant)",align='C')
  pdf.ln(0.5)
  pdf.image(images[3],x=1.5, w=5.5, h=4)
  pdf.ln(0.6)
  pdf.cell(pdf.w-0.5, 0.0, "Template isomiR profile (non-redundant)",align='C')
  pdf.set_font('Arial', '', 12.0)
  pdf.ln(0.2)
  pdf.image(images[4],x=1.5, w=5.5, h=4)
  pdf.ln(0.3)
  pdf.set_font('Arial', '', 11.0)
  pdf.cell(0.2)
  pdf.cell(3.0, 0.0, "  * IsomiRs potentialy initiated from multiple loci")


  if analysis=="2":
     pdf.add_page('L')

     pdf.set_font('Arial', 'B', 16.0)
     pdf.cell(pdf.w-0.5, 0.5, "Non-template IsomiRs",align='C')
     pdf.ln(0.5)
     pdf.set_font('Arial', 'B', 12.0)
     pdf.cell(pdf.w-0.5, 0.5, "3' Additions of reference of isomiR sequence",align='C')
     pdf.ln(0.7)

     yh=FPDF.get_y(pdf)
     pdf.image(images[5],x=1.5,w=3.65, h=2.65)
     pdf.image(images[7],x=6.5,y=yh, w=3.65, h=2.65)
     pdf.ln(0.5)
     yh=FPDF.get_y(pdf)
     pdf.image(images[6],x=1.5,w=3.65, h=2.65)
     pdf.image(images[8],x=6.5,y=yh, w=3.65, h=2.65)

  pdf.close()
  pdf.output('report1.pdf','F')




#############################################################################################################################################################3

def pdf_after_DE(analysis,top,font_path,iso_star_fl,non_star_fl):

  # Image extensions
  if analysis=="2":
     image_extensions = ("tem.png","a2.png","non.png")
  else:
    image_extensions = ("tem.png","a2.png")
 
  # This list will hold the images file names
  images = []

  # Build the image list by merging the glob results (a list of files)
  # for each extension. We are taking images from current folder.
  for extension in image_extensions:
      images.extend(glob.glob(extension))
 
  # Create instance of FPDF class
  pdf = FPDF('P', 'in', 'letter')
  pdf.add_font('uni-arial', '', font_path+"/arial-unicode-ms.ttf", uni=True)
  # Add new page. Without this you cannot create the document.
  pdf.add_page()
  # Set font to Arial, 'B'old, 16 pts
  pdf.set_font('Arial', 'B', 16.0)

  # Page header
  pdf.cell(pdf.w-0.5, 0.5, 'Differential expression of miRNAs and isomiRs',align='C')
  #pdf.ln(0.25)

  pdf.ln(0.7)
  pdf.set_font('Arial','B', 12.0)
  if "tem.png" in images:
     pdf.cell(pdf.w-0.5, 0.5, 'Top '+top+' differentially expressed miRNA and templated isoforms',align='C')
     # Smaller font for image captions
     pdf.set_font('Arial', '', 10.0)
     # Image caption 
     pdf.ln(0.4)
     pdf.image(images[images.index("tem.png")],x=0.8, w=7, h=8)
     pdf.ln(0.3)
     if iso_star_fl==1:
        pdf.set_font('uni-arial', '', 9.0)
        pdf.cell(0.2)
        pdf.cell(3.0, 0.0, "  ★ IsomiRs potentially generated from multiple loci")
        #pdf.set_font('Arial','B', 12.0)
  else:
     print("WARNING: There aren't miRNAs which fullfiled these criteria" )
  pdf.set_font('Arial','B', 12.0)
  if "non.png" in images and analysis=="2":
     if "tem.png" in images: pdf.add_page()
     pdf.ln(0.7)
     pdf.cell(pdf.w-0.5, 0.5, 'Top '+top+' differentially expressed non-templated isomiRs',align='C')
     pdf.ln(0.4)
     pdf.image(images[images.index("non.png")],x=0.8, w=7, h=8)
     pdf.ln(0.3)
     if  non_star_fl==1:
         pdf.set_font('uni-arial', '', 9.0)
         pdf.cell(0.2)
         pdf.cell(3.0, 0.0, "  ★ IsomiRs potentially generated from multiple loci")

     #pdf.image(images[images.index("non.png")],x=0.5, w=7.5, h=6.5)
  else:
     print("WARNING: There aren't non-template miRNAs which fullfiled these criteria" )

  pdf.set_font('Arial','B', 12.0)
  if "a2.png" in images:
     if len(images)>=2: pdf.add_page()
     pdf.ln(0.5)
     pdf.cell(pdf.w-0.5, 0.5, 'Top '+top+' differentially expressed miRNAs and isomiRs grouped by arm',align='C')
     pdf.ln(0.4)
     pdf.image(images[images.index("a2.png")],x=0.8, w=7, h=8)
     pdf.ln(0.3)
  else:
     print("WARNING: There aren't non-template miRNAs which fullfiled these criteria" )


  pdf.output('report2.pdf', 'F')



