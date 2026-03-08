# 方案调研记录 V1（外部资料）

## 调研目标
- 验证是否能复用现成框架，减少自研成本。
- 评估 MaaFramework 与 Airtest/Poco 在本项目的落地适配度。

## 来源与观察

### 1) MaaFramework
- 来源：`https://github.com/MaaXYZ/MaaFramework`
- 观察：
  - 明确定位“基于图像识别的自动化黑盒测试框架”。
  - 提供跨语言生态（PyPI/NuGet/npm/go/rust），社区活跃。
  - 有 Pipeline 协议与调试工具生态，适合流程化任务编排。

### 2) Airtest
- 来源：`https://github.com/AirtestProject/Airtest`
- 观察：
  - 成熟的跨平台 UI 自动化框架，强调图像识别与脚本复用。
  - 支持 CLI 与 Python API，适合快速原型。
  - 社区体量大，文档与样例较多。

### 3) Poco
- 来源：`https://github.com/AirtestProject/Poco`
- 观察：
  - 偏向“UI 层级/控件树”驱动自动化。
  - 适配 Unity/安卓/iOS 等场景较强。
  - 需目标应用暴露或可访问 UI 结构时效果更好。

## 与本项目的匹配结论
- 你的项目核心是“黑盒图像识别 + 状态流程 + 计数决策”，优先匹配 MaaFramework 或 Airtest。
- 当前建议：
  1. 先用 MaaFramework 做最小 POC（任务识别 + 计数 + 领奖策略）。
  2. 若适配成本或稳定性不达标，再切 Airtest 方案。
  3. Poco 作为补充路线（当可稳定获取 UI 层级时再引入）。

## POC 通过门槛
- 成功率 >= 85%
- 单次运行 <= 60 分钟
- 出错可恢复，且日志可追溯

## 待确认
- 是否允许并行做 Airtest 备份 POC（1-2 天）以降低选型风险。
