## 人工智能模型部署应用场景

- 设备
PC 浏览器，手机app，微信小程序，服务器，嵌入式开发板，无人车，无人机，Jetson Nano，树莓派，机械臂，物联网设备

- 芯片：CPU GPU TPU NPU VPU等等
- 厂商：英特尔，英伟达，amd，苹果，高通，麒麟等

本地终端，快速实时，硬件多样，算力薄弱，数据隐私

### 模型部署的通用流程pytorch

![[Pasted image 20231110235957.png]]

需要把推理文件放在推理框架上运行
需要在本地硬件上安装ONNX RUNTIME框架

### 模型部署中间格式ONNX

![[Pasted image 20231111000209.png]]

Open Neural Network Exchange

- 开源机器学习通用中间格式，由微软，facebook，亚马逊，ibm发起
- 兼容各种深度学习框架
- 兼容各种推理引擎
- 兼容各种终端硬件
- 兼容各种操作系统
 主页：https://onnx.ai

