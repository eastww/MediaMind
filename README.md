# MediaMind - 媒体智能管家 | MediaMind - Smart Media Management Tool

[English](#english-version) | [中文](#chinese-version)

## 🌟 Language Selector / 语言选择器
<div align="center">
  <button onclick="toggleLanguage()" id="langToggle" style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 25px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
  ">
    🌐 切换 English / Switch to Chinese
  </button>
</div>

<script>
function toggleLanguage() {
  const enContent = document.getElementById('enContent');
  const zhContent = document.getElementById('zhContent');
  const toggleBtn = document.getElementById('langToggle');
  
  if (enContent.style.display === 'none') {
    enContent.style.display = 'block';
    zhContent.style.display = 'none';
    toggleBtn.innerHTML = '🌐 切换 English / Switch to Chinese';
  } else {
    enContent.style.display = 'none';
    zhContent.style.display = 'block';
    toggleBtn.innerHTML = '🌐 切换中文 / Switch to English';
  }
}

// Set default language
document.addEventListener('DOMContentLoaded', function() {
  const enContent = document.getElementById('enContent');
  const zhContent = document.getElementById('zhContent');
  
  // Default to Chinese
  enContent.style.display = 'none';
  zhContent.style.display = 'block';
});
</script>

---

## English Version

🎬 An intelligent media file management tool that automatically detects and organizes your media library.

## ✨ Features

### Intelligent Detection
- ✅ **Auto Scan** - Records all media files
- ✅ **Change Detection** - Identifies new, deleted, and modified files
- ✅ **Smart Classification** - Automatically recognizes TV shows, movies, animations
- ✅ **Status Tracking** - Records historical status of each media

### Auto Organization
- ✅ **Incremental Updates** - Only organizes changed files
- ✅ **Smart Naming** - Automatically standardizes filenames and folders
- ✅ **Structure Optimization** - Creates unified directory structure
- ✅ **Memory Function** - Won't reorganize already organized files

### User Friendly
- ✅ **Chinese Interface** - Fully localized user experience
- ✅ **Detailed Reports** - Clearly shows changes
- ✅ **Interactive Confirmation** - Shows changes before execution
- ✅ **Error Recovery** - Supports rollback and repair

## 🚀 Quick Start

### Basic Usage

```bash
# Scan and organize media library
python mediamind.py v:/media

# Scan only, no organization
python mediamind.py v:/media --scan-only

# Show help
python mediamind.py --help
```

### Workflow

1. **First Run**
   ```bash
   python mediamind.py v:/media/drama
   ```
   MediaMind will scan all files and record status

2. **Add New Episodes**
   ```bash
   # Manually add new folders to v:/media/drama/
   python mediamind.py v:/media/drama
   ```
   MediaMind will automatically detect new content and organize

3. **Regular Maintenance**
   ```bash
   # Run periodically, only process changed parts
   python mediamind.py v:/media
   ```

## 📋 Smart Recognition

### TV Show Recognition
- Recognizes through season, episode, 第 keywords
- Supports S01E01 format parsing
- Automatically creates Season 01/02 folders

### Movie Recognition
- Defaults to movie classification
- Supports special character handling
- Keeps folder names concise

### Animation/Manga Recognition
- Automatically recognizes through keywords
- Supports Japanese and American comic classification
- Flexible naming rules

## 🔧 Advanced Features

### Database Mechanism
MediaMind creates `.mediamind.json` file in media directory to record:

```json
{
  "last_scan": "2024-01-01T12:00:00",
  "shows": [
    {
      "name": "Reply 1988",
      "type": "tv",
      "files": [...],
      "last_updated": "2024-01-01T12:00:00",
      "status": "organized"
    }
  ]
}
```

### Incremental Updates
- Automatically organizes when new files are detected
- Won't reorganize already organized files
- Supports file modification detection

### Change Reports
Running shows detailed change reports:

```
📊 Detected Changes:
------------------------------
🆕 New (2):
   • Speed Racers (2023)
   • Spider-Man
🔄 Modified (1):
   • Reply 1988
```

## 📁 Directory Structure

### Organized Standard Structure

#### TV Shows
```
Reply 1988 (2015)/
├── Season 01/
│   ├── S01E01.mp4
│   ├── S01E02.mp4
│   └── ...
├── poster.jpg
└── .mediamind.json
```

#### Movies
```
Spider-Man (2021)/
├── movie.mp4
└── .mediamind.json
```

#### Animation
```
Spirited Away (2001)/
├── movie.mp4
└── .mediamind.json
```

## 🛠️ Configuration Options

### Command Line Arguments

```bash
python mediamind.py [options] <directory>

Options:
  -h, --help            Show help information
  --scan-only          Scan only, no organization
```

### Environment Variables

- `MEDIAMIND_VERBOSE` - Verbose output mode
- `MEDIAMIND_DRY_RUN` - Dry run mode

## 🚨 Notes

### First Use
- Recommend using `--scan-only` first to see what will be processed
- Important files please backup first

### Filename Conventions
- Avoid special characters
- Chinese filenames fully supported
- Year information helps with classification

### Performance Considerations
- Large media library first scan may be slow
- Subsequent incremental updates will be faster
- File checksums only calculated when needed

## 🔄 Comparison with Old Version

| Feature | MediaMind | Old Version |
|---------|-----------|-------------|
| Smart Detection | ✅ Auto scan changes | ❌ Manual specification |
| Incremental Updates | ✅ Only process changes | ❌ Reorganize all |
| Memory Function | ✅ Records history | ❌ No memory |
| Change Reports | ✅ Detailed display | ❌ No reports |
| User Experience | ✅ Chinese interface | ❌ English output |

## 📈 Usage Scenarios

### 1. New Media Library
```bash
# Setup new media library
python mediamind.py v:/media/new_shows
```

### 2. Regular Maintenance
```bash
# Run periodically, automatically process new content
python mediamind.py v:/media
```

### 3. Problem Fixing
```bash
# If organization has issues, delete .mediamind.json and retry
rm v:/media/.mediamind.json
python mediamind.py v:/media
```

## 🤝 Contributing

Issues and suggestions are welcome!

### Development Process
1. Fork project
2. Create feature branch
3. Commit changes
4. Create Pull Request

## 📄 License

MIT License

---

Let MediaMind be your media manager! 🎉

---

## Chinese Version

🎬 一个智能化的媒体文件管理工具，自动检测和组织你的媒体库。

## ✨ 特性

### 智能检测
- ✅ **自动扫描** - 记录所有媒体文件
- ✅ **变化检测** - 识别新增、删除、修改的文件
- ✅ **智能分类** - 自动识别电视剧、电影、动画
- ✅ **状态跟踪** - 记录每个媒体的历史状态

### 自动整理
- ✅ **增量更新** - 只整理有变化的文件
- ✅ **智能命名** - 自动标准化文件名和文件夹
- ✅ **结构优化** - 创建统一的目录结构
- ✅ **记忆功能** - 不会重复整理已整理的文件

### 用户友好
- ✅ **中文界面** - 完全本地化的用户体验
- ✅ **详细报告** - 清晰展示变化情况
- ✅ **交互确认** - 在执行前显示变化并确认
- ✅ **错误恢复** - 支持回滚和修复

## 🚀 快速开始

### 基本使用

```bash
# 扫描并整理媒体库
python mediamind.py v:/media

# 只扫描，不整理
python mediamind.py v:/media --scan-only

# 查看帮助
python mediamind.py --help
```

### 工作流程

1. **首次运行**
   ```bash
   python mediamind.py v:/media/drama
   ```
   MediaMind会扫描所有文件并记录状态

2. **添加新剧集**
   ```bash
   # 手动添加新文件夹到 v:/media/drama/
   python mediamind.py v:/media/drama
   ```
   MediaMind会自动检测新内容并整理

3. **日常维护**
   ```bash
   # 定期运行，只处理变化的部分
   python mediamind.py v:/media
   ```

## 📋 智能识别

### 电视剧识别
- 通过季、集、第等关键词识别
- 支持 S01E01 格式解析
- 自动创建 Season 01/02 文件夹

### 电影识别
- 默认归类为电影
- 支持特殊字符处理
- 保持文件夹名简洁

### 动画/漫画识别
- 通过关键词自动识别
- 支持日漫、美漫分类
- 灵活的命名规则

## 🔧 高级功能

### 数据库机制
MediaMind在媒体目录中创建 `.mediamind.json` 文件来记录：

```json
{
  "last_scan": "2024-01-01T12:00:00",
  "shows": [
    {
      "name": "请回答1988",
      "type": "tv",
      "files": [...],
      "last_updated": "2024-01-01T12:00:00",
      "status": "organized"
    }
  ]
}
```

### 增量更新
- 检测到新文件时自动整理
- 不会重复整理已整理的文件
- 支持文件修改检测

### 变化报告
运行时会显示详细的变化报告：

```
📊 检测到的变化:
------------------------------
🆕 新增 (2):
   • 极速车魂 (2023)
   • 蜘蛛侠
🔄 修改 (1):
   • 请回答1988
```

## 📁 目录结构

### 整理后的标准结构

#### 电视剧
```
请回答1988 (2015)/
├── Season 01/
│   ├── S01E01.mp4
│   ├── S01E02.mp4
│   └── ...
├── poster.jpg
└── .mediamind.json
```

#### 电影
```
蜘蛛侠 (2021)/
├── movie.mp4
└── .mediamind.json
```

#### 动画
```
千与千寻 (2001)/
├── movie.mp4
└── .mediamind.json
```

## 🛠️ 配置选项

### 命令行参数

```bash
python mediamind.py [选项] <目录>

选项:
  -h, --help            显示帮助信息
  --scan-only          只扫描，不整理
```

### 环境变量

- `MEDIAMIND_VERBOSE` - 详细输出模式
- `MEDIAMIND_DRY_RUN` - 试运行模式

## 🚨 注意事项

### 首次使用
- 建议先使用 `--scan-only` 查看将要处理的内容
- 重要文件请先备份

### 文件名规范
- 避免使用特殊字符
- 中文文件名完全支持
- 年份信息有助于分类

### 性能考虑
- 大媒体库首次扫描可能较慢
- 后续增量更新会更快
- 文件校验和只在需要时计算

## 🔄 与旧版本对比

| 特性 | MediaMind | 旧版本 |
|------|-----------|--------|
| 智能检测 | ✅ 自动扫描变化 | ❌ 需手动指定 |
| 增量更新 | ✅ 只处理变化 | ❌ 全部重新整理 |
| 记忆功能 | ✅ 记录历史状态 | ❌ 无记忆 |
| 变化报告 | ✅ 详细变化展示 | ❌ 无报告 |
| 用户体验 | ✅ 中文界面 | ❌ 英文输出 |

## 📈 使用场景

### 1. 新媒体库
```bash
# 设置新媒体库
python mediamind.py v:/media/new_shows
```

### 2. 定期维护
```bash
# 定期运行，自动处理新增内容
python mediamind.py v:/media
```

### 3. 问题修复
```bash
# 如果整理有问题，删除 .mediamind.json 后重试
rm v:/media/.mediamind.json
python mediamind.py v:/media
```

## 🤝 贡献

欢迎提交Issue和建议！

### 开发流程
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 📄 许可证

MIT License

---

**让MediaMind成为你的媒体管家！** 🎉