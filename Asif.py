import sys

if sys.version_info[:2] == (3, 11):
    import BNBM
    BNBM.main()

elif sys.version_info[:2] == (3, 13):
    import BNBB
    BNBB.main()

else:
    raise RuntimeError(
        f"Unsupported Python version: {sys.version_info.major}.{sys.version_info.minor}"
    )
