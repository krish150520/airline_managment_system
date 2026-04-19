try:
    import oracledb
    ORACLE_AVAILABLE = True
except ImportError:
    ORACLE_AVAILABLE = False


def get_connection():
    if not ORACLE_AVAILABLE:
        raise RuntimeError("Run: pip install oracledb")

    return oracledb.connect(
        user="krish",
        password="krish",
        dsn="localhost:1521/XE"
    )