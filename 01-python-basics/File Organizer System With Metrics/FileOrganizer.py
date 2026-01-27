import os
import shutil

class FileOrganizer:

    @staticmethod
    def Organize():

        folders = {
            "Images": (".jpg", ".png", ".jpeg"),
            "Audio": (".mp3", ".wav", ".flac"),
            "Video": (".mp4", ".avi", ".mkv"),
            "Documents": (".pdf", ".doc", ".docx"),
            "Archives": (".zip", ".rar", ".7z"),
            "Scripts": (".py", ".js", ".java")
        }
        
        for folder in list(folders.keys()) + ["Other"]:
            if not os.path.exists(folder):
                os.mkdir(folder)

        files = os.listdir()
        summary = {folder: 0 for folder in folders}
        summary["Other"] = 0

        for file in files:
            if os.path.isfile(file):
                moved = False

                for folder, extensions in folders.items():
                    if file.lower().endswith(extensions):
                        shutil.move(file, folder)
                        print(f"{file} -> {folder}/")
                        summary[folder] += 1
                        moved = True
                        break

                if not moved:
                    shutil.move(file, "Other")
                    print(f"{file} -> Other/")
                    summary["Other"] += 1

        print("\nSummary:", summary)

FileOrganizer.Organize()
