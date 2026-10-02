import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
    
        if args:
            command.extend(args)

        output = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output_string = ""
        if output.returncode != 0:
            output_string += f"Process exited with code {output.returncode}"

        if not output.stdout and not output.stderr:
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {output.stdout}\n"
            output_string += f"STDERR: {output.stderr}"
        
        return output_string
                
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file with optional arguments",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to python file to execute, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Arguments to be supplied to the python function when running it",
                }
            },
        },
    },
}