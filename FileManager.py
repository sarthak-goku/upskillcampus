import os
import shutil
from tkinter import Tk, filedialog, messagebox

# Define file type categories
FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css'],
    "Others": []
}


def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Invalid directory selected.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        messagebox.showinfo("Info", "No files to organize.")
        return

    summary = {}

    for file in files:
        file_path = os.path.join(directory, file)
        category = get_category(file)
        category_folder = os.path.join(directory, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        shutil.move(file_path, os.path.join(category_folder, file))

        if category in summary:
            summary[category].append(file)
        else:
            summary[category] = [file]

    # Create summary message
    message = "✅ File Organization Completed!\n\n"
    for category, file_list in summary.items():
        message += f"{category}: {len(file_list)} file(s)\n"
        for f in file_list:
            message += f"  - {f}\n"
        message += "\n"

    messagebox.showinfo("Summary", message)


def browse_and_organize():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Folder to Organize")

    if folder_selected:
        organize_files(folder_selected)


if __name__ == "__main__":
    browse_and_organize()
