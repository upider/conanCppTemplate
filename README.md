# conanCppTemplate

## description

conan 仓库模板

## 创建仓库步骤

1. 创建项目：`conan new conanCppTemplate/0.0.1 --template=cmake_lib`
2. 完成代码
3. 创建本地conan包：`conan create .`
4. 推送到远程：`conan upload conanCppTemplate/0.0.1 --all -r=<repo name>`