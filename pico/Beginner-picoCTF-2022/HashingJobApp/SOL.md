# HashingJobApp
- Connect to the instance via the generated command
- Use the built in md5sum command for each string as follows: `echo -n (string) | md5sum`, which will print out the md5 hash of the string. Three times will get you the flag.
    - The reason why you need the `echo` command is because md5sum takes in either a filename (and it checks that it is a file), or takes in stdin