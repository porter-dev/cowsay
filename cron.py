"""
starts a one-off process
"""
import signal
import time

from shared import consume_cpu, consume_memory, handle_signal, is_exiting


def main():
    """
    starts a no-op task that consumes resources
    """
    print("consuming cpu")
    consume_cpu()
    print("consuming memory")
    consume_memory()
    print("sleeping for 70 seconds")
    time.sleep(70)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_signal)

    main()
