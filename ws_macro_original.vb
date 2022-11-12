Sub MailMergeToPdfBasic()                                                        ' Mark the start of the Subroutine (i.e. Macro) and name it "MailMergeToPdf"
' Macro created by Imnoss Ltd
' Please share freely while retaining attribution
' Last Updated 2021-05-03
    Dim masterDoc As Document, singleDoc As Document, lastRecordNum As Long   ' Create variables ("Post-it Notes") for later use
    Set masterDoc = ActiveDocument                                               ' Identify the ActiveDocument (foremost doc when Macro run) as "masterDoc"

    masterDoc.MailMerge.DataSource.ActiveRecord = wdLastRecord                   ' jump to the last active record (active = ticked in edit recipients)
    lastRecordNum = masterDoc.MailMerge.DataSource.ActiveRecord                  ' retrieve the record number of the last active record so we know when to stop

    masterDoc.MailMerge.DataSource.ActiveRecord = wdFirstRecord                  ' jump to the first active record (active = ticked in edit recipients)
    Do While lastRecordNum > 0                                                   ' create a loop, lastRecordNum is used to end the loop by setting to zero (see below)
        masterDoc.MailMerge.Destination = wdSendToNewDocument                    ' Identify that we are creating a word docx (and no e.g. an email)
        masterDoc.MailMerge.DataSource.FirstRecord = masterDoc.MailMerge.DataSource.ActiveRecord              ' Limit the selection to just one document by setting the start ...
        masterDoc.MailMerge.DataSource.LastRecord = masterDoc.MailMerge.DataSource.ActiveRecord               ' ... and end points to the active record
        masterDoc.MailMerge.Execute False                                        ' run the MailMerge based on the above settings (i.e. for one record)
        Set singleDoc = ActiveDocument                                           ' Identify the ActiveDocument (foremost doc after running the MailMerge) as "singleDoc"
        singleDoc.SaveAs2 _
            FileName:=masterDoc.MailMerge.DataSource.DataFields("DocFolderPath").Value & Application.PathSeparator & _
                masterDoc.MailMerge.DataSource.DataFields("DocFileName").Value & ".docx", _
            FileFormat:=wdFormatXMLDocument                                      ' Save "singleDoc" as a word docx with the details provided in the DocFolderPath and DocFileName fields in the MailMerge data
        singleDoc.ExportAsFixedFormat _
            OutputFileName:=masterDoc.MailMerge.DataSource.DataFields("PdfFolderPath").Value & Application.PathSeparator & _
                masterDoc.MailMerge.DataSource.DataFields("PdfFileName").Value & ".pdf", _
            ExportFormat:=wdExportFormatPDF                                      ' Export "singleDoc" as a PDF with the details provided in the PdfFolderPath and PdfFileName fields in the MailMerge data
        singleDoc.Close False                                                    ' Close "singleDoc", the variable "singleDoc" can now be used for the next record when created
        If masterDoc.MailMerge.DataSource.ActiveRecord >= lastRecordNum Then     ' test if we have just created a document for the last record
            lastRecordNum = 0                                                    ' if so we set lastRecordNum to zero to indicate that the loop should end
        Else
            masterDoc.MailMerge.DataSource.ActiveRecord = wdNextRecord           ' otherwise go to the next active record
        End If

    Loop                                                                         ' loop back to the Do start
End Sub                                                                          ' Mark the end of the Subroutine