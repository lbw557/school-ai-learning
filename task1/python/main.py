import asyncio
import router
import logging
def main()->None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s - %(message)s",
        filename="app.log",
        encoding="utf-8"
    )
    logger = logging.getLogger(__name__)
    logger.info("开始请求")
    try:
        final=asyncio.run(router.output())
        router.json_dump(final)
        logger.info("请求成功")
    except Exception:
        logger.exception("请求失败")
        raise
if __name__ == "__main__":
    main()

