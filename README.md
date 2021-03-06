## Welcome to the Bioinformatics Working Group @ [UC Santa Barbara](https://www.ucsb.edu/)

All materials from our sessions will be posted in this repository. 

---

### Week 1: [Introduction to NGS technologies and Linux Basics](https://github.com/tarunaaggarwal/bwg-s19/blob/master/presentations/Week1-Intro2NGStech-LinuxBasics.pdf)

---

### A. **How to generate and copy an SSH key to login into remote servers automatically**. More detailed instructions are [here](https://www.ssh.com/ssh/copy-id#sec-Setting-up-public-key-authentication).

#### Mac users

* NOTE: The command prompt line is underlinded in pink in the image below.  

1. To generate SSH key, run `ssh-keygen`. 
2. When asked to `Enter file in which to save the key (/Users/YOURNAME/.ssh/id_rsa):`, just hit enter and DO NOT specify a file name. As you will notice here, the file name is already set so we don't need to type another name.

 ![SSH key output](https://www.dropbox.com/s/tel2ic79jcf9pfl/ssh-key-4-macs.png?raw=1)

3. When asked to `Enter passphrase (empty for no passphrase):`, just hit enter again and do not worry about creating a passphrase.

4. Hit enter again to confirm you don't want a passphrase.

5. You should get a message saying 
```
Your identification has been saved in /Users/YOURNAME/.ssh/id_rsa.
Your public key has been saved in /Users/YOURNAME/.ssh/id_rsa.pub.
```
6. Double that your files are in the right directory by running `ls ~/.ssh`. You should see two files starting with `id_`.
7. Next, copy your SSH key to the remote server by running `ssh-copy-id -i ~/.ssh/id_rsa.pub user@pod-login1.cnsi.ucsb.edu`

You may have to enter your password again.

8. To test the key, run `ssh -i ~/.ssh/mykey user@pod-login1.cnsi.ucsb.edu`. Now you should be able to login without typing your password.
	

#### PC users

1. Please follow the instructions in [this online tutorial](https://www.youtube.com/watch?v=DDjSjC4SAYM) with a couple of caveats
	
	a. You do not need to `mkdir` an `~/.ssh` directory because it should already. In case it is not, only then make it and follow the instructions in the video.
	
	b. You do not need to change the port 22. 
	
2. Remember that under the `hostname`, you have to type `pod-login1.cnsi.ucsb.edu`. The dude in the video types an IP address.


---
___
#### B. **Practice Makes Perfect** 
It would be great if you are able to run through this [Software Carpentry Shell Novice Tutorial](http://swcarpentry.github.io/shell-novice/) before next week. This way we don't have to spend too much reviewing, and we can move into Qiime2 right away. 

---

### Week 2: [Introduction to QIIME2](https://github.com/tarunaaggarwal/bwg-s19/blob/master/presentations/Week1-Intro2NGStech-LinuxBasics.pdf)

---

### A. [QIIME2](https://qiime2.org/) is an open-source pipeline used to analyze and visualize microbial diversity. The biggest advantage of using Q2 is the support network. This tool is activately being developed and maintained. Most answers to your questions can be found at the [Q2 Google forum](https://forum.qiime2.org/). 

1. Before we start, let's go over the [terms](https://docs.qiime2.org/2019.1/glossary/) and [core concepts](https://docs.qiime2.org/2019.1/concepts/) QIIME2 developers suggest new users know. 
 
2. Install [anaconda](https://www.anaconda.com/distribution/#linux) and [QIIME2](https://docs.qiime2.org/2019.1/install/native/#install-qiime-2-within-a-conda-environment).

3. `conda activate` your QIIME2 environment. 

---

### Week 8: Making your code and figures more reproducible

---

> **Jupyter notebook** is an open-source application that allows one to create and share interactive code with others. You can create a Jupter notebook for any programming language such as Python and R. 

> **[Binder](https://mybinder.org/)** allows you and other to interact with your notebooks live on a cloud computer. 


### General Rmd, Jupyter, Binder Instructions. For more info, click [here](https://mybinder.readthedocs.io/en/latest/sample_repos.html) or [here](https://kbroman.org/blog/2019/02/18/omg_binder/)

1. How to make an R kernel in Binder? You need the following files:
    - Sample data
    - A R kernel Jupyter Notebook _OR_ an R markdown file
    - A `runtime.txt` file formatted like `r-<YYYY>-<MM>-<DD>`. This file will be used to install the libaries. This file is literally a one-liner containing`r-2019-05-09`.
    - An `install.R` that will be executed for the build. The contents of an example are below.
        
        ```
        install.packages("knitr")
        install.packages("rmarkdown")
        install.packages("vegan")
        install.packages("ggplot2")
        install.packages("ggpubr")
        install.packages("reshape2")
        install.packages("cowplot")
        install.packages("superheat")
        install.packages("plyr")
        install.packages("dplyr")

        source("http://www.bioconductor.org/biocLite.R")
        biocLite("DESeq2")
        biocLite("phyloseq")

        install.packages("devtools")
        devtools::install_github("benjjneb/decontam")

        ```

**IMPORTANT NOTE** 

A. Once you copy your github repo link in Binder, you will need to copy the address that Binder creates (see pink arrow in the image below).

![](https://i.imgur.com/JXluAta.png)

B. Paste this link into your github repo's README and add `?urlpath=rstudio` at the end of the link so that when you share this Binder, the default console will be R studio instead of Jupyter notebook. To get fancy, you can link the Binder with the ![Binder](https://mybinder.org/badge_logo.svg) log. Use the code below to do so.

```
Click to launch Binder: [![Binder](https://mybinder.org/badge_logo.svg)]yy(https://mybinder.org/v2/gh/zeyaxue/Mock_Community2/master?urlpath=rstudio)
```

  
2. How to make a Python
    - An `environment.yml` containing all the Python libraries to install. You can quickly do so by running the following commands.
        ```
        source activate example-env
        conda env export > environment.yml
        ```
    - Your Jupyter notebook. 
    - Save the Binder generated link as described in the **IMPORTANT NOTE** above except do not change the ending. Just save the link as iS in the github repo's README.

