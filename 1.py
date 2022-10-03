from xml.etree import ElementTree
import csv

# PARSE XML
xml = ElementTree.parse("xyz.xml")


# CREATE CSV FILE
csvfile = open("ans.csv",'w',encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD THE HEADER TO CSV FILE
csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id","FinInstrmGnlAttrbts.FullNm",
                         "FinInstrmGnlAttrbts.ClssfctnTp","FinInstrmGnlAttrbts.CmmdtyDerivInd",
                         "FinInstrmGnlAttrbts.NtnlCcy","Issr"])

# FOR EACH Data
for FinInstrmGnlAttrbts in xml.findall("FinInstrmGnlAttrbts"):
    if(FinInstrmGnlAttrbts):
        FinInstrmGnlAttrbts.Id = FinInstrmGnlAttrbts.find("Id")
        FinInstrmGnlAttrbts.FullNm = FinInstrmGnlAttrbts.find("FullNm")
        FinInstrmGnlAttrbts.ClssfctnTp = FinInstrmGnlAttrbts.find("ClssfctnTp")
        FinInstrmGnlAttrbts.CmmdtyDerivInd = FinInstrmGnlAttrbts.find("CmmdtyDerivInd")
        FinInstrmGnlAttrbts.NtnlCcy = FinInstrmGnlAttrbts.find("NtnlCcy")
        Issr = FinInstrmGnlAttrbts.find("Issr")
        csv_line = [FinInstrmGnlAttrbts.Id.text, FinInstrmGnlAttrbts.FullNm.text, FinInstrmGnlAttrbts.ClssfctnTp.text,
                  FinInstrmGnlAttrbts.CmmdtyDerivInd.text, FinInstrmGnlAttrbts.NtnlCcy.text, Issr.text]
        csvfile_writer.writerow(csv_line)
csvfile.close()  
# EXTRACT  DETAILS
# ADD A NEW ROW TO CSV FILE

