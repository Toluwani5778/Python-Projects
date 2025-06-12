import os


def get_files_info(working_directory, directory=None):
    """
    Get information about files in the specified directory.

    :param working_directory: The base directory to search in.
    :param directory: The specific subdirectory to look into. If None, uses the base directory.
    :return: A list of dictionaries containing file information.
    """
    orig_directory = directory
    try:
        if directory[-1] == "/":
            directory = directory[:-1]
    except TypeError:
        directory = "."

    try:
        join_dir = (
            os.path.join(working_directory, directory)
            if directory
            else working_directory
        )
    except TypeError:
        return "Error: Invalid type for 'directory'. It should be a string or None."

    contents = os.listdir(working_directory)

    if (directory not in contents) and (directory not in ["."]):
        return f'Error: Cannot list "{orig_directory}" as it is outside the permitted working directory'

    if not os.path.isdir(join_dir):
        return f'Error: "{directory}" is not a directory'

    dir_content = ""
    contents = os.listdir(join_dir)
    for content in contents:
        content_path = os.path.join(join_dir, content)
        dir_content += f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={not (os.path.isfile(content_path))}\n"
    return dir_content
