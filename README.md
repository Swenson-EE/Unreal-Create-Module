# Unreal Module Creator

This is a simple module creator that allows a user to add the base required files for a module, and add the module to the uproject file.

## Configuration

This project requires a `config.json` file placed in the root directory. Below is the expected structure and description of each field:

```json
{
  "template_folder": "Module Template",
  "relative_dir": "..",
  "source_dir": "Source",
  "template": "[MODULE]",
  "project_name": "TestProject"
}
```

| Key               | Type     | Description                                                   |
| ----------------- | -------- | ------------------------------------------------------------- |
| `template_folder` | `string` | Folder name that holds the module template files              |
| `relative_dir`    | `string` | Path where the project root is relative to the root directory |
| `source_dir`      | `string` | Name of the Source directory                                  |
| `template`        | `string` | Template string used for file name and text replacement       |
| `project_name`    | `string` | Name of the project                                           |
