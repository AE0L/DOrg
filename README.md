# Download's folder Organizer (DOrg)

Organizes downloads folder based on the config file, `dorg.config.ini`. Logs can be found on the `logs.txt` file created after execution.

## Usage

1. Run `dorg.exe`
2. ???
3. Profit

## Config

Sample config file:

```ini
# format for file groups
[GROUP NAME]
folder = folder name
extensions = ['ext1', 'ext2', 'ext3']

# sample file group
[IMAGES]
folder = images
extensions = ['jpg', 'png', 'webm', 'gif']

# please don't remove the following exclusions, just add at the end of the array what you want to be excluded
[EXCLUSIONS]
folders = ['build', 'dist', 'sorted', 'directories', 'unknown']
files = ['dorg.exe', 'dorg.config.ini', 'logs.txt']
extensions = ['py', 'spec']
```