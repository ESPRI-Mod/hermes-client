===================================
HERMES Client Installation Guide
===================================

Installing the HERMES client library is simple & straightforward.

**Note** - it is assumed that git and pip are available.

Step 1: Install python dependencies
----------------------------

The HERMES client library requires the following python 2.7 libraries all of which can be installed via pip::

	pip install arrow
	pip install requests

Step 2: Clone from GitHub
----------------------------

Simply clone from GitHub into your working directory::

	cd YOUR_WORKING_DIRECTORY
	git clone https://github.com/Prodiguer/hermes-client.git

Step 3: Setup shell environment
----------------------------

Edit either $HOME/.bash_profile or $HOME/.bash_rc to setup your shell environment so that the HERMES client library is correctly initialised.  You may cut & paste the following code (remember to define the YOUR_WORKING_DIRECTORY field)::

	# --------------------------------------------------------------------
	# HERMES client settings
	# --------------------------------------------------------------------

	# HERMES: web-service URL.
	export HERMES_CLIENT_WEB_URL='https://hermes-test-web.ipsl.fr'

	# HERMES: activate shell
	source $HERMES_CLIENT_HOME/activate

Step 4.	Command line usage
----------------------------

Open a new interactive terminal session in order to activate the HERMES client commands.  Full usage instructions are documented `here <https://github.com/Prodiguer/hermes-client/blob/master/docs/usage.rst>`_.
