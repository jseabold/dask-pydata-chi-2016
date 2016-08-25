import dask.array as da

x = da.arange(2500, chunks=25)
z = x ** .5
z[-1]

print(z[-1].compute())
