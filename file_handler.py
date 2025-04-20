import shutil
import os


class FileHandler:
    template_dir: str
    module_dir: str

    template: str
    module_name: str

    def __init__(self, template_dir, module_dir, template, module_name):
        self.template_dir = template_dir
        self.module_dir = module_dir

        self.template = template
        self.module_name = module_name

    def copy_template_directory(self):
        try:
            shutil.copytree(src=self.template_dir, dst=self.module_dir, dirs_exist_ok=True)
            print("Copied directory")
        except Exception as e:
            print(f"An error occured: {e}")

    def replace_file_name_templates(self):
        for root, _, files in os.walk(self.module_dir):
            for file in files:
                file_path = os.path.join(root, file)

                if self.template in file_path:
                    os.rename(
                        file_path, 
                        file_path.replace(
                            self.template, 
                            self.module_name
                        )
                    )
                
    def replace_file_text_templates(self):
        for root, _, files in os.walk(self.module_dir):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        content = f.read()

                    updated_content = content.replace(
                        self.template,
                        self.module_name
                    )

                    with open(file_path, "w") as f:
                        f.write(updated_content)

                except Exception as e:
                    print(f"An error occurred: {e}")
