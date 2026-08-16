# MediaMind 快速开始指南

## 🎬 5分钟快速上手

### 1. 首次使用
```bash
# 进入技能目录
cd ~/.claude/skills

# 整理你的媒体库
python mediamind.py v:/media
```

MediaMind会：
- 📊 扫描所有文件
- 📋 显示将要整理的内容
- 🚀 自动执行整理

### 2. 添加新剧集
```bash
# 1. 手动添加新文件夹到 v:/media/drama/
# 2. 运行 MediaMind
python mediamind.py v:/media/drama
```

MediaMind会：
- 🔍 检测到新内容
- 📤 只整理新增的部分
- ✅ 保持已整理的内容不变

### 3. 日常维护
```bash
# 定期运行，自动处理变化
python mediamind.py v:/media
```

## 🎯 支持的媒体类型

### 电视剧
- 自动识别季和集
- 创建 Season 01/02 文件夹
- 标准化 S01E01.mp4 格式

### 电影
- 保持简洁的文件夹名
- 支持中文标题
- 自动分类

### 动画/漫画
- 通过关键词自动识别
- 灵活的命名规则

## 💡 使用技巧

### 只扫描不整理
```bash
python mediamind.py v:/media --scan-only
```

### 详细输出
```bash
# Linux/macOS
./mediamind.sh v:/media -v

# Windows
mediamind.bat v:/media -v
```

### 批量处理
```bash
# 电视剧
python mediamind.py v:/media/drama

# 电影
python mediamind.py v:/media/movie

# 动画
python mediamind.py v:/media/comic
```

## 🔧 故障排除

### 常见问题

1. **"未找到Python"**
   - 安装Python 3.6+
   - 确保Python在PATH中

2. **"目录不存在"**
   - 检查路径是否正确
   - 确保有读取权限

3. **第一次运行很慢**
   - 正常现象，首次扫描需要索引文件
   - 后续运行会更快

### 重置数据库
如果整理有问题，可以删除数据库文件：
```bash
rm v:/media/.mediamind.json
```

## 🎉 完成了！

现在你已经拥有：
- ✅ 智能的媒体管理工具
- ✅ 自动检测变化
- ✅ 增量更新能力
- ✅ 中文友好界面

**享受 MediaMind 带来的便利吧！** 🎉