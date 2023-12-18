# Packaging and Distributing:

This will explain how to convert our python application into executable files for different operating systems using pyinstaller and what are the different ways of doing it.

- There are two options for packaging that is "one-file" and "one-folder" methods

- The one-file method will convert all our dependencies into a single executable file but it is comparatively slower than one folder

- The one-folder method will convert all our dependencies into a single executable folder.

- In the one-folder method the assets or data files are stored in the folder that contains the app so the app can easily access it

- In the one-file method the assets and other data will be extracted when executed and stored in the temp folder of our system for execution, that's why it is slower.

- one-file method command is pyinstaller `pyinstaller main.py --onefile`

- one-folder method command is pyinstaller `pyinstaller main.py`

- to add the assets in the one-folder command `pyinstaller main.py --add-data "data_folder_name;destination_folder_name"`

- to add the assets in the one-file we need to change the file path in the source_code to the temp file path

- sample code:

        bundle_dir = getattr(
            sys, "_MEIPASS", path.abspath(path.dirname(__file__))
        )
        snake_image_path = path.join(bundle_dir, "images", "snake.png")
        snake_body = Image.open(snake_image_path)
    

- to add the assets in the one-file command `pyinstaller main.py --add-data "data_folder_name;destination_folder_name"`

- To avoid the opening of the terminal in windows for our app add `--windowed` to the end