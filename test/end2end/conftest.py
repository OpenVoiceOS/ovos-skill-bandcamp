try:
    import ovoscope  # noqa: F401
except ImportError:
    collect_ignore_glob = ["*.py"]
