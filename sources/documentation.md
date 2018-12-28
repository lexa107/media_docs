# Usage of this documentation system
## General
This documentation system consists of several parts:

1. source files placed on harddrive (/media/samsungd3/share/docs/sources)
2. generator (python script)
3. generated html pages placed in the webinterface service folder (/media/services/webinterface)

## Generating html pages
To generate html pages use generate.py script in root of documentation folder. **EXPORT_PATH** from *config.py* is used as destination folder

## Adding new documentation page
1. Place new .md file in *sources* folder
2. Add link to it in *docs.md*

	```
	[Text for the new link](name of the new doc file.html)
	```
3. Regenerate html pages

[Back](docs.html)
