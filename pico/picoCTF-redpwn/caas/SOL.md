# caas
- Open the given page and download the js file
- From the file, we see that it will cowsay anything that we send to it
- Therefore, we should try to command inject or escape the cowsay command. The way to do this is by using the `;` character so that we can end the cowsay command and run a command of our own. I sent `/cowsay/bad; ls` to run the ls command, then `/cowsay/bad; cat falg.txt` to get the flag