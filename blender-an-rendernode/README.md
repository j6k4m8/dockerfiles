# blender-an-rendernode

A render node for Blender, with Animation Node support


## to build:
```
# from this directory:
docker build --rm -t blender-an .
```

## to use:

```
docker run --rm blender-an -b -v $(pwd):/mnt/pwd my-file.blend -o //results/####.png -a
```
