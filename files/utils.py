import glob
import logging
import os
import shutil
import typing


def list_contents_of_folder(folder_path: str, extension: typing.Optional[str] = None) -> typing.List[str]:
    """Returns full paths of all files in the folder, does not traverse sub folders

    Parameters
    ----------
    folder_path: str
        full path to folder whose contents are needed
    extension: typing.Optional[str], optional
        if specified only return files ending in extension from folder, by default None

    Returns
    -------
    List of full path of files contained in the folder
    """
    if extension:
        folder_path = os.path.join(folder_path, "*{}".format(extension))
    logging.info("Looking for all files matching: {}".format(folder_path))
    return glob.glob(folder_path)


def delete_folder(folder_path: str, empty: typing.Optional[bool] = True) -> None:
    """Delete specified folder

    Parameters
    ----------
    folder_path : str
        full path to folder that needs to be deleted
    empty : typing.Optional[bool], optional
        if False, delete folder even if its not empty
        if True will not delete a folder that has contents, by default True
    """
    if empty:
        files = list_contents_of_folder(folder_path)
        if len(files) > 0:
            logging.warning("Folder({}) is non empty, has {} files. NOT DELETING".format(folder_path, len(files)))
            return
        else:
            os.rmdir(folder_path)
            return

    shutil.rmtree(folder_path)


def make_folder_if_not_exists(folder_path: str, make_new: typing.Optional[bool] = False) -> None:
    """Make folder and sub folders for the given folder path

    Parameters
    ----------
    folder_path : str
        full path of folder that needs to be created
    make_new : typing.Optional[bool], optional
        if True, delete the existing folder and all its contents and create new folder, by default False
    """
    if os.path.exists(folder_path):
        logging.info("Folder({}) already exists".format(folder_path))
        if not make_new:
            return

        # delete existing folder and contents and re-create folder
        delete_folder(folder_path, empty=False)

    os.makedirs(folder_path)


def move_files(file_paths: typing.List[str], folder_path: str) -> None:
    """move files specified by their full paths to a destination folder

    Parameters
    ----------
    file_paths : typing.List[str]
        List of full paths of files that need to be moved
    folder_path : str
        Full path of destination folder where the files need to be moved
    """
    for fp in file_paths:
        shutil.move(fp, folder_path)


def copy_files(file_paths: typing.List[str], folder_path: str) -> None:
    """copy files specified by their full paths to a destination folder

    Parameters
    ----------
    file_paths : typing.List[str]
        List of full paths of files that need to be copied
    folder_path : str
        Full path of destination folder where the files need to be copied
    """
    for fp in file_paths:
        shutil.copy(fp, folder_path)
