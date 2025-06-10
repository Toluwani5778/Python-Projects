import os
import subprocess

def run_python_file(working_directory, file_path):
    """
    Runs a Python file in the specified working directory.
    
    :param working_directory: The directory in which to run the Python file.
    :param file_path: The path to the Python file to be executed.
    """

    file_path_lvls = file_path.split('/')
    
    try:
        full_path = os.path.join(working_directory, file_path)
    except TypeError:
        return "Error: Invalid type for 'file_path'. It should be a string or None."
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    contents = os.listdir(working_directory)
    if (file_path_lvls[0] not in contents) and (file_path_lvls[0] not in ['.']):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        output = subprocess.run(['python', full_path], check=True, text=True, capture_output=True, timeout=30)
        if output.stdout != None:
            return f"STDOUT: {output.stdout}, STDERR: {output.stderr}"
        return "No output produced."

    except subprocess.CalledProcessError as e:
        return f"STDOUT: {e.stdout}, STDERR: {e.stderr}, Process exited with code {e.returncode}" 
        
    except subprocess.TimeoutExpired as e:
        return f"Error: Execution of '{file_path}' timed out after 30 seconds."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"