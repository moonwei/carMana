# 智慧相机管理服务平台

这是一个基于 Python + Flask + SQLite 的 API 服务，用于实现相机管理功能。

## 功能

1. 相机管理：对多个进出口相机实现添加、修改、删除、查询功能，并记录在 SQLite 数据库中。
2. 白名单管理：车辆白名单在数据库中的增删查改功能，并按照要求和相机中的白名单进行比对，提供界面后确认后对相机的白名单进行同步。
3. 相机状态管理：相机心跳信号采集和回复。
4. 车牌识别结果管理：接收车牌识别结果，并记录在 SQLite 数据库中。
5. 数据统计和导出功能：对车牌识别结果进行统计，并提供导出功能。

## 运行说明

1. 安装依赖：

   ```bash

   pip install -r requirements.txt
   ```

2. 运行应用：

   ```bash

   python run.py
   ```

3. 访问 API：
   应用将在 http://127.0.0.1:5000/ 运行。您可以使用 Postman 或其他 API 测试工具来测试各个接口。

## API 文档

详细的 API 文档请参考 `docs/芊熠api.md` 文件。
