===================================
Prodiguer Client Installation Guide
===================================

Installing the prodiguer client library is simple & straightforward.

Step 1: Install python dependencies
----------------------------

The prodiguer client library requires the following python libraries both of which can be installed via pip:

- **arrow**

- **requests**

Step 2: Clone library from GitHub
----------------------------

cd YOUR_WORKING_DIRECTORY
git clone https://github.com/Prodiguer/prodiguer-client.git

Step 3: Set library environment variables
----------------------------

Edit either $HOME/.bash_profile or $HOME/.bash_rc and setup your environment so that the prodiguer client library is correctly initialised::

	export PYTHONPATH=$PYTHONPATH:**YOUR_WORKING_DIRECTORY**/prodiguer-client
	export PRODIGUER_CLIENT_WEB_URL='https://prodiguer-test-web.ipsl.fr'
	source **YOUR_WORKING_DIRECTORY**/prodiguer-client/aliases.sh

Step 4.	Command line usage
----------------------------

Open a new terminal session in order to activate the prodiguer client library.  Full usage instructions are documented `here <https://github.com/Prodiguer/prodiguer-client/blob/master/docs/usage.rst>`_.