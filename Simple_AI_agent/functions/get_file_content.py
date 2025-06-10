import os

def get_file_content(working_directory, file_path):
    """
    Reads the content of a file from a specified directory.

    :param working_directory: The directory where the file is located.
    :param file_path: The path to the file relative to the working directory.
    :return: The content of the file as a string, or None if the file does not exist.
    """

    file_path_lvls = file_path.split('/')
    
    try:
        join_dir = os.path.join(working_directory, file_path)
    except TypeError:
        return "Error: Invalid type for 'file_path'. It should be a string or None."
    
    contents = os.listdir(working_directory)
    if (file_path_lvls[0] not in contents) and (file_path_lvls[0] not in ['.']):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(join_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    with open(join_dir, 'r') as file:
        file_content_string = file.read(MAX_CHARS)

        if len(file.read()) > MAX_CHARS:
            file_content_string += f'\n\n[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string