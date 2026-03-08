# 关键技能候选清单 V1（待审批）

> 当前仅做提案，不安装。安装需口令：`批准安装 <name>@<version>`

## 来源说明（本次补充）
- 本清单中的 skill 名称为“项目内拟定技能包”，将以本地技能形式落地到 `.opencode/skills/<name>/SKILL.md`。
- 拟定技能内容的证据来源（白名单内）如下：
  - MaaFramework: `https://github.com/MaaXYZ/MaaFramework`
  - Airtest: `https://github.com/AirtestProject/Airtest`
  - Poco: `https://github.com/AirtestProject/Poco`
- 审批通过后，执行顺序仍为：来源校验 -> 完整性校验 -> dry-run -> 回报结果 -> 再启用。

## 候选 1
- 技能：`framework-eval-maa@0.1.0`
- 来源：`https://github.com/MaaXYZ/MaaFramework`
- 目标代理：`system-architect`
- 作用：标准化 MaaFramework 复用评估（适配成本、风险、回退条件）
- 所需权限：只读文档分析 + 本地文档写入
- 风险：Low
- 回滚：删除 `.opencode/skills/framework-eval-maa/` 并回退对应代理提示词

## 候选 2
- 技能：`vision-template-matching@0.1.0`
- 来源：`https://github.com/AirtestProject/Airtest`
- 目标代理：`sw-engineer`
- 作用：模板匹配、阈值调优、漂移诊断
- 所需权限：本地代码读写 + 本地截图/模板文件读写
- 风险：Low
- 回滚：删除 `.opencode/skills/vision-template-matching/` 并回退调用说明

## 候选 3
- 技能：`ocr-task-parser@0.1.0`
- 来源：`https://github.com/AirtestProject/Airtest`
- 目标代理：`sw-engineer`
- 作用：任务文本 OCR 与标准任务 ID 映射
- 所需权限：本地 OCR 依赖调用 + 本地解析规则文件读写
- 风险：Medium
- 回滚：禁用 OCR 路径，回退到模板/规则识别

## 候选 4
- 技能：`automation-failsafe@0.1.0`
- 来源：`https://github.com/MaaXYZ/MaaFramework`
- 目标代理：`sw-engineer`, `sw-qa`
- 作用：急停、超时、重试、焦点丢失保护
- 所需权限：本地输入控制封装 + 本地日志写入
- 风险：Low
- 回滚：移除 failsafe 钩子并恢复基础执行器

## 候选 5
- 技能：`regression-stability-gate@0.1.0`
- 来源：`https://github.com/AirtestProject/Airtest`
- 目标代理：`sw-qa`
- 作用：成功率门禁（>=85%）与最长时长门禁（<=60min）
- 所需权限：测试日志读取 + 报告写入
- 风险：Low
- 回滚：移除门禁校验步骤，仅保留手工判定

## 候选 6
- 技能：`pipeline-artifact-report@0.1.0`
- 来源：`https://github.com/MaaXYZ/MaaFramework`
- 目标代理：`devops-ci`
- 作用：结构化日志、截图、失败报告自动归档
- 所需权限：CI 配置读写 + 制品目录写入
- 风险：Low
- 回滚：恢复最小流水线，不做制品归档

## 优先级建议
1. `framework-eval-maa@0.1.0`
2. `vision-template-matching@0.1.0`
3. `automation-failsafe@0.1.0`

## 审批示例
- 批准安装 framework-eval-maa@0.1.0
- 拒绝安装 ocr-task-parser@0.1.0

## 本次审批结果（2026-03-08）
- 已批准：
  - framework-eval-maa@0.1.0
  - vision-template-matching@0.1.0
  - ocr-task-parser@0.1.0
  - automation-failsafe@0.1.0
  - regression-stability-gate@0.1.0
  - pipeline-artifact-report@0.1.0
