# Fonero GUI Wallet

Copyright (c) 2018, The Fonero Project (www.fonero.org)

# Installation & running from source codes

1. Clone the repo:
		
		git clone https://github.com/fonero-project/fonero-gui-lite

2. Install dependencies (with Python 2.7):

	* Generally, you can use Python `pip` to install required components:
		
			pip install PySide, requests, psutil
	
	* or
			
			pip install -r requirements.txt 
	
	* On some OSes, PySide may be required to install from pre-built packages. For example, on Ubuntu 16.04, install PySide with the following command:
			
			sudo apt install python-pyside


3. Build/download Fonero binaries from [Fonero repo](https://github.com/fonero-project/fonero) and put them to `Resources/bin` sub-directory.

4. Run the wallet (Python 2.7):
		
		cd /path/to/fonero-gui-lite
		python wallet.py
