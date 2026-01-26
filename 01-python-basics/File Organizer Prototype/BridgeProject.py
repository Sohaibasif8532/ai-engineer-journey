
    class FileOrganizer:


        def Organize(FilesInput):

            folders = {
                "Images": (".jpg", ".png", ".jpeg"),
                "Audio": (".mp3", ".wav", ".flac"),
                "Video": (".mp4", ".avi", ".mkv"),
                "Documents": (".pdf", ".doc", ".docx"),
                "Archives": (".zip", ".rar", ".7z"),
                "Scripts": (".py", ".js", ".java")
            }
            summary={folder: 0 for folder in folders}
            summary["Other"]=0
            for file in FilesInput:
                moved=False
                for folder, extensions in folders.items():
                    if file.lower().endswith(extensions):
                        print(f"{file} -> {folder}/")
                        summary[folder]+=1
                        moved=True
                        break
                if not moved:
                    print(f"{file} -> Other/")
                    summary["Other"]+=1
        
            print("Summary:", summary)

    FileOrganizer.Organize(["file1.txt", "file2.jpg", "file3.mp3"])