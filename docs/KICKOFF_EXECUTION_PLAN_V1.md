# 项目重启执行清单 V1

## 里程碑 M0：立项冻结（今天）
- 立项基线：`PROJECT_CHARTER_V1.md`
- 方案对比：`ARCH_OPTIONS_V1.md`
- 调研证据：`RESEARCH_NOTES_V1.md`
- 通过门槛：成功率 >= 85%，单次运行 <= 60 分钟

## 里程碑 M1：选型 POC（1-2 天）

### `project-analyst`
- 输出立项单 V2（补齐非目标、验收边界、约束）

### `system-architect`
- 产出 ADR-001：
  - 主方案：MaaFramework
  - 备选：Airtest
  - 回退条件：POC 未达到 85%/60min

### `sw-engineer`
- 做最小 POC：
  - 识别当日任务文本
  - 解析任务 -> 标准任务 ID
  - 更新计数并输出领奖决策（仅 dry-run）

### `sw-qa`
- 建立 POC 验收脚本：
  - 识别准确率
  - 计数误差
  - 异常恢复

### `devops-ci`
- 建立基础流水线（lint + dry-run + artifact）

## 里程碑 M2：流程自动化（3-5 天）
- 完成“登录 -> 任务识别 -> 执行 -> 统计 -> 领奖策略”闭环
- 增加 fail-safe（急停、超时、重试上限）
- 形成稳定日志与截图证据

## 暂不执行
- 多账号并行
- 云端托管
- 高级对局策略优化
