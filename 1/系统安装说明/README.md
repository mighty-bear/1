# 系统安装说明

可以在 Pyhton3.7 + Django 2.2.2 上运行。

1、cd到requirements.txt文件目录下，创建项目的虚拟环境：

```bash
virtualenv venv -p python3
```

2、激活venv环境：

```bash
source venv/bin/activate
```

3、安装 requirements.txt 运行环境依赖

```bash
pip install -r requirements.txt
```

4、创建数据库模型（ORM）

生成应用程序模型:
```python
python manage.py makemigrations
```

迁移模型到数据库：
```python
python manage.py migrate
```

5、 Admin 管理工具
 `http://sitename/admin/` 访问后台管理页面

创建超级用户并设置设置密码：
```python
python manage.py createsuperuser
```

输入命令后，会提示输入`用户名`(区分大小写)，`邮箱`(方便django邮件通知管理员)，`密码`：
```bash
Username: aaa
Email address: aaa@163.com
Password:
Password (again):
Superuser created successfully.
```

6、运行django：

```bash
python manage.py runserver
```
7、浏览器打开 127.0.0.1:8000 访问网站

