import os


def write_file(working_directory, file_path, content):
    """
    Write content to a file in the specified working directory.

    :param working_directory: The directory where the file will be created.
    :param file_path: The path of the file to write, relative to the working directory.
    :param content: The content to write into the file.
    """

    file_path_lvls = file_path.split("/")

    try:
        full_path = os.path.join(working_directory, file_path)
    except TypeError:
        return "Error: Invalid type for 'file_path'. It should be a string or None."

    contents = os.listdir(working_directory)
    if (
        (file_path_lvls[0] not in contents)
        and (file_path_lvls[0] not in ["."])
        and (len(file_path_lvls) > 1)
    ):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
    try:
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except:
        return f"Error: {file_path} is not a file to be written to"
