# Installation steps

1. Anaconda Installation

Install anaconda from the official anaconda site. 
https://www.anaconda.com/
After installing anaconda you need to restart the terminal
To activate anaconda type conda activate.
To deactivate anaconda type conda deactivate.
 

2. Selenium Installation

For windows :
Click on start and search for anconda terminal.
Open the terminal and type : conda install selenium

For linux :
Open terminal and type : 
conda activate
conda install selenium

3. Downloading the web driver.
Visit https://www.seleniumhq.org and click on download button.
Then search for the Google Chrome Driver.
Then download the driver which is Latest stable release ChromeDriver.

You need to provide the path of the chrome driver in your code.
eg. driver=webdriver.Chrome('/home/intelliswift/sachin/yo/chromedriver')#location of the chrome driver

Now you can run your program. 
(Note for linux users : Don't forget to enter into the virtual environment by typing conda activate).

