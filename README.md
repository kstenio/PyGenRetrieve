# PyGenRetrieve
This is a very simple software for retreiving data from **NCBI GTR** (Genetic Testing Registry).

The program receives a search string, *"breast cancer"* or *"epilepsy"* and an output name for saving. Using these values, the program opens every page in GTR and saves a text file (in the same folder) with all the genes related to the searched condition (disease).

In order to the app work properly, you must install some extra libraries. For **Ubuntu/Debian** based systems, run:

**`apt install python3-pandas python3-html5lib python3-bs4 python3-pyqt4`**

It would also be recommended to enable execute bit for the py file:

**`chmod +x pgr.py`**

After that, you can double click or run from a terminal: `./pgr.py`

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of **MERCHANTABILITY** or **FITNESS FOR A PARTICULAR PURPOSE**.  See the GNU General Public License attached for more details.

Thanks, for downloading! Any feedbacks and/or forks are welcome.

---

**Windows users**: this program can be used in Windows as well, however installation is a little tricky, mostly because of the PyQt4 library.

1. Go to Python website and download latest [Python 3.7.x for Windows](https://www.python.org/downloads/windows/). Also, do not forget to enable **ADD PYTHON TO PATH** during installation!
1. Download the exe installer for PyQt4 ([32-bit](https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py3.4-Qt4.8.7-x32.exe/download) or [64-bit](https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe/download));
1. Install the package. It will show an error message, just ignore it. When asks for Python folder, choose where you installed it (default location would be `C:\Python37`);
1. Download [PyQt4 standalone file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4) provided by *Christoph Gohlke*. The library file must match your Python version (bigger than 3.7) and Windows architecture (probably amd64);
1. Open CMD or Windows PowerShell. Change folder (use **cd**) to where you downloaded PyQt4 whl file;
1. Type **pip install WHLFILE**, where WHLFILE would be something like *PyQt4-4.11.4-cp37-cp37m-win_amd64.whl* (file name may change);
1. If you had no errors, proceed to install remaining libraries. Type: **pip install pandas bs4 html5lib** (internet connection needed).

After that, without errors, you can click on **pgr.py** file and open the program.
