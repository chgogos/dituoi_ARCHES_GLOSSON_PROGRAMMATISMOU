import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("e4a11.log", mode="w")],
)

logger = logging.getLogger()
logger.handlers[1].setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
logger.handlers[1].setLevel(logging.DEBUG)


def calculate_division(x, y):
    logger.debug(f"Calculating {x} / {y}")
    try:
        result = x / y
        logger.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.exception("Division by zero!")
        return None


calculate_division(10, 2)
calculate_division(5, 0)
