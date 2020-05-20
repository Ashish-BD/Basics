import pdfkit
import pandas as pd
import glob
import lxml.etree as ET
import O_XML

from pyspark.sql import SparkSession

class Merge:
    def main(self):
            spark = SparkSession.builder.appName("Reports").master("local[*]").enableHiveSupport().getOrCreate();
            global filelist
            # dff.show(10)
            spark.conf.set("spark.sql.execution.arrow.enabled", "true")
            dff = spark.sql("Select * from db1.n_info")

            dff.write.mode("overwrite").option("header", "true").csv("/home/vaibhav/Desktop/DataSet/Merge/n_info")
            filelist = glob.glob("/home/vaibhav/Desktop/DataSet/Merge/n_info/*.csv")
            chunksize = 500
            #print filelist
            read_IN= raw_input("You want to convert hive data is which format, please enter PDF/Excel/XMLwithStyle or All :")
            if (read_IN == 'PDF'):
                self.createPDF(chunksize)
            elif (read_IN == 'Excel'):
                self.createExcel(chunksize)
            elif (read_IN == 'XMLwithStyle'):
                O_XML.XML_COnverter().createXML()
            elif (read_IN=='All'):
                print "Creating PDF report..."
                self.createPDF(chunksize)
                print "PDF report created"
                print "Creating excel report... "
                self.createExcel(chunksize)
                print "Excel report created"
                print "Creating XML report..."
                O_XML.XML_COnverter().createXML()
                print "Created XML report, added style and transformed it to HTML"
            else:
                print "Please enter correct input"



    def createPDF(self,chunksize):
        for filename in filelist:
            results = pd.DataFrame([])

            chunksize = 20000
            for gm_chunk in pd.read_csv(filename, chunksize=chunksize):
                print ("DF reading is going on...", filename)
                results = results.append(gm_chunk)
                # print results.shape


            file = open('/home/vaibhav/Desktop/DataSet/n_info.html', 'w')
            print "It is writing to HTML file"
            file.write(results.to_html())
            print ("Now will write PDF", filename)
            file.close()

            options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                '--header-html': '/home/vaibhav/Desktop/DataSet/CSS/header.html',
                '--user-style-sheet': '/home/vaibhav/Desktop/DataSet/CSS/v.css',

            }
            pdfkit.from_file('/home/vaibhav/Desktop/DataSet/n_info.html',
                             '/home/vaibhav/Desktop/DataSet/Merge/{}_n_info.pdf'.format(filename[50:56]),
                             options=options, cover='/home/vaibhav/Desktop/DataSet/CSS/Cover.html')

    def createExcel(self,chunksize):

        writer = pd.ExcelWriter('/home/vaibhav/Desktop/DataSet/Merge/export_dataframe.xlsx', engine='xlsxwriter',
                                mode='w')

        # writer.book.use_zip64()
        df = pd.DataFrame({'': []})
        df.to_excel(excel_writer=writer, sheet_name='Cover sheet', index=False)
        worksheet_for_c = writer.sheets['Cover sheet']
        # Widen the first column to make the text clearer.
        worksheet_for_c.set_column('A:B', 25)

        #     # Insert an image.
        worksheet_for_c.write('A2', 'Insert an image in a cell:')
        worksheet_for_c.insert_image('B2', '/home/vaibhav/Desktop/DataSet/CSS/excel_img.png')
        i = 1
        for file in filelist:
            print file

            for gm_chunk in pd.read_csv(file, chunksize=chunksize):
                # result_pdf.to_excel()

                gm_chunk.to_excel(excel_writer=writer, sheet_name='sheet {}'.format(str(i)), index=False, header=True,
                                  startrow=2, startcol=0, freeze_panes=(3, 10))


                workbook = writer.book
                worksheet = writer.sheets['sheet {}'.format(str(i))]
                cell_format = workbook.add_format({'bg_color': '#efefef'})
                cell_format.set_align('centre')
                # cell_format.set_border(style=0)
                worksheet.set_column('A3:H3', 18, cell_format)
                merge_format = workbook.add_format({
                    'bold': 1,
                    'border': 1,
                    'align': 'center',
                    'valign': 'vcenter',
                    'fg_color': 'red'})
                worksheet.merge_range('A1:H2', 'It is a place holder', merge_format)

                i += 1
            writer.save()
            print ("Excel Report has been created")


obj = Merge()
obj.main()

