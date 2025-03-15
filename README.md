# EZ Code Reader


***

## About ez_code_reader

ez_code_reader  is a lightweight tool designed to help developers quickly understand the core logic of code files or projects. 

With concise code (less than 100 lines), it can automatically generate interpretations of code files, including functional overviews, code structure, key methods, and more. 

Whether you're a beginner or an experienced developer, you can easily integrate and use it to accelerate code reading and comprehension.



***

## How to use

1、set `LLM_KEY`,`MODEL_NAME`,  `BASE_URL` in your computer environment

or just set in in the `llm.py` 

2、set `allowed_extensions` and `ignored_extensions` in `reader.py`

default read python files 

3、select a code file or project directory  

```shell
python reader.py agent.py
```



***

for a directory:

```shell
python reader.py .../agent 
```



***

## 关于 ez_code_reader

ez_code_reader 是一个轻量级工具，旨在帮助开发者快速理解代码文件或项目的核心逻辑。通过简洁的代码（少于 100 行），它能够自动生成代码文件的解读，包括功能概述、代码结构、关键方法等。无论是初学者还是资深开发者，都可以轻松集成并使用它来加速代码阅读和理解。



***

## 使用方法

1、在你的计算机环境中设置 `LLM_KEY`、`MODEL_NAME` 和 `BASE_URL`

或者直接在 `llm.py` 文件中设置这些值

2、在 `reader.py` 中设置 `allowed_extensions` 和 `ignored_extensions`

默认读取 Python 文件

3、选择一个代码文件或项目目录

```shell
python reader.py agent.py
```

***

对于目录：

```shell
python reader.py .../agent
```



***

伊织 2025-03-15（六）
