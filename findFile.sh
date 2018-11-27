find /home/ -print0 2> /dev/null | while IFS=""  read -r -d "" file ; do [ -d "$file"  ] &&  [ -w "$file" ]  && echo "$file" is writeable ; done
