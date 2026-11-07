import asyncio
import C_router
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
        final=asyncio.run(C_router.output())
        C_router.json_dump(final)
        logger.info("请求成功")
    except Exception:
        logger.exception("请求失败")
        raise

main()

#venv 和 pip 分别负责什么？
#为什么不同 Python 项目需要独立的虚拟环境？
#requirements.txt 有什么作用？
#为什么不能直接提交 .venv 到 Git？
#logging 相比 print() 有哪些优势？
#.env 和命令行参数同时配置时，如何设计优先级？

#1.负责独立运行环境和在环境中安装包
#每个python项目所使用的包是不一样的，使用独立虚拟环境可以保证项目迁移到别的设备时成功运行
#3.显示环境已装包，一键安装所需包
#4.
#5.更详细且可以输出到别的文件中
#6.一般情况下命令行参数优先

#补充：4.
# 体积大：虚拟环境可能包含大量第三方库，增加仓库体积。
# 平台差异：Windows 和 Linux 的 Python 环境不能直接通用。
# 可重建：可以通过 venv 创建环境，再通过 requirements.txt 安装依赖。