# sheepit
> Spin up a SheepIt renderfarm node instance.

Run with environment variables for login and password:

```shell
docker run -it --rm --cpus=6 -e LOGIN=j6m8 -e PASSWORD=sTXvN1eECcf44BUIMCLKevUt8UQ2gzdnHjzcrcME j6k4m8/sheepit
```

You can specify the number of CPUs to use at the docker daemon level rather than with command line flags in order to let Docker best handle which CPUs are in use.
