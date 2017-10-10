# PyGenRetrieve
This is a very simple software for retreiving data from **NCBI GTR** (Genetic Testing Registry).

The program receives a search string, *"breast cancer"* or *"epilepsy"*, the number of pages in NCBI GTR (sorry for this, for now it has to be an input parameter), and finally an output name for saving. Using these values, the program opens every page in this querry, and saves a text file with all the genes related to the searched condition.

In order to the app to work, you must install some extra libraries. For **Ubuntu/Debian** based systems, run:

**`apt install python3-pandas python3-html5lib python3-bs4 python3-pyqt4`**

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of **MERCHANTABILITY** or **FITNESS FOR A PARTICULAR PURPOSE**.  See the GNU General Public License attached for more details.

Thanks, for downloading! Any feedbacks and/or forks are welcome.
