# nbmelt

melt your notebooks if they don't get used!

Usage:

```
pip install nbmelt
jupyter serverextension enable nbmelt
# This notebook server will exit if you don't use it in 30 seconds!
NBMELT_TIMEOUT=30 jupyter notebook
```

```
[I 23:42:27.597 NotebookApp] This notebook will self destruct in 30 seconds! (if you don't use it)
[I 23:42:27.604 NotebookApp] Serving notebooks from local directory: ~/notebooks
[I 23:42:27.604 NotebookApp] 0 active kernels
[I 23:42:27.605 NotebookApp] The Jupyter Notebook is running at:
[I 23:42:27.605 NotebookApp] http://localhost:8888/
[I 23:42:27.605 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[E 23:42:57.600 NotebookApp] No API request received in 30s, exiting.
[I 23:42:57.601 NotebookApp] Shutting down 0 kernels
```
