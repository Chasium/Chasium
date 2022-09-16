# 前端

此处存放前端代码。

前端代码基于Vue 3.0以及构建工具Vite编写。使用Typescript作为编程语言，并充分利用Vue的工具链及插件——包括Vue-Router，Pinia，Vitest，Cypress，ESLint和Prettier。

前端的样式统一采用Scss作为样式语言。

## 前端运行方法

由于Dependabot经常更新前端使用的库版本，在每次从远程仓库同步前端后，应使用`npm install`重新安装依赖库。

运行前端之前，先通过`npm run lint`进行代码风格检查，并修复错误，再通过`npm run dev`运行。