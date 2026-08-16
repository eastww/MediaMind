#!/usr/bin/env python3
"""
MediaMind - 媒体智能管家
自动扫描、检测和整理媒体文件的智能工具
"""

import os
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class MediaFile:
    """媒体文件信息"""
    path: str
    name: str
    size: int
    modified: str
    checksum: str
    media_type: str
    season: Optional[int] = None
    episode: Optional[int] = None


@dataclass
class MediaShow:
    """剧集/电影信息"""
    name: str
    path: str
    type: str  # 'tv' | 'movie' | 'comic'
    files: List[MediaFile]
    last_updated: str
    status: str  'pending' | 'organized' | 'error'


class MediaMind:
    """媒体智能管家核心类"""

    def __init__(self, media_dir: str, db_path: str = None):
        self.media_dir = Path(media_dir)
        self.db_path = db_path or os.path.join(media_dir, ".mediamind.json")
        self.media_types = {
            'tv': {
                'name': '电视剧',
                'indicators': ['季', '集', '第', 'S', 'E'],
                'file_pattern': r'.*(S\d{2}E\d{2}|\d{1,2}).*',
                'season_pattern': r'Season \d{2}'
            },
            'movie': {
                'name': '电影',
                'indicators': [],
                'file_pattern': r'.*',
                'season_pattern': None
            },
            'comic': {
                'name': '漫画/动画',
                'indicators': [],
                'file_pattern': r'.*',
                'season_pattern': None
            }
        }

        self.load_database()

    def load_database(self):
        """加载媒体数据库"""
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.known_shows = {show['name']: MediaShow(**show)
                                   for show in data.get('shows', [])}
                self.last_scan = data.get('last_scan')
        else:
            self.known_shows = {}
            self.last_scan = None

    def save_database(self):
        """保存媒体数据库"""
        data = {
            'last_scan': datetime.now().isoformat(),
            'shows': [asdict(show) for show in self.known_shows.values()]
        }
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def scan_directory(self) -> Dict[str, MediaShow]:
        """扫描目录，发现所有媒体文件"""
        print(f"正在扫描目录: {self.media_dir}")

        new_shows = {}
        video_extensions = {'.mp4', '.mkv', '.avi', '.webm', '.wmv', '.flv'}

        for item in self.media_dir.iterdir():
            if not item.is_dir():
                continue

            # 检测媒体类型
            media_type = self._detect_media_type(item.name)

            # 扫描文件
            files = self._scan_show_files(item, media_type)

            if files:
                show = MediaShow(
                    name=item.name,
                    path=str(item),
                    type=media_type,
                    files=files,
                    last_updated=datetime.now().isoformat(),
                    status='pending'
                )
                new_shows[item.name] = show

        return new_shows

    def _detect_media_type(self, name: str) -> str:
        """检测媒体类型"""
        name_lower = name.lower()

        # 电视剧检测
        tv_indicators = ['季', '集', '第', 's', 'e']
        if any(indicator in name_lower for indicator in tv_indicators):
            return 'tv'

        # 漫画/动画检测
        comic_keywords = ['漫画', '动画', 'anime', 'cartoon', 'comic']
        if any(keyword in name_lower for keyword in comic_keywords):
            return 'comic'

        # 默认为电影
        return 'movie'

    def _scan_show_files(self, show_dir: Path, media_type: str) -> List[MediaFile]:
        """扫描剧集文件夹中的文件"""
        files = []
        video_extensions = {'.mp4', '.mkv', '.avi', '.webm'}

        for root, dirs, filenames in os.walk(show_dir):
            for filename in filenames:
                file_path = Path(root) / filename

                if file_path.suffix.lower() in video_extensions:
                    # 计算文件校验和（可选，用于检测文件变化）
                    checksum = self._calculate_checksum(file_path)

                    # 解析季和集信息
                    season, episode = self._parse_episode_info(file_path, media_type)

                    file_info = MediaFile(
                        path=str(file_path),
                        name=filename,
                        size=file_path.stat().st_size,
                        modified=datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        checksum=checksum,
                        media_type=media_type,
                        season=season,
                        episode=episode
                    )
                    files.append(file_info)

        return files

    def _calculate_checksum(self, file_path: Path, chunk_size: int = 8192) -> str:
        """计算文件校验和（简化版，只读取头部）"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read(chunk_size)).hexdigest()
        except:
            return ""

    def _parse_episode_info(self, file_path: Path, media_type: str) -> tuple:
        """解析季和集信息"""
        season = None
        episode = None

        if media_type == 'tv':
            # 匹配 S01E01 格式
            s_match = file_path.name.upper().match(r'S(\d{2})E(\d{2})')
            if s_match:
                season = int(s_match.group(1))
                episode = int(s_match.group(2))
            else:
                # 匹配 01, 02 格式
                num_match = file_path.name.match(r'(\d{1,2})')
                if num_match:
                    episode = int(num_match.group(1))

        return season, episode

    def detect_changes(self, new_shows: Dict[str, MediaShow]) -> Dict[str, str]:
        """检测变化（新增、删除、修改）"""
        changes = {
            'new': [],
            'deleted': [],
            'modified': [],
            'unchanged': []
        }

        # 检测新增和修改
        for name, new_show in new_shows.items():
            if name not in self.known_shows:
                changes['new'].append(name)
            else:
                known_show = self.known_shows[name]
                if self._show_changed(known_show, new_show):
                    changes['modified'].append(name)
                else:
                    changes['unchanged'].append(name)

        # 检测删除
        for name in self.known_shows:
            if name not in new_shows:
                changes['deleted'].append(name)

        return changes

    def _show_changed(self, known_show: MediaShow, new_show: MediaShow) -> bool:
        """检查剧集是否发生变化"""
        # 检查文件数量
        if len(known_show.files) != len(new_show.files):
            return True

        # 检查文件是否相同
        known_files = {f.name: f for f in known_show.files}
        new_files = {f.name: f for f in new_show.files}

        # 检查新增/删除文件
        if set(known_files.keys()) != set(new_files.keys()):
            return True

        # 检查文件修改
        for name, new_file in new_files.items():
            known_file = known_files[name]
            if known_file.modified != new_file.modified:
                return True

        return False

    def organize_show(self, show: MediaShow) -> bool:
        """整理单个剧集"""
        try:
            print(f"正在整理: {show.name}")

            if show.type == 'tv':
                self._organize_tv_show(show)
            elif show.type == 'movie':
                self._organize_movie(show)
            elif show.type == 'comic':
                self._organize_comic(show)

            show.status = 'organized'
            return True

        except Exception as e:
            print(f"整理失败: {show.name} - {e}")
            show.status = 'error'
            return False

    def _organize_tv_show(self, show: MediaShow):
        """整理电视剧"""
        show_dir = Path(show.path)

        # 创建标准目录结构
        season_dirs = {}

        # 分析文件并创建季文件夹
        for file in show.files:
            if file.season:
                season_name = f"Season {file.season:02d}"
                season_path = show_dir / season_name

                if season_path not in season_dirs:
                    season_path.mkdir(exist_ok=True)
                    season_dirs[season_path] = []

                # 移动文件到季文件夹
                src_path = Path(file.path)
                dst_path = season_path / src_path.name

                if src_path != dst_path:
                    shutil.move(str(src_path), str(dst_path))

        # 更新文件路径
        show.files = []
        for season_path, files in season_dirs.items():
            for file_path in season_path.glob("*"):
                if file_path.is_file() and file_path.suffix.lower() in {'.mp4', '.mkv', '.avi', '.webm'}:
                    # 重新解析文件信息
                    season = int(season_path.name.split()[1])
                    episode = self._parse_episode_info(file_path, 'tv')[1]

                    show.files.append(MediaFile(
                        path=str(file_path),
                        name=file_path.name,
                        size=file_path.stat().st_size,
                        modified=datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                        checksum=self._calculate_checksum(file_path),
                        media_type='tv',
                        season=season,
                        episode=episode
                    ))

    def _organize_movie(self, show: MovieShow):
        """整理电影"""
        # 电影不需要特殊整理，只需确保名称规范
        pass

    def _organize_comic(self, show: MediaShow):
        """整理漫画/动画"""
        # 漫画/动画不需要特殊整理
        pass

    def auto_organize(self) -> Dict[str, Any]:
        """自动整理流程"""
        print("🎬 MediaMind - 媒体智能管家")
        print("=" * 50)

        # 1. 扫描目录
        new_shows = self.scan_directory()

        # 2. 检测变化
        changes = self.detect_changes(new_shows)

        # 3. 报告变化
        self._report_changes(changes)

        # 4. 询问用户是否继续
        if not changes['new'] and not changes['modified']:
            print("✅ 没有检测到变化")
            return {'status': 'no_changes', 'changes': changes}

        # 5. 执行整理
        results = {}
        for name in changes['new'] + changes['modified']:
            show = new_shows[name]
            success = self.organize_show(show)
            results[name] = success

        # 6. 更新数据库
        self.known_shows.update(new_shows)
        self.save_database()

        return {
            'status': 'completed',
            'changes': changes,
            'results': results
        }

    def _report_changes(self, changes: Dict[str, List[str]]):
        """报告变化"""
        print("\n📊 检测到的变化:")
        print("-" * 30)

        if changes['new']:
            print(f"🆕 新增 ({len(changes['new'])}):")
            for name in changes['new']:
                print(f"   • {name}")

        if changes['deleted']:
            print(f"🗑️  删除 ({len(changes['deleted'])}):")
            for name in changes['deleted']:
                print(f"   • {name}")

        if changes['modified']:
            print(f"🔄 修改 ({len(changes['modified'])}):")
            for name in changes['modified']:
                print(f"   • {name}")

        if changes['unchanged']:
            print(f"✅ 未变化 ({len(changes['unchanged'])}):")
            for name in changes['unchanged'][:5]:  # 只显示前5个
                print(f"   • {name}")
            if len(changes['unchanged']) > 5:
                print(f"   ... 还有 {len(changes['unchanged']) - 5} 个未变化")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='MediaMind - 媒体智能管家')
    parser.add_argument('directory', help='媒体目录路径')
    parser.add_argument('--scan-only', action='store_true', help='只扫描，不整理')

    args = parser.parse_args()

    # 创建MediaMind实例
    mediamind = MediaMind(args.directory)

    if args.scan_only:
        new_shows = mediamind.scan_directory()
        print(f"发现 {len(new_shows)} 个媒体:")
        for name, show in new_shows.items():
            print(f"• {name} ({len(show.files)} 个文件)")
    else:
        # 自动整理
        result = mediamind.auto_organize()

        if result['status'] == 'completed':
            print("\n🎉 整理完成!")
        else:
            print("\n✅ 无需整理")


if __name__ == '__main__':
    main()