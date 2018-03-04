### 基于Flask Restful框架的Rest API

#### 项目结构

由于Python的项目比较灵活，相对项目结构也比较灵活、多变，该项目结构只是一个参考

```
app 项目主模块
|
|___business 项目业务模块
|
|___common 通用模块
|
|___conf 配置项模块
|
|___models 模型模块（包括数据库模型等）
|
|___util 工具类模块
|
|___resources 资源类模块
|
|___main.py Flask应用模块
|
|___db.py 数据库模块
|
|docs 项目文件
|
|manage.py 程序入口，可以使用Flask-Script定义相关命令
|
|.pylintrc 定义项目编写规范(基于Pep8)
|
|requirements.txt 项目所需第三方模块
```


#### 项目所用技术
* Flask：Python Web方向一个主流模块
* Flask-RESTFUL：Flask 扩展，它添加了快速构建 REST APIs 的支持
* Flask-SQLAlchemey：ORM插件
* Flask-Script：使Flask应用可以通过命令行来运行服务器
* Flask-Migrate：数据迁移工具
* flask-restful-swagger：帮助项目生成对应的API文档

#### 参考资料
* [Django和Flask这两个框架在设计上各方面有什么优缺点？](https://www.zhihu.com/question/41564604)
* [flask-restful中文](http://www.pythondoc.com/Flask-RESTful/)
* [flask-sqlchemey中文](http://www.pythondoc.com/flask-sqlalchemy/)
