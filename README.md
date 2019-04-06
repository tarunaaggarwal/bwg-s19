## Welcome to the Bioinformatics Working Group @ [UC Santa Barbara](https://www.ucsb.edu/)

All materials from our sessions will be posted in this repository. 

---
### Week 1: [Introduction to NGS technologies and Linux Basics](https://github.com/tarunaaggarwal/bwg-s19/blob/master/presentations/Week1-Intro2NGStech-LinuxBasics.pdf)

---
---

### A. **How to generate and copy an SSH key to login into remote servers automatically**. More detailed instructions are [here](https://www.ssh.com/ssh/copy-id#sec-Setting-up-public-key-authentication).

<span style="color:blue; font-size:1.5em;"> **Mac Users** </span>


* NOTE: The command prompts are underlinded in pink in the image below.  

1. To generate SSH key, run `ssh-keygen`. 
2. When asked to `Enter file in which to save the key (/Users/YOURNAME/.ssh/id_rsa):`, just hit enter and DO NOT specify a file name. As you will notice here, the file is already set so we don't need to type another name.

 ![SSH key output](https://www.dropbox.com/s/tel2ic79jcf9pfl/ssh-key-4-macs.png?raw=1)

3. When asked to `Enter passphrase (empty for no passphrase):`, just hit enter again and do not worry about creating a passphrase.

4. Hit enter again to confirm you don't want a passphrase.

5. You should get a message saying 
```
Your identification has been saved in /Users/YOURNAME/.ssh/id_rsa.
Your public key has been saved in /Users/YOURNAME/.ssh/id_rsa.pub.
```
6. Double that your files are in the right directory by running `ls ~/.ssh`. You should see two files starting with `id_`.
7. Next, copy your SSH key to the remote server by running `ssh-copy-id -i ~/.ssh/mykey user@pod-login1.cnsi.ucsb.edu`

You may have to enter your password again.

8. To test the key, run `ssh -i ~/.ssh/mykey user@pod-login1.cnsi.ucsb.edu`. Now you should be able to login without typing your password.
	

<span style="color:blue; font-size:1.5em;"> **PC Users** </span>

1. Please follow the instructions in [this online tutorial](https://www.youtube.com/watch?v=DDjSjC4SAYM) with a couple of caveats
	
	a. You do not need to `mkdir` an `~/.ssh` directory because it should already. In case it is not, only then make it and follow the instructions in the video.
	
	b. You do not need to change the port 22. 
	
2. Remember that under the `hostname`, you have to type `pod-login1.cnsi.ucsb.edu`. The dude in the video types an IP address.


---
---
#### B. **Practice Makes Perfect** 
It would be great if you are able to run through this [Software Carpentry Shell Novice Tutorial](http://swcarpentry.github.io/shell-novice/) before next week. This way we don't have to spend too much reviewing and move into Qiime2 right away. 

