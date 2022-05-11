import win32com.client as win32
import sys
import os
from tqdm import tqdm

def docx2pdf(path_input, path_output):
    path_input, path_output = os.path.abspath(path_input), os.path.abspath(path_output)

    word = win32.Dispatch("Word.Application")    
    doc = word.Documents.Open(path_input)
    doc.SaveAs(path_output, FileFormat=17)
    word.Quit()
    
    print("export: {}".format(path_output))

def hwp2pdf(path_input, path_output):
    path_input, path_output = os.path.abspath(path_input), os.path.abspath(path_output)
    
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
    hwp.XHwpWindows.Item(0).Visible = True
    
    hwp.Open(path_input)
    hwp.HParameterSet.HFileOpenSave.filename = path_output
    hwp.HParameterSet.HFileOpenSave.Format = "PDF"
    hwp.HParameterSet.HFileOpenSave.Attributes = 16384
    hwp.HAction.Execute("FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)

    hwp.Quit()

    print("export: {}".format(path_output))


if __name__ == "__main__":
    form = sys.argv[1]
    dir_folder = sys.argv[2]

    lst_docs = [doc for doc in os.listdir(dir_folder) if form in doc]
    for doc in tqdm(lst_docs):
        
        if form == "hwp":
            hwp2pdf(
                path_input=os.path.join(dir_folder, doc),
                path_output=os.path.join(dir_folder, "{}.pdf".format(doc[:-4]))
            )
        else:
            docx2pdf(
                path_input=os.path.join(dir_folder, doc),
                path_output=os.path.join(dir_folder, "{}.pdf".format(doc[:-5]))            
            )
    
