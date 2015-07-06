======================
Using Prodiguer client
======================

Upon successful `installation <https://github.com/Prodiguer/prodiguer-client/blob/master/docs/installation.rst>`_ of the `prodiguer client <https://github.com/Prodiguer/prodiguer-client>`_ library, supported commands can easily be called from command line.  Listed below are the full set of supported commands alongside command argument descriptions.

**Note** - For each command listed below type -h or --help to access the command's help text.

prodiguer-client-metrics-add
----------------------------

Uploads simulation metrics to remote repository.

**-f, --file**

	Path to a metrics file to be uploaded to server

**--duplicate-action**

	Action to take when adding a metric with a duplicate hash identifier.  **Default = skip**.

	**skip** = duplicate metrics are ignored.

	**force** = existing metrics are overwritten.

prodiguer-client-metrics-add-batch
----------------------------

Uploads a batch of simulation metrics to remote repository.

**-d, --directory**

	Path to a directory in which are metrics files to be uploaded to server

**--duplicate-action**

	Action to take when adding a metric with a duplicate hash identifier.  **Default = skip**.

	**skip** = duplicate metrics are ignored.

	**force** = existing metrics are overwritten.

prodiguer-client-metrics-delete
----------------------------

Deletes simulation metrics from remote repository.

**-g, --group**

	A metrics group identifier.

**-f, --filter**

	Path to a metrics filter to be applied.

prodiguer-client-metrics-fetch
----------------------------

Fetches a set of simulation metrics from remote repository.

**-g, --group**

	A metrics group identifier.

**-f, --filter**

	Path to a metrics filter to be applied.

prodiguer-client-metrics-fetch-columns
----------------------------

Fetches columns associated with a set of simulation metrics from remote repository.

**-g, --group**

	A metrics group identifier.

prodiguer-client-metrics-fetch-count
----------------------------

Fetches count associated with a set of simulation metrics from remote repository.

**-g, --group**

	A metrics group identifier.

**-f, --filter**

	Path to a metrics filter to be applied.

prodiguer-client-metrics-fetch-file
----------------------------

Fetches a set of simulation metrics from remote repository and saves them to local file system.

**-g, --group**

	A metrics group identifier.

**-f, --filter**

	Path to a metrics filter to be applied.

**-o, --output-dir**

	Directory to which downloaded metrics files will be written.

prodiguer-client-metrics-fetch-setup
----------------------------

	Fetches setup data associated with a set of simulation metrics.

**-g, --group**

	A metrics group identifier.

**-f, --filter**

	Path to a metrics filter to be applied.

prodiguer-client-metrics-fetch-list
----------------------------

Fetches list of all simulation metric group names.

prodiguer-client-metrics-format
----------------------------

Formats simulation metrics in readiness for upload.

**-g, --group**

	A metrics group identifier.

**-i, --input-dir**

	Directory containing unformatted metrics files.

**-o, --output-dir**

	Directory to which reformatted metrics files will be written.

prodiguer-client-metrics-rename
----------------------------

Renames a set of simulation metrics.

**-g, --group**

	A metrics group identifier.

**-n, --new-name**

	New metrics group identifier.

prodiguer-client-metrics-set-hashes
----------------------------

Reassigns hash identifiers for a set of simulation metrics.

**-g, --group**

	A metrics group identifier.
