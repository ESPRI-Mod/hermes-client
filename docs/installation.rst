===================================
Prodiguer Client Installation Guide
===================================

Installing the prodiguer client library is simple & straightforward.

**Note** - it is assumed that git and pip are available.

Step 1: Install python dependencies
----------------------------

The prodiguer client library requires the following python libraries all of which can be installed via pip::

	pip install arrow
	pip install requests

Step 2: Clone from GitHub
----------------------------

Simply clone from GitHub into your working directory::

	cd YOUR_WORKING_DIRECTORY
	git clone https://github.com/Prodiguer/prodiguer-client.git

Step 3: Setup environment
----------------------------

Edit either $HOME/.bash_profile or $HOME/.bash_rc and setup your environment so that the prodiguer client library is correctly initialised::

	export PYTHONPATH=$PYTHONPATH:YOUR_WORKING_DIRECTORY/prodiguer-client
	export PRODIGUER_CLIENT_WEB_URL='https://prodiguer-test-web.ipsl.fr'
	source YOUR_WORKING_DIRECTORY/prodiguer-client/aliases.sh

Step 4.	Command line usage
----------------------------

Open a new terminal session in order to activate the prodiguer client library.  Full usage instructions are documented `here <https://github.com/Prodiguer/prodiguer-client/blob/master/docs/usage.rst>`_.