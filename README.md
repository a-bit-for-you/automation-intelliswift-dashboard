# Installation steps

**1. Anaconda Installation**

Install anaconda from the official anaconda site. 
https://www.anaconda.com/
After installing anaconda you need to restart the terminal
To activate anaconda type conda activate.
To deactivate anaconda type conda deactivate.
 

**2. Selenium Installation**

For windows :
Click on start and search for anconda terminal.
Open the terminal and type : conda install selenium

For linux :
Open terminal and type : 
conda activate
conda install selenium

**3. Downloading the web driver.**
Visit https://www.seleniumhq.org and click on download button.
Then search for the Google Chrome Driver.
Then download the driver which is Latest stable release ChromeDriver.

You need to provide the path of the chrome driver in your code.
eg. driver=webdriver.Chrome('/home/intelliswift/sachin/yo/chromedriver')#location of the chrome driver

Now you can run your program. 
(Note for linux users : Don't forget to enter into the virtual environment by typing conda activate).


**Setting the crontab in linux :**

type env > a in terminal and search for environment variables and you will get the following values :
DISPLAY=:0
XAUTHORITY=/run/user/1000/gdm/Xauthority
PATH=/home/intelliswift/anaconda3/condabin:/home/intelliswift/.local/bin:/home/intelliswift/bin:/opt/apache-maven/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin
Then copy paste the above lines in the crontab and finally set the crontab.

**Crontab examples :**

#Morning monday to friday

24 07 * * 1-5 /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py morning>> /home/intelliswift/tools/selenium/logs/dcheck_morning.out 2>&1

#Afternoon monday to friday

54 11 * * 1-5 /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py afternoon>> /home/intelliswift/tools/selenium/logs/dcheck_afternoon.out 2>&1

#Evening monday to friday

24 15 * * 1-5 /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py evening>> /home/intelliswift/tools/selenium/logs/dcheck_evening.out 2>&1

#saturday 

54 11 * * 6 /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py saturday>> /home/intelliswift/tools/selenium/logs/dcheck_saturday.out 2>&1

#sunday

54 11 * * 7 /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py sunday>> /home/intelliswift/tools/selenium/logs/dcheck_sunday.out 2>&1

#input feed check saturday and sunday

50 11 * * 6-7 /usr/bin/python3 /home/intelliswift/tools/selenium/input_feed_check.py inputfeed>> /home/intelliswift/tools/selenium/logs/input_feed_check.out 2>&1
