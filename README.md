## Welcome to the Bioinformatics Working Group @ [UC Santa Barbara](https://www.ucsb.edu/)

All materials from our sessions will be posted in this repository. 

---
### Week 1: [Introduction to NGS technologies and Linux Basics](https://github.com/tarunaaggarwal/bwg-s19/blob/master/presentations/Week1-Intro2NGStech-LinuxBasics.pdf)


A. **How to generate and copy an SSH key to login into remote servers automatically**. More detailed instructions are [here](https://www.ssh.com/ssh/copy-id#sec-Setting-up-public-key-authentication).

1. To generate SSH key, run `ssh-keygen`. The output will something like this:

![SSH key output](https://www.dropbox.com/s/d9e2oaay4d97sb9/ssh-key-image.png?raw=1)

2. Next, copy your SSH key to the remote server by running `ssh-copy-id -i ~/.ssh/mykey user@pod.cnsi.ucsb.edu`

You may have to enter your password again.

3. To test the key, run `ssh -i ~/.ssh/mykey user@host`. Now you should be able to login without typing your password.
	


