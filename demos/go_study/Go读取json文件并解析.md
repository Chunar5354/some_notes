## 读取文件

通过`os`和`io/ioutil`两个包来实现文件读取功能

os.Open()将给定的文件名返回成`*os.File`类型，ioutil.ReadAll()函数将文件的所有内容读取到内存，读取出的格式是字节数组`[]byte`

```go
f, err := os.Open("data.json")
if err != nil {
	fmt.Println("file open fail", err)
}
defer f.Close()
content, err := ioutil.ReadAll(f) // content: []unit8
if err != nil {
	fmt.Println("read open fail", err)
}
fmt.Printf("%T, %v\n", content, content)
```

或者也可以直接使用ioutil.ReadFile()来读取`整个`文件：

```go
content, err := ioutil.ReadFile("data.json") // content: []unit8
if err != nil {
	fmt.Println("read open fail", err)
}
fmt.Printf("%T, %v\n", content, content)
```

## json解码

go中的json包编码解码操作都是基于`结构体`来进行的，要想将json字符串解码，首先要创建一个对应格式的结构体

比如有下面的json字符串

```go
`{"name":"Jack", "age":26, "friends":["Jerry", "Tom"]}`
```

要想对其进行解码，首先要创建与之相对应的结构体，结构体成员名的首字母必须` 大写`：

```go
type Person struct {
    Name string
    Age int
    Friends []string
}
```

使用json.Unmarshal()函数来进行解码，它接收两个参数，第一个是要解码的字符串，且需要是字节数组`[]byte`类型，第二个参数是`结构体实例的地址`

```go
type Person struct {
    Name string
    Age int
    Friends []string
}

str := `{"name":"Jack", "age":26, "friends":["Jerry", "Tom"]}`

var person Person
if json.Unmarshal([]byte(str), &person) == nil {
	fmt.Println("json.Unmarshal result: ", person.Name, person.Age, person.Friends)
}
```

### 使用结构体tag

在上面的例子中，因为结构体成员名与json字符串中的键名相同（除了首字母大写），所以在解析时能够直接将对应的值解析到结构体成员中

但有时候需要为结构体成员赋予不同于json键的名称，此时可以使用结构体tag来让json在解析时能够找到对应的结构体成员

结构体tag就是在结构体声明时附加到一个字符串，一般是一系列用空格分割的`键值对`，如

```go
type Person struct {
    PersonName string  `json:"name,omitempty"`
    Age int
    Friends []string
}
```

这种以json键的结构体tag用于encoding/json包的编码与解码行为

比如上面的PersonName成员，它的tag中值的第一部分用于`指定json对象的名字`，在解码时会将json字符串的"name"字段解析到PersonName成员中，第二部分omitempty表示当结构体成员为空或零值时`不生成`该对象（编码时用到）

此时尽管Person结构体中没有名为Name的成员，依然能够将上面的json字符串成功解析
