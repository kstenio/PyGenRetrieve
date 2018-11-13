# PyGenRetrieve (v1.2)
This is a very simple software for retreiving data from **NCBI GTR** (Genetic Testing Registry).

The program receives a search string, *"breast cancer"* or *"epilepsy"* and an output name for saving. Using these values, the program opens every page in GTR and saves a text file (in the same folder as the app) with all the genes related to the searched condition (disease).

In order to the app work properly, you must install some extra libraries. For **Ubuntu/Debian** based systems, run:

**`apt install python3-pandas python3-html5lib python3-bs4 python3-pyqt5 python3-lxml`**

It would also be recommended to enable execute bit for the py file:

**`chmod +x pgr.py`**

After that, you can double click or run from a terminal: `./pgr.py`

If you use **Windows**, you can use the standalone install package in the *win* folder. Install it and then run the `pgr.exe` file

---

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of **MERCHANTABILITY** or **FITNESS FOR A PARTICULAR PURPOSE**.  See the GNU Affero General Public License version 3.0 attached for more details.

Thanks, for downloading! Any feedbacks and/or forks are welcome.
