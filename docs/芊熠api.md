# 芊熠智慧停车出入相机API接口

## 1. 心跳包

- 方法：POST
- URL：/api/heartbeat
- 参数：
  - timestamp: 时间戳（格式：yyyy-MM-dd HH:mm:ss）
  - sn: 设备序列号
- 响应：  

```json
  {
    "code": 0,
    "msg": "success"
  }  ```

- 描述：相机定期发送心跳包，用于检测相机在线状态

## 2. 车牌识别结果上报

- 方法：POST
- URL：/api/recognition
- 参数：
  - timestamp: 识别时间（格式：yyyy-MM-dd HH:mm:ss）
  - plateNumber: 车牌号码
  - confidence: 置信度
  - imageUrl: 车辆图片URL
  - sn: 设备序列号
- 响应：

  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "gateControl": "open" // 或 "close"
    }
  }  ```

- 描述：相机识别到车牌后，上报识别结果

## 3. 获取白名单

- 方法：GET
- URL：/api/whitelist
- 参数：
  - sn: 设备序列号
- 响应：  

```json
  {
    "code": 0,
    "msg": "success",
    "data": [
      {
        "plateNumber": "京A12345",
        "startTime": "2023-05-01 00:00:00",
        "endTime": "2023-12-31 23:59:59"
      },
      // 更多白名单记录...
    ]
  }  ```

- 描述：相机获取最新的白名单数据

## 4. 设备状态上报

- 方法：POST
- URL：/api/status
- 参数：
  - timestamp: 状态上报时间（格式：yyyy-MM-dd HH:mm:ss）
  - sn: 设备序列号
  - cpu: CPU使用率
  - memory: 内存使用率
  - disk: 磁盘使用率
  - temperature: 设备温度
- 响应：

  ```json

  {
    "code": 0,
    "msg": "success"
  }  ```

- 描述：相机定期上报设备状态信息
