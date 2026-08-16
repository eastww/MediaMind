# MediaMind - Smart Media Management Skill

![Claude Skills](https://img.shields.io/badge/Claude-Skills-blue)
![Media Type](https://img.shields.io/badge/Media-Manager-green) [![中文](https://img.shields.io/badge/Language-中文-red.svg)](README_CH.md)

🎬 **A Claude Skill** for intelligent media file management that automatically detects and organizes your media library.

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

*MediaMind - Let MediaMind be your media manager!* 🎉