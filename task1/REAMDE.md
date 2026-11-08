### 项目名称：异步并发请求多个 HTTP 接口并汇总结果的脚本

#### 1.项目简介

一个基于 Python asyncio 和 httpx 的异步 HTTP 请求汇总工具。

支持多个 HTTP 接口并发请求，并对请求结果进行统一汇总。

#### 2.功能特性

- 支持多个 HTTP 请求并发执行
- 支持限制最大并发数量
- 支持请求超时控制
- 支持 HTTP 异常处理
- 支持请求结果统一汇总
- 支持 JSON 文件输出
- 支持 logging 日志记录

#### 3.环境要求

anyio==4.16.0
certifi==2026.10.23
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.20
python-dotenv==1.2.4
typing_extensions==4.16.0

#### 4.安装步骤

克隆项目：

    git clone <项目地址>

进入项目目录：

    cd async-http-aggregator

创建虚拟环境：

    python -m venv .venv

激活虚拟环境：

Linux:

    source .venv/bin/activate

Windows:

    .venv\Scripts\activate

安装依赖：

    pip install -r requirements.txt

#### 5.配置说明

项目支持通过 .env 文件配置：

| 配置项          | 说明         | 默认值 |
| --------------- | ------------ | ------ |
| REQUEST_TIMEOUT | 请求超时时间 | 10     |
| MAX_CONCURRENCY | 最大并发数量 | 3      |
|                 |              |        |

#### 6.运行方式

运行程序：

    python main.py

指定并发数量：

    python main.py --max_concurrency 5

指定超时时间：

```
python main.py --timeout 10
```

#### 7.输出说明
- 运行结果保存在 results.json
- 日志保存在 app.log
