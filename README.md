### Web Scraping Scripts
---

A collection of Python scripts I wrote to play around with web scraping with the BeautifulSoup library.

To be able to run these scripts locally, you need to have python3+ on your system. Get it [here](https://https://www.python.org/downloads/ "here"). Make sure to add python.exe to your operating system path variables to be able to run python scripts from the command line.

Navigate into a directory of choice on your local machine and run the following command

```
git clone https://github.com/olamileke/web-scraping.git
```
This will clone this repository onto your system. Up next, navigate into the root of the cloned repo by running

```
cd Web-Scraping
```
At this point, we need to create the virtual machine in which the application will run. Depending on if you are working in a windows or linux environment, follow the instructions found [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ "here") to create the virtual environment.

Activate the virtual environment by running 
```
venv\scripts\activate
```
or 
```
source venv/scripts/activate
```
for windows and linux respectively.  Now, with the virtual environment active, run the following command
```
pip install -r requirements.txt
```
This will install all the application dependences as outlined in the requirements.txt file in the root.

Still in the root and with the virtual environment still active, run

```
python script-of-your-choice.py
```
Please replace 'script-of-your-choice' with any script you intend to run. Say for example *python jobs.py* or *python nytimes.py*

