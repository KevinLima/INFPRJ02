# INFPRJ02
Git project for INFPRJ02 by group 2.

## Projectmembers
- Pim Bazuin
- Dave Caron
- Kevin Lima
- Mitchell van der Staal 
- ~~Duncan Sumter~~ (RIP)

## Install mysqlclient

### Prerequisites

You may need to install the Python and MySQL development headers and libraries like so:

`sudo apt-get install python-dev libmysqlclient-dev`  # Debian / Ubuntu

`sudo yum install python-devel mysql-devel`  # Red Hat / CentOS

On Windows, there are binary wheel you can install without MySQLConnector/C or MSVC. 

#### Note on Python 3 : if you are using python3 then you need to install python3-dev using the following command :

`sudo apt-get install python3-dev` # debian / Ubuntu

`sudo yum install python3-devel `  # Red Hat / CentOS

`brew install mysql-connector-c`  # macOS (Homebrew)

### Install from PyPI

`pip install mysqlclient`

NOTE: Wheels for Windows may be not released with source package. You should pin version
in your `requirements.txt` to avoid trying to install newest source package.


### Install from source

1. Download source by `git clone` or [zipfile](https://github.com/PyMySQL/mysqlclient-python/archive/master.zip).
2. Customize `site.cfg`
3. `python setup.py install`