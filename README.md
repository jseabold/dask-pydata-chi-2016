# Dask tutorial for PyData Chicago 2016

Create the environment for this tutorial:

```
conda create -n dask-tutorial -y --no-default-packages --override-channels -c conda-forge -c defaults nomkl graphviz h5py ipython jupyter dask==0.11.0
source activate dask-tutorial
pip install graphviz
```

Start your jupyter notebook:

```
jupyter notebook
```

# Acknowledgements

This notebook draws heavily on many existing Dask materials written by [Matt Rocklin](https://github.com/mrocklin), [Jim Crist](https://github.com/jcrist), and others. Links to these materials are in the notebook.
