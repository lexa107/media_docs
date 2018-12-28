# How to make copy of the sdcard

## General

In case of some damages of the sdcard or just for backup purposes you may need to make copy of the sdcard that can be used by raspberry pi as the old one

## Windows

1. Make image of the sdcard using Win32DiskImager software. Note that in case sdcard has several partitions you may select any disk as the source of reading
2. In some cases image of the old card may be bigger than size of the new sdcard. In this case image can be truncated using cygwin
	* open folder with the image in cygwin terminal
	* run fdisk to get info about image data

	```
	/lib/fdisk -lu <name_of_image>
	```

	* note the sector size (mostly it will be 512), and the last sector of the partition
	* to the last sector add 1 and multiply by sector size

	```
	new_size = (last_sector + 1) * sector_size
	```

	* in cygwin terminal run

	```
	truncate --size <new_size> <name_of_image>
	```

3. Write image to the new sdcard using Win32DiskImager
