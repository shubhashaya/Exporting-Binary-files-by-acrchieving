from tkinter import *
from tkinter import messagebox
from zipfile import ZipFile
import shutil
import os.path
import sys
import subprocess
import zipfile, os
import logging

def clear(): 
    #clearing the column
    Source_field.delete(0, END) 
    Destination_field.delete(0, END)

#Temporary files deletion
def delete_files():
    folder ="\\tmp"
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logging.info(e)

def insert(): 

    #checking for Empty string  
    if (Source_field.get() == "" and
        Destination_field.get() == ""):
        messagebox.showinfo('Message', 'Enter Valid Path')      
        print("empty input") 
    else:
        #For valid path performing Zip and copying to destination path.
        Source_Path=Source_field.get()
        Destination_Path=Destination_field.get()
        print(Source_Path,Destination_Path)

        handle=zipfile.ZipFile('Zipped_binary.zip','w')
        
        for x in os.listdir(Source_Path):
            try:
                
                if x.endswith('.py'):
                    handle.write(x,compress_type=zipfile.ZIP_DEFLATED)
                    
                    #logs every binary file that is extracted.
                    logging.basicConfig(filename="logged_file.log", 
                        format='%(asctime)s %(message)s', 
                        filemode='w')   
                    logger=logging.getLogger() 
                    logger.setLevel(logging.DEBUG)
                    logger.info("This file"+" "+x +" "+"is zipped")

                    handle.close()
                    newPath = shutil.copy('Zipped_binary.zip',Destination_Path)
                    newPath = shutil.copy('logged_file.log',Destination_Path)

                    #Successful message prompt after the Zip is performed.
        
                    messagebox.showinfo('Message', 'Files Zipped Successfully!!!')
                    messagebox.showinfo('Message', 'Zipped Files are exported to Destination Path')
                    handle.close()
                    sys.exit()

            except Exception as e:
                    logging.info(e)
                    print("Binary files are fetched or empty")
                    handle.close()
                    sys.exit()

# Driver code 
if __name__ == "__main__": 
           
    root = Tk() 
    root.configure(background='light green')      
    root.title("Assessment") 
    root.geometry("500x300")

    
    heading = Label(root, text="Zipping Binary File", bg="light green") 
    Source = Label(root, text="Source_Path", bg="light green")   
    Destination = Label(root, text="Destination_Path", bg="light green") 
    
    heading.grid(row=0, column=1) 
    Source.grid(row=1, column=0) 
    Destination.grid(row=2, column=0) 
       
    Source_field = Entry(root) 
    Destination_field = Entry(root)
    
    Source_field.grid(row=1, column=1, ipadx="100") 
    Destination_field.grid(row=2, column=1, ipadx="100")
    
    #Submit button calls Zipping functionality called 'insert' function
    
    submit = Button(root, text="Submit", fg="Black", 
                            bg="Red", command=insert)
    submit.grid(row=8, column=1) 
    root.mainloop()
    delete_files()
    
