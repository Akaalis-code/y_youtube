## APT :
    Advanced Packaging Tool is a package manager in Debian-based Linux distributions
    
    To install any package 
        > sudo apt install <Package_name>

    To check all the installed packges through apt 
        > apt list --installed                                      # Gives all installed packages
        > apt list | grep -i <any_package_you_are_looking_for>      # Grep helps you filter out with the package name you are looking for

    To uninstall the apt installed package 
        > sudo apt remove <package_name>        # This only uninstalls the package but any local confguratons will stay
        > sudo apt purge <package_name>         # This will remove any pre existing config files 
        > sudo apt autoremove                   # This will remove any unused dependent libraries that were auto installed


## Get file or folder sizes 
    
    Use "du" command which is short for (disk usage)
    To get how to use "du" command run below command
        > du --help 
    Generally if you want to find out size of any folder run below 
        > du -sh folder_name           # 's' argument simplifies and summarizes the output 'h' isplays size in human readable form