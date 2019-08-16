# sheepit
> Spin up a SheepIt renderfarm node instance.

Run with environment variables for login and password:

```
docker run -it --rm --cpus=6 -e LOGIN=XXXXXX -e PASSWORD=XXXXXX sheepit
```

You can specify the number of CPUs to use at the docker daemon level rather than with command line flags in order to let Docker best handle which CPUs are in use.
