import tkinter as tk

from dataclasses import dataclass, asdict

import os

from json_serializable import JsonSerializable
from file_handler import FileHandler
from uproject import UProject


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Config(JsonSerializable):
    project_name: str
    template_folder: str
    relative_dir: str
    source_dir: str
    template: str


class ModuleCreator:
    padx = 20
    pady = 20

    config: Config

    module_base: str
    module_name: str

    def __init__(self, config_path):
        self.window = tk.Tk()

        self.window.title("Create Unreal Module")


        tk.Label(self.window, text="Module Base").grid(row=0, padx=self.padx, pady=self.pady)
        tk.Label(self.window, text="Module Name").grid(row = 1, padx=self.padx, pady=self.pady)

        self.base_entry = tk.Entry(self.window)
        self.name_entry = tk.Entry(self.window)

        self.base_entry.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.name_entry.grid(row=1, column=1, padx=self.padx, pady=self.pady)



        self.create_button = tk.Button(self.window, text="Create", command=self.create_module)
        self.cancel_button = tk.Button(self.window, text="Cancel", command=self.window.destroy)

        # Place button in window
        self.create_button.grid(row=2, column=0, padx=self.padx, pady=self.pady)
        self.cancel_button.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        self.config = Config.from_json_file(config_path)


    def show(self):
        self.window.mainloop()    

    def create_module(self):
        print("Create")

        self.module_base = self.base_entry.get()
        self.module_name = self.name_entry.get()


        copy_dir = os.path.join(ROOT_DIR, self.config.template_folder)
        project_dir = os.path.join(ROOT_DIR, self.config.relative_dir)
        module_dir = os.path.join(
            project_dir, 
            self.config.source_dir,

            self.module_base,
            self.module_name
        )

        # Copy files and replace template in file names and text
        self.handle_files(copy_dir=copy_dir, module_dir=module_dir)

        self.add_to_uproject_file(project_dir)

        self.window.destroy()
        
        
    def handle_files(self, copy_dir: str, module_dir: str):
        handler = FileHandler(
            template_dir=copy_dir,
            module_dir=module_dir,

            template=self.config.template,
            module_name=self.module_name
        )

        handler.copy_template_directory()
        handler.replace_file_name_templates()
        handler.replace_file_text_templates()

    def add_to_uproject_file(self, project_dir: str):
        uproject = UProject.from_json_file(
            os.path.join(
                project_dir, 
                f"{self.config.project_name}.uproject", 
                )
            )
        
        uproject.add_module(self.module_name)
        uproject.save(os.path.join(project_dir, f"{self.config.project_name}.uproject"))