# 持续集成：使用Jenkins API创建视图
[持续集成：通过Jenkins API创建项目和节点](https://blog.csdn.net/u010698107/article/details/126923744)介绍了使用jenkins API来创建项目和新建节点，jenkins API也可以创建视图（view）。



## 1. 获取视图配置文件

jenkins API创建视图（view）和创建项目类似，通过一个视图配置文件，发送post请求来创建。

视图配置文件可通过如下步骤获取：

1. 手动在jenkins创建一个视图，例如我创建一个名为myview的视图。
2. 访问[http://192.168.30.8:8080/view/myview/config.xml](http://192.168.30.8:8080/view/myview/config.xml)，这个就是视图myview的配置文件，保存到本地(view.xml)。192.168.30是我的jenkins服务器地址。

![](continuous-integration-for-jenkins-api-create-view/view-config.png)

如果不保存为文件，需要赋给某个变量，可以使用[xml压缩工具](http://www.jsons.cn/xmlformat/)压缩一下：

```xml
<?xml version="1.1" encoding="UTF-8"?><hudson.model.ListView><name>myview</name><filterExecutors>false</filterExecutors><filterQueue>false</filterQueue><properties class="hudson.model.View$PropertyList"/><jobNames><comparator class="java.lang.String$CaseInsensitiveComparator"/></jobNames><jobFilters/><columns><hudson.views.StatusColumn/><hudson.views.WeatherColumn/><hudson.views.JobColumn/><hudson.views.LastSuccessColumn/><hudson.views.LastFailureColumn/><hudson.views.LastDurationColumn/><hudson.views.BuildButtonColumn/><hudson.plugins.robot.view.RobotListViewColumn plugin="robot@3.2.0"/><hudson.plugins.favorite.column.FavoriteColumn plugin="favorite@2.4.1"/></columns><recurse>false</recurse></hudson.model.ListView>
```

## 2. 创建视图

执行如下命令：

```bash
$ curl -vvv -X POST --USER admin:11133124cbb8558231da29e8eb12b2de71 -d @view.xml -H "Content-Type: text/xml" http://192.168.30.8:8080/createView?name=MyView2
```

执行成功后会新创建一个名为MyView2的视图。

```bash
$ curl -vvv -X POST --USER admin:11133124cbb8558231da29e8eb12b2de71 -d @view.xml -H "Content-Type: text/xml" http://192.168.30.8:8080/createView?name=MyView2
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 192.168.30.8:8080...
* Connected to 192.168.30.8 (192.168.30.8) port 8080 (#0)
* Server auth using Basic with user 'admin'
> POST /createView?name=MyView2 HTTP/1.1
> Host: 192.168.30.8:8080
> Authorization: Basic emhhbmdoYWl5b25nOjExMTMzMTI0Y2JiODU1ODIzMWRhMjllOGViMTJiMmRlNzE=
> User-Agent: curl/7.83.1
> Accept: */*
> Content-Type: text/xml
> Content-Length: 785
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Fri, 16 Dec 2022 06:42:22 GMT
< X-Content-Type-Options: nosniff
< Content-Length: 0
< Server: Jetty(9.4.46.v20220331)
<
* Connection #0 to host 192.168.30.8 left intact
```

## 3. 将job添加到视图

可以将某个job放到创建某个的view中：

```bash
$ curl -vvv -X POST --USER admin:11133124cbb8558231da29e8eb12b2de71 "http://192.168.100.31:8080/view/MyView2/addJobToView?name=my_pipeline"
```

上面的接口请求实现将名为my_pipeline的job添加MyView2中。





参考资料：

1. https://stackoverflow.com/questions/52126961/jenkins-rest-api-create-new-job-view



