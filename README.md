# yk-file-service
yk-file-service是一个文件上传服务端，基于Python Flask框架。它提供了文件上传和文件下载功能，并支持自动构建Docker镜像。

### Docker镜像创建命令
要使用Docker部署和运行yk-file-service，你可以按照以下步骤执行Docker镜像创建命令：

### 构建Docker镜像:

``` plaintext
docker build -t file-service .
```
### 运行Docker容器:

``` plaintext
docker run -d --name cdn-service -p 3976:3000 -v /uploads:/docker/cdn/uploads --restart=always 67371c375779e27e3f31cd95356f1f24cd0ee0ea79e93
```
请注意，上述命令中的67371c375779e27e3f31cd95356f1f24cd0ee0ea79e93是替代为你自己的镜像ID。

### 使用说明
文件上传：

启动容器后，可以通过POST接口 http://localhost:3976/upload 实现上传。
在页面上选择要上传的文件，并点击"上传"按钮。
上传的文件将被保存在/uploads目录中。
### 文件下载：

要下载已上传的文件，请访问http://localhost:3976/upload/<filename>，其中<filename>是要下载的文件名。
### 注意事项
请确保已经安装了Docker，并且具有足够的权限来执行上述命令。
在运行Docker容器之前，确保/uploads目录存在并且具有适当的权限。
以上是一个基本的README文件示例，你可以根据实际情况进行修改和扩展。
