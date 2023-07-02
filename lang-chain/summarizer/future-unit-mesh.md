## 未来软件架构：Unit Mesh 架构

> Unit Mesh 是一种基于人工智能生成的分布式架构，与传统的分布式架构不同，Unit Mesh 中的服务单元 (Unit) 是由 AI 生成的，应用程序中的服务和数据抽象为一个个独立的单元，并通过统一的控制平面进行管理和部署。

之所以叫 Unit Mesh，是因为我们写了一个底层服务叫 [Unit Runtime](https://github.com/prompt-engineering/unit-runtime) ，还有参考了 Service Mesh 和 Data Mesh 架构理念，所以 AI 取建议我们叫 \***\*Unit Mesh\*\*** 。

### TLDR 版本

我们初步定义的这个版本（0.1 ，称之为 UnitGenius）有三个核心特性：

- **语言与框架的 DSL**（领域特定语言） 抽象：抽象非编程语言和框架特性，以简化出错的可能性。
- **REPL 即服务**：运行 AI 生成的代码，并提供对应的 API 服务。
- **AI 设计的适应性结构**：自我适应的 API 服务架构，以在不同的环境下自动调整和优化。

开发者可以通过与 AI 交互，生成一定程度的 DSL 抽象化代码，然后在 REPL 即 Serverless 服务上运行和测试这些代码。开发者还可以将这些代码提交给 AI 进行自动化运维，AI 会对代码进行优化和调整，从而进一步提高 API 服务的性能和可靠性。

开始正文的废话版本。

### Unit Mesh 初步 Demo：DSL + REPL = Unit Server

详细过程，见本文的后半部分。

前端页面：[https://prompt.phodal.com/zh-CN/click-flow/unit-mesh-unit-server/](https://prompt.phodal.com/zh-CN/click-flow/unit-mesh-unit-server/)

首先，你需要克隆一下 Unit Server 的代码：[https://github.com/prompt-engineering/unit-server](https://github.com/prompt-engineering/unit-server) 

然后，选择 kotlin-repl 或者 typescript-repl 对应 Kotlin、TypeScript 两种语言。

然后，按对应的 README 运行起你的 Unit Server。

接着，在 ChatFlow 里让 ChatGPT 生成如下的代码，并点击 `Run` 按钮：

```jsx
%spring

@RestController
object Pages {
   @GetMapping("/")
   fun main() = "It works!"
}
```

最后，你就可以得到一个正在运行的服务（该功能还在开发中）：[http://localhost:8080/](http://localhost:8080/hello) ，访问该服务后，如果的应该是 It works。

---

PS：这里有一个手动加入调用 Application 类和调用 main 方法的代码，因为需要做静态分析，才能确定使用的框架，暂时没写在 Unit Server 代码中。

